import React from 'react'
import './Home.css'
import welcome from './images/welcome.svg'
import { useHistory } from 'react-router-dom'

function Home(props) {
  const history = useHistory()
  return (
    <>
      <div className="home_wrapper">
        <div className="home">
          <div className="text">
            <div className="content">
              <h2 className="text_shadows">Github</h2>
              {/* <h2 className="text_shadows">- </h2> */}
              <h2 className="text_shadows">Visualizer</h2>
            </div>
            <div className="webflow-style-input">
              <form
                onSubmit={(e) => {
                  e.preventDefault()
                  props.submitUsername(history)
                }}
              >
                <input
                  className="home_input"
                  type="text"
                  placeholder="Enter your Github Username"
                  onChange={(e) => {
                    props.setUsername(e.target.value)
                  }}
                ></input>
                <button type="submit">
                  <i className="icon ion-android-arrow-forward"></i>
                </button>
              </form>
            </div>
          </div>
          <div className="img">
            <img src={welcome} alt="" />
          </div>
        </div>
        <div className="footer">
          Made with ❤️ by <a href="https://github.com/ACM-Thapar">@ACM-Thapar</a>
        </div>
      </div>
    </>
  )
}

export default Home
