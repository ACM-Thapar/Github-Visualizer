import React from 'react'
import './Home.css'
import welcome from '../../assets/images/welcome.svg'

function Home() {
  return (
    <>
      <div className="wrapper">
        <div className="home">
          <div className="text">
            <div className="content">
              <h2 className="text_shadows">Github</h2>
              {/* <h2 className="text_shadows">- </h2> */}
              <h2 className="text_shadows">Visualizer</h2>
            </div>
            <div className="webflow-style-input">
              <input className="" type="email" placeholder="Enter your Github Username"></input>
              <button type="submit">
                <i className="icon ion-android-arrow-forward"></i>
              </button>
            </div>
          </div>
          <div className="img">
            <img src={welcome} alt="" />
          </div>
        </div>
        <div className="footer">
          Made with ❤️ by <a href="https://github.com/ACM-Thapar">{'   '}@ACM-Thapar</a>
        </div>
      </div>
    </>
  )
}

export default Home
