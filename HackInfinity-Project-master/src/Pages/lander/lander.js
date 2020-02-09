import React, { Component } from 'react';
import Navbar from '../../Components/Navbar/Navbar';
import './lander.css'
import { Link } from 'react-router-dom';
class Lander extends Component{
    constructor(props){
        super(props)

        this.state = {
            name:"S"
        }
    }

    render(){
        return(
            <div className='Container'>
            <Navbar />
               <div className='heading'>
                Efficient Energy Consumption, Solutions
                <div className='actions'>
                    <Link to='/register'>
                    <button className='lead button'>
                        Start Services
                    </button></Link>
               </div>
            </div>

            <section>
                Energy Services
            </section>
            <footer>
                Contact Us
            </footer>
               </div>    
        );
    }
}

export default Lander;