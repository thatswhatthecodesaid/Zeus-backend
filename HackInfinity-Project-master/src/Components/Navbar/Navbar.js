import React, { Component } from 'react'
import './Navbar.css';
import { Link } from 'react-router-dom';


class Navbar extends Component {
    constructor(props) {
        super(props)

        this.state = {
            isDrawer:false 
        }
    }
    openDrawer = ()=>{
        if(this.state.isDrawer){
            
        this.setState({isDrawer:false})
        }else{
            
        this.setState({isDrawer:true})
        }
    }
    render() {
        let ourdrawer;
        let drawericon;
        if(this.state.isDrawer){
            drawericon = <div><i className="fa fa-times" aria-hidden="true"></i></div>;
            ourdrawer = <div className='drawer-content'>
                <h1 style={{textAlign:'center'}}>
                    <div className='Navbar_Content_Header'>
                        <div className='Navbar_Content_Container'>
                            <div className='Navbar_Content_Item' >Home</div >
                            <div className='Navbar_Content_Item'>Charges </div >
                            <div className='Navbar_Content_Item'>Accounts</div >
                            <div className='Navbar_Content_Item'>Your Data Privacy</div >
                            <div className='Navbar_Content_Item'>Security Settings</div >
                            <div className='Navbar_Content_Item'> Log Out </div >
                        </div>
                    </div>
                </h1>
            </div>;
            console.log(drawericon)
        }else{
            drawericon=<div><i className="fa fa-reorder" aria-hidden="true"></i></div>;
            ourdrawer = '';
        }
        return (
            <div id='Navbar' className=''>
                <Link id='logo' to='/history'><div className='elem ripple'><i className="fa fa-calendar" aria-hidden="true"></i></div></Link>
                <Link to='/home'  id='title'><div className='elem ripple' style={{textDecoration:"none",color:"white"}}>Zeus</div></Link>
                <div id='drawer' className='elem' onClick={this.openDrawer} style={{background:ourdrawer === ''?'':'white',color:ourdrawer === ''?'':'black'}}>{drawericon}</div>
                {
                    ourdrawer
                }
            </div>
        )
    }
}

export default Navbar
