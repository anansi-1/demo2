const Weather = () => {
  let temprature = 10 
        if(temprature < 15){
            return <h2>it is cold out side</h2>;
        }
        else if(temprature > 15 && temprature <25){
            return <h2> its nice outside</h2>;}
        else if (temprature > 25){
            return(<h2> it is hot ooutside</h2>)
        }
       
        
    
 
}

export default Weather