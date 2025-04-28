const UserStatus = (props) => {
  if (props.loggedIn && props.isAdmin){
    return <h1>welcome admin</h1>
  }
  else{
    return <h1>welcome user</h1>
  }
}

export default UserStatus