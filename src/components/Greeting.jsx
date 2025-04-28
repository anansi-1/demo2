const Greeting = (props) => {
  return props.timeOfDay === "morning"?(<h1>good morning</h1>):(<h1>good afternoon</h1>)
}

export default Greeting