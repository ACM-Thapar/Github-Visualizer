import React from 'react'
import { AppContent, AppSidebar, AppFooter, AppHeader } from '../components/index'

const DefaultLayout = ({data}) => {
  console.log(data)
  return (
    <div>
      <AppSidebar data={data}/>
      <div className="wrapper d-flex flex-column min-vh-100 bg-light">
        <AppHeader data={data}/>
        <div className="body flex-grow-1 px-3">
          <AppContent data={data}/>
        </div>
        <AppFooter />
      </div>
    </div>
  )
}

export default DefaultLayout
