import React, { Component } from 'react'
import Navbar from '../../Components/Navbar/Navbar'
import './register.css';
import { Redirect } from 'react-router-dom';
// In My Project Every This is Written from Scratch
class register extends Component {
    constructor(props) {
        super(props)

        this.state = {
                 isLoggedIn:false
        }
    }

    login = (event)=>{
        event.preventDefault();
        this.setState({isLoggedIn:true});

        localStorage.setItem("token","true");
    }



    render() {
       if(!this.state.isLoggedIn && !(localStorage.getItem("token") == "true")){ // Means Here this.state.isLoggedIn is true
        return (
            <div>
            <Navbar />
                <div className='header'>
                    Save Some Energy with us !
                </div>
                <form onSubmit={this.login}>
                    <div className='form-group'>
                        <input id='registerphone' className='lead' type='number' placeholder='Enter Your Phone Number' />
                    </div>
                  <small className=''>By Submitting here you are agreeing Terms and Conditions</small>
                    <div className='form-group'>
                        <button id='registerbtn'>Submit, Let's Save</button> 
                    </div>
                </form>
            </div>
        )
       }else{
           return(<Redirect to='/home' />)
       }
    }
}

export default register
