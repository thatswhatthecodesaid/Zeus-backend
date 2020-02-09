import React, { Component } from 'react'
import './Footer.css'
import { Link } from 'react-router-dom'
class Footer extends Component{
    constructor(props){
        super(props)

        this.state = {

        }
    }

    render(){
        return(
            <div className='Footer_container'>
                
                <Link to='/home' className="Footer_item ripple"><i className="fa fa-home" aria-hidden="true"></i></Link>
                <Link to='/totalbill' className="Footer_item ripple"><i className="fa fa-flash" aria-hidden="true"></i></Link> {/* Energy Optimisation */}
                <Link to='/notification' className="Footer_item ripple"><i className="fa fa-bell" aria-hidden="true"></i></Link>
                <Link to='/profile' className="Footer_item ripple"><i className="fa fa-user" aria-hidden="true"></i></Link>
            </div>
        )
    }
}

export default Footer