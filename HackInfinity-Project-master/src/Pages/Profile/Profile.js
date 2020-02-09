import React, { Component } from 'react'
import Navbar from '../../Components/Navbar/Navbar'
import Footer from '../../Components/Footer/Footer'

import './Profile.css';
class Profile extends Component {
    constructor(props) {
        super(props)
        let data = localStorage.getItem("userdata");

        this.state = {
            User:(JSON.parse(data))[0]

        }
        console.log(this.state.User)
    }

    render() {
        return (
            <div>
                <Navbar />
                    <div className='Profile-Container'>
                    <img  className='User-Photo ripple' style={{height:'200px'}} src='https://avatars0.githubusercontent.com/u/24816726?v=4' />
                    <div className='User-Profile ripple'>
                            <i className='fa fa-users userprofilename'></i>
                            {this.state.User.name}
                            <br />
                            <i className='fa fa-envelope userprofilename'></i>{this.state.User.email}
                            <br />
                            <i className='fa fa-phone userprofilename'></i>{this.state.User.phone}
                            <br />
                            <i className='fa fa-map-marker userprofilename'></i>{this.state.User.address}
                    </div>

                    <div className='Profile-bar'>

                    </div>
                    </div>
                <Footer />
            </div>
        )
    }
}

export default Profile
