import time
import numpy as np
from datetime import datetime, timedelta
import csv
import pandas as pd
from django.core.files.storage import FileSystemStorage

def applianceSimulator(name, a_wh, stop, start, a_name):
    File = f'C:\madr1x\Dev\Django\{name}.csv'
    with open(File, "w") as newFile:
        nfw = csv.writer(newFile)
        nfw.writerow(["Day","Name","From","Too","Usage"])
        for i in range(100):
            x = np.random.randint(low = 0, high = 60, size = 1)[0]
            y = np.random.randint(low = 0, high = 60, size = 1)[0]
            a_wm =float(a_wh)/60
            t_format = "%H:%M"
            ad_format = f'%Y-%m-%d %H:%M:%S'
            ad_on = datetime.strptime(start, t_format) + timedelta(minutes=int(y))
            ad_off = datetime.strptime(stop, t_format) + timedelta(minutes=int(x))
            off_time = str(ad_off)
            on_time = str(ad_on)
            diff = datetime.strptime(off_time, ad_format) - datetime.strptime(on_time, ad_format)
            usage = ((diff.seconds)/60)*a_wm
            too = f"{ad_off.hour}:{ad_off.minute}"
            frm = f"{ad_on.hour}:{ad_on.minute}"
            print(f"Day {i} from-{frm} to-{too} {usage}")
            nfw.writerow([i,a_name,frm,too,usage])



        
