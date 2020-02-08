import requests, json
import time
from math import *
import pandas as pd
import numpy as np
from keras.models import Sequential
from datetime import datetime as dt
from scipy.stats import zscore
import tensorflow as tf
from tensorflow.keras import layers


def Tempc2(city, ac_bool, ac_temp):
    api_key = "5aac8d7e066c9171f11fe957c064b0c6"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    x = response.json()
    if x['cod'] != 404:
        y = x['main']
        temp = y['temp']
        print(f"y = {y}")
        avg_temp = (float(y['temp_max']) + float(y['temp_min']))/2
        print(f'avg = {avg_temp}')
        print(f'temp = {temp}')
        if temp > 308:
          if temp - ac_temp > 5:
            if ac_bool == True:
              op = "gtg"    
            elif ac_bool == False:
              x = temp - 5
              x = x - 273
              op = f"you can start ac with {x} temperature"
        elif floor(temp) < 308:
          if temp - ac_temp > 5:
            if ac_bool == True:
              print(1)
              op = "gtg"
            elif ac_bool == False:
              print(2)
              op = "you can start ac"
          else:
            if ac_bool == True:
              print(3)
              op = "turn off"
            elif ac_bool == False:
              print(4)
              op = "gtg"
    return op

def json_convert(h, k):
    x = {}
    x[h] = k
    x = json.dumps(x)
    return x


def Ml(z):
    f = "NCENT.csv"
    df = pd.read_csv(f)
    def makeUsefulDf(df, noise=2.5, hours_prior=24):
      if 'dates' not in df.columns:
          df['dates'] = df.apply(lambda x: dt(int(x['year']), int(x['month']), int(x['day']), int(x['hour'])), axis=1)
      r_df = pd.DataFrame()
      r_df["loads_n"] = zscore(df["load"])
      r_df["loads_prev_n"] = r_df["loads_n"].shift(hours_prior)
      r_df["loads_prev_n"].bfill(inplace=True)
      def _chunks(l, n):
          return [l[i:i+n] for i in range(0, len(l), n)]
      n = np.array([val for val in _chunks(list(r_df["loads_n"]), 24) for _ in range(24)])
      l = ["l" + str(i) for i in range(24)]
      for i, s in enumerate(l):
          r_df[s] = n[:, i]
          r_df[s] = r_df[s].shift(hours_prior)
          r_df[s] = r_df[s].bfill()
      r_df.drop(['loads_n'], axis=1, inplace=True)
      r_df["years_n"] = zscore(df["dates"].dt.year)
      r_df = pd.concat([r_df, pd.get_dummies(df.dates.dt.hour, prefix='hour')], axis=1)
      r_df = pd.concat([r_df, pd.get_dummies(df.dates.dt.dayofweek, prefix='day')], axis=1)
      r_df = pd.concat([r_df, pd.get_dummies(df.dates.dt.month, prefix='month')], axis=1)
      temp_noise = df['tempc'] + np.random.normal(0, noise, df.shape[0])
      r_df["temp_n"] = zscore(temp_noise)
      r_df['temp_n^2'] = zscore([x*x for x in temp_noise])
      return r_df
    x = makeUsefulDf(df)
    y = df["load"]
    shape = x.shape[1]
    epochs=10    
    model = tf.keras.Sequential()
    model.add(layers.Dense(shape, activation=tf.nn.relu, input_shape=[len(x.keys())]))
    model.add(layers.Dense(shape, activation=tf.nn.relu))
    model.add(layers.Dense(shape, activation=tf.nn.relu))
    model.add(layers.Dense(shape, activation=tf.nn.relu))
    model.add(layers.Dense(shape, activation=tf.nn.relu))
    model.add(layers.Dense(1))   
    def MAPE(predictions, answers):
      assert len(predictions) == len(answers)
      return sum([abs(x - y)/(y+1e-5) for x, y in zip(predictions, answers)])/len(answers)*100
    optimizer = tf.keras.optimizers.RMSprop(0.0001)
    model.compile(loss="mean_squared_error",optimizer=optimizer,metrics=["mean_absolute_error", "mean_squared_error"])
    early_stop = tf.keras.callbacks.EarlyStopping(monitor="mean_absolute_error", patience=3)
    x_train, y_train = x[:-17520], y[:-17520]
    model.fit(x_train, y_train, epochs=1, verbose=0, callbacks=[early_stop])
    predictions = [float(f) for f in model.predict(x[-8760:])]
    train = [float(f) for f in model.predict(x[:-8760])]
    sx = pd.DataFrame({'TimeStamp': df.dates[-8760:], 'Load_Prediction': predictions})
    dfdv = list(sx.TimeStamp)
    for i in range(len(dfdv)):
      dfdv[i] = str(dfdv[i])
    xc = pd.DataFrame({'dt': dfdv, 'lp':predictions})
    x = xc[xc["dt"].str.contains(z)]['lp']
    x = list(x)
    return x