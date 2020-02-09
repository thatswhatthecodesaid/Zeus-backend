import React, { Component } from 'react'
import Navbar from '../../Components/Navbar/Navbar'
import Footer from '../../Components/Footer/Footer'
import './Notification.css'
import Host from '../../myIp'
class Notification extends Component {
    constructor(props) {
        super(props)

        this.state = {
                 
        }

        for(let i = 0;i<10;i++){

        }
        // List of Notification Data - 
        // 1. Notify Title
        // 2. body
        /* 3. Optimization
              Warning
              On-Off Lock Room
        // Leaderboard - GitHub
        // User Profile - Photu, Naam, Adres, Phone Number, score(init = 0), email 
        

        */
       this.quotes = ["100-200 zyada lele par electricity bachale", "Keep calm and save electricity", "Save electricity, Got it?", "There is a thin line between using electricity and wasting electricity", "Electricity: Use it – Don’t abuse it"];

    }

    async componentDidMount(){
        let reponse = await fetch("http://"+Host.host+":8000/iot/ac/");
        let data = await reponse.json();

        console.log(data.task)

    }

    render() {
        return (
            <span>
                <Navbar />
                <div className='Notification-Container'>
                    <div className='Notification'>
                        <div className='Notification-Content'>
                            Your Bill Amount Reached
                            <br />
                            <small></small>
                        </div>
                    </div>
                    <div className='Notification'>
                        <div className='Notification-Content'>
                            Your Bill Amount Reached
                        </div>
                    </div>
                </div>
                <Footer />
            </span>
        )
    }
}

export default Notification;