import React, { Component,Suspense,lazy } from 'react';
import './App.css';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Lander from './Pages/lander/lander';
import Register from './Pages/register/register';
import History from './Pages/History/History';


const Home = lazy(() => import('./Pages/home/home'));
const Rooms = lazy(()=> import('./Pages/Rooms/Rooms'));
const Notification = lazy(()=>import('./Pages/Notification/Notification'));
const Profile = lazy(()=> import('./Pages/Profile/Profile'))

class App extends Component {

  constructor(){
    super()
    
    this.state = {
      isLoaded:false
    }
  }

  componentDidMount(){
    this.setState({
      isLoaded:true
    })
  }

  render(){
    return (
      <div className="App">
        <Router>
          <Suspense fallback={<div> Hold On We're Calculating Data !! </div>}>
            
          <Switch>
            <Route path='/' exact component={Lander} />
            <Route path='/register' exact component={Register} />
            <Route path='/home' exact component={Home} />
            <Route path='/home/:roomname' exact component={Rooms} />
            <Route path='/notification' exact component={Notification} />
            <Route path='/profile' exact component={Profile} />
            <Route path='/history' exact component={History} />
            </Switch>
          </Suspense>
        </Router>
      </div>
    );
  }
}

export default App;
