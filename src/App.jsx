import Greeting from "./components/Greeting"
import StyleCard from "./components/StyleCard"
import UserStatus from "./components/UserStatus"
import Weather from "./components/weather"

const App = () => {
  return (
    <div>
      <Weather/>
      <UserStatus loggedIn = {true} isAdmin = {false}/>
      <Greeting timeOfDay = "morning"/>
      <StyleCard/>
    </div>
  )
}

export default App  