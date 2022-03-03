import React, { Component, useEffect, useState } from 'react'
import { HashRouter, Redirect, Route, Switch } from 'react-router-dom'
import './scss/style.scss'
import Home from './views/Home/Home'
import axios from 'axios'

const loading = (
  <div className="pt-3 text-center">
    <div className="sk-spinner sk-spinner-pulse"></div>
  </div>
)

// Containers
const DefaultLayout = React.lazy(() => import('./layout/DefaultLayout'))

// Pages
const Login = React.lazy(() => import('./views/pages/login/Login'))
const Register = React.lazy(() => import('./views/pages/register/Register'))
const Page404 = React.lazy(() => import('./views/pages/page404/Page404'))
const Page500 = React.lazy(() => import('./views/pages/page500/Page500'))

const App = () => {
  const [username, setUsername] = useState(null)
  const [data, setData] = useState([])

  // useEffect(async () => {
  //   if (username !== null) {
  //     const res = await axios.get('https://github-visualiser-acm.herokuapp.com/Samikmalhotra/')
  //     console.log(res.data)
  //     setData(res.data)
  //   }
  // }, [])
  const submitUsername = async(history) => {
    
    try {
      const res = await axios.get(`https://github-visualiser-acm.herokuapp.com/${username}/`)
      setData(res.data)
      history.push('/dashboard')
    } catch (error) {
      console.error(error.message)
    }
  }
  console.log(username)
  console.log(data)
  if(data !== []){
    <Redirect to = '/dashboard'></Redirect>
  }

  return (
    <HashRouter>
      <React.Suspense fallback={loading}>
        <Switch>
          <Route
            exact
            path="/home"
            name="Home Page"
            render={() => <Home setUsername={setUsername} submitUsername={submitUsername}/>}
          />
          <Route exact path="/login" name="Login Page" render={(props) => <Login {...props} />} />
          <Route
            exact
            path="/register"
            name="Register Page"
            render={(props) => <Register {...props} />}
          />
          <Route exact path="/404" name="Page 404" render={(props) => <Page404 {...props} />} />
          <Route exact path="/500" name="Page 500" render={(props) => <Page500 {...props} />} />
          <Route
            path="/"
            name="Home"
            render={(props) => <DefaultLayout {...props} data={data} />}
          />
        </Switch>
      </React.Suspense>
    </HashRouter>
  )
}

export default App
