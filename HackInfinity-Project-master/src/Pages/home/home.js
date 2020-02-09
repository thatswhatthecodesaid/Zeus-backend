import React, { Component } from 'react'
import Navbar from '../../Components/Navbar/Navbar'
import './home.css'
import { Link } from 'react-router-dom'
import Footer from '../../Components/Footer/Footer'
import Host from '../../myIp';
class home extends Component {
    constructor(props) {
        console.log(Host.host)
        super(props)

     
    



        let userdata = localStorage.getItem('userdata');
        let User = JSON.parse(userdata);

        this.progressStatus = [0,30,45,60,75,90,95,100];
        // Status - 30, 45, 60,75,90,95
        this.classOfProgessStatus = "pie-wrapper progress-"+this.progressStatus[7];
          
       
        this.state = {
            LeaderboardData:[],
            bio:'',
            Rooms:[],
            User:{},
            progressBarPercentage:this.classOfProgessStatus,
            userData:User
        }


    }
 async componentDidMount(){
    this.getLeaderboardData()

    let rooms_response = await fetch("http://"+Host.host+":8000/popu/rooms/");
    let rooms_json = await rooms_response.json();
    this.setState({
        Rooms:rooms_json
    });

    let User_response = await fetch("http://"+Host.host+":8000/api/usview/");
    let User = await User_response.json();

    this.setState({
        User:User
    })
    console.log(this.state)
   localStorage.setItem("userdata",JSON.stringify(User));
 }
    getLeaderboardData = async (index = 1)=>{
        
        console.log(
            "Before Starting"
        )
        let response = await fetch(
            "http://"+Host.host+":8000/popu/rooms/",
            {type:"cors","Access-Control-Allow-Origin":"*"}
        )
        let data = await response.json();

            data = {
                "female" : [
                  "Saanvi",
                  "Anya",
                  "Aadhya",
                  "Aaradhya",
                  "Ananya",
                  "Pari",
                  "Anika",
                  "Navya",
                  "Angel",
                  "Diya",
                  "Myra",
                  "Sara",
                  "Iraa",
                  "Ahana",
                  "Anvi",
                  "Prisha",
                  "Riya",
                  "Aarohi",
                  "Anaya",
                  "Akshara",
                  "Eva",
                  "Shanaya",
                  "Kyra",
                  "Siya"
                ],
                "male" : [
                  "Aarav",
                  "Vihaan",
                  "Vivaan",
                  "Ananya",
                  "Diya",
                  "Advik",
                  "Kabir",
                  "Anaya",
                  "Aarav",
                  "Vivaan",
                  "Aditya",
                  "Vivaan",
                  "Vihaan",
                  "Arjun",
                  "Vivaan",
                  "Reyansh",
                  "Mohammed",
                  "Sai",
                  "Arnav",
                  "Aayan",
                  "Krishna",
                  "Ishaan",
                  "Shaurya",
                  "Atharva",
                  "Advik",
                  "Pranav",
                  "Advaith",
                  "Aaryan",
                  "Dhruv",
                  "Kabir",
                  "Ritvik",
                  "Aarush",
                  "Kian",
                  "Darsh",
                  "Veer"
                ],
                "surnames" : [
                  "Bedi",
                  "Gandhi",
                  "Parekh",
                  "Kohli",
                  "Ahluwalia",
                  "Chandra",
                  "Jha",
                  "Khanna",
                  "Bajwa",
                  "Chawla",
                  "Lal",
                  "Anand",
                  "Gill",
                  "Chakrabarti",
                  "Dubey",
                  "Kapoor",
                  "Khurana",
                  "Modi",
                  "Kulkarni",
                  "Khatri",
                  "Kaur",
                  "Dhillon",
                  "Kumar",
                  "Gupta",
                  "Naidu",
                  "Das",
                  "Jain",
                  "Chowdhury",
                  "Dalal",
                  "Thakur",
                  "Gokhale",
                  "Apte",
                  "Sachdev",
                  "Mehta",
                  "Ganguly",
                  "Bhasin",
                  "Mannan",
                  "Ahuja",
                  "Singh",
                  "Bakshi",
                  "Basu",
                  "Ray",
                  "Mani",
                  "Datta",
                  "Balakrishna",
                  "Biswas",
                  "Laghari",
                  "Malhotra",
                  "Dewan",
                  "Purohit"
                ]
              }
            console.log("After Requset",data)

        this.setState({
            LeaderboardData:data.male
        },()=>{
            console.log("Printed")
            this.render()
        });
        return data;
    }

    render() {
        return (
            <div>
                <Navbar />
                <div className='homecontainer'>

                    {/* ================================== Rooms ================================== */}
                        
                    <b className='lead'>Rooms Available</b>
                    <div className='rooms cards horizontal-scroll-wrapper'>{/* Users Rooms Appliances with Rooms Services */}
                        {
                            this.state.Rooms.map(
                                room=>{
                                    return(
                                       <Link key={room}  className='room card-item ripple' style={{textDecoration:"none"}} to={`/home/`+room}>
                                        <div key={room} className='' style={{background:"url('https://image.flaticon.com/icons/svg/2321/2321390.svg') center fit "}}> {/*  for Every Room Actually Map Method will Iterate Here */}
                                                <div  className='room-title lead'>{room}</div>
                            
                                        </div>
                                        </Link>
                                    );
                                }
                            )
                        }
                    </div>
                    
                        

               
                    {/* 1. What Friends Have Saved
                        2. Leaderboard
                        3. Add Some Other Resources to Optimise
                        4. Below an Another Drawer kind to Add People, [ Like Floating Button ]  */}
                    <div></div>
                            
                    {/* ================================== Rooms ================================== */}
                        <div className='leaderboard'>
                            <span className='lead'  style={{textAlign:"center",fontSize:"30px",padding:"30px",margin:"20px"}}>Leaderboard</span>
                            {
                                this.state.LeaderboardData.map(user=>{
                                    return(
                                    <div className='leaderboard-item ripple' key={user}>{user} : {` Zeus Score : `+user.length * 100}</div>
                                    );
                                })
                            }
                        </div>
                    {/* 1. What Friends Have Saved
                        2. Leaderboard
                        3. Add Some Other Resources to Optimise
                        4. Below an Another Drawer kind to Add People, [ Like Floating Button ]  */}
                   
                </div>
                
                <Footer />
                
                
            </div>
        );
    }
}

export default home

