import React, { Component } from 'react'
import Navbar from '../../Components/Navbar/Navbar'
import Footer from '../../Components/Footer/Footer'
import './History.css';
import Host from '../../myIp';
import { ThemeConsumer } from 'styled-components';
class History extends Component {
    constructor(props) {
        super(props)
        let userdata = localStorage.getItem('userdata');
        let User = JSON.parse(userdata);

        this.progressStatus = [0,30,45,60,75,90,95,100];
        // Status - 30, 45, 60,75,90,95
        this.classOfProgessStatus = "pie-wrapper progress-"+this.progressStatus[7];
        this.state = {
            progressBarPercentage:this.classOfProgessStatus,
            userData:User[0],
            Bills:[]
        }
        this.count = 30
        
    }

    async componentDidMount(){
        let response = await fetch(
            "http://"+Host.host+":8000/api/use/"
        )
        let data = await response.json()
        console.log(data)
        this.setState({
            Bills:data
        })
    }

    render() {
        return (
            <div>
                <Navbar />
                    <div className='History-Container'>
                    
                    <div className="row">
                        <div className="set-size charts-container">
                            <div className={this.state.progressBarPercentage}>
                                <span className="label">{this.state.userData.score}</span>
                                
                                <div className="pie">
                                    <div className="left-side half-circle"></div>
                                    <div className="right-side half-circle"></div>
                                </div>
                            </div>

                        </div>
                        <div className='Consumption-Container lead'>
                            <br /><br />
                            <div className='Card-title' style={{transform: "translateX(-15px)"}}>
                               {
                                   this.count === 30?'Yesterday\'s Bill is of $43.32':''
                               }
                            </div>
                        </div>
                    </div>
                            {
                                this.state.Bills.map(
                                    bill=>{
                                            this.count--;
                                       
                                            return(
                                            
                                            <div className='Card-title' key={this.count}>
                                              
                                                On {this.state.count === 0 ?'Yesterday\'s':this.count}th January 2020 Bill was of ₹{Math.ceil(bill*5/1000)}
                                            </div>
                                        );
                                    }
                                )
                            }
                            <br />
                            <div className='Card-title' style={{fontSize:'20px'}}>
                                Load More . . .
                            </div>
                            <br /><br /><br />
                    </div>
                <Footer />
            </div>
        )
    }
}

export default History
