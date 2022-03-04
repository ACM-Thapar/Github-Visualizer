import React, { Fragment } from 'react'
import { Grid } from 'react-loader-spinner'

const Loader = () => {
  return (
      <Fragment>
    <Grid ariaLabel="loading-indicator" />
    </Fragment>
  )
}

export default Loader