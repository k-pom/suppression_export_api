
import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'



@connect((store) => ({router: store.router}))
export default class NavBar extends Component {

  proptypes: {
    router: PropTypes.object.isRequired
  }

  render() {
    return (<h1>I am a header</h1>);
  }
}
