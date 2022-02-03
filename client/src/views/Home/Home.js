import React from 'react'
import * as styles from './Home.styles.js'
import { CForm, CFormLabel, CFormInput, CFormText, CContainer, CRow, CCol } from '@coreui/react'
import '@coreui/coreui/dist/css/coreui.min.css'

function Home() {
  return (
    <CContainer fluid>
      <CRow className="align-items-start">
        <CCol></CCol>
        <CCol className="bg-light">
          <h1>Github Visualizer - ACM</h1>
          <h4>Someones keeping an eye on you</h4>
        </CCol>
        <CCol></CCol>
      </CRow>
      <CRow className="align-items-center">
        <CCol></CCol>
        <CCol className="bg-light">
          <CForm>
            <div className="mb-3">
              <CFormLabel htmlFor="inputPassword5">Password</CFormLabel>
              <CFormInput
                type="password"
                id="inputPassword5"
                aria-describedby="passwordHelpBlock"
              />
              <CFormText id="passwordHelpBlock">
                Your password must be 8-20 characters long, contain letters and numbers, and must
                not contain spaces, special characters, or emoji.
              </CFormText>
            </div>
          </CForm>
        </CCol>
        <CCol></CCol>
      </CRow>
      <CRow className="align-items-end">
        <CCol></CCol>
        <CCol className="bg-light">One of three columns</CCol>
        <CCol></CCol>
      </CRow>
    </CContainer>
  )
}

export default Home
