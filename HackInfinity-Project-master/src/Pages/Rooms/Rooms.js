import React, { Component } from 'react';
import Navbar from '../../Components/Navbar/Navbar';
import './Rooms.css'
import Footer from '../../Components/Footer/Footer';
import Host from '../../myIp';

class Rooms extends Component{
    constructor(props){
        super(props)

        let {roomname} = this.props.match.params;
        this.state = {
            roomname:roomname,
            appliances:[],
            isappliances:false
        }

        this.appliances = [];

        this.routes = {
            'hall':1,
            'bedroom':5,
            'kitchen':3
        }

        console.log(this.state.roomname)
        this.ourRouteKey = this.routes[this.state.roomname];
    }

    async componentDidMount(){
        let response = await fetch("http://"+Host.host+":8000/popu/air/");
        let data = await response.json();
        
        data.map(app=>{
            if(app.fields.a_room == this.ourRouteKey){
               this.appliances.push(app.fields); 
            }

            
        })

        console.log(this.appliances)
        this.setState(
            {
                appliances:this.appliances,
                isappliances:true
            },
            ()=>{
                console.log("Fetched")
            }
        );


    }

     DeviceIO = async (event)=>{
        let device_name = event.target.getAttribute("value");
        let status = event.target.getAttribute("status");
        console.log(device_name,status)
        if(event.target.getAttribute("status") == "on"){

            event.target.setAttribute("class","appliance");
            event.target.setAttribute("status","off");

            
        }else{
            event.target.setAttribute("class","appliance appliance_active");
            event.target.setAttribute("status","on");
        }




        // Send API Request to Server from Here
        let valueOfDb = status == "off"?true:false;
        console.log(valueOfDb)
        let reponse = await fetch(
            "http://"+Host.host+":8000/iot/io/",
            {
                method:"POST",
                headers:
                {
                    'Content-Type':'application/x-www-form-urlencoded'
                },
                body:"appliance="+device_name+"&a_io="+valueOfDb
            }
        );

        let data = await reponse.json();

        console.log(data)
    }
    render(){
        return(
            <div className='container'>
                <Navbar />
                <div className='roomContainer'>
                    <div className='rooms-title ripple' style={{padding:'10px',textTransform:"uppercase"}}>
                        {this.state.roomname}
                    </div>
                    <div className='rooms'>
                        {
                            this.state.appliances.map(eachAppliance=>{
                                console.log(eachAppliance.a_io)
                                return(
                                <div onClick={this.DeviceIO} name="device" status="on" value={eachAppliance.a_name} key={eachAppliance.a_name} className={eachAppliance.a_io == true?'appliance  appliance_active':'appliance '}>
                                    
                                        {eachAppliance.a_name}
                                   
                                </div>
                                );
                            })
                        }
                    </div>
                </div>
                <Footer />
            </div>
        );
    }
}

export default Rooms