
import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import NavBar from './header'


@connect((store) => ({router: store.router }))
export default class Application extends Component {

  proptypes: {
    router: PropTypes.object.isRequired
  }

  render() {
    console.log(this.props);
    return (<div>
              <NavBar />
              <h1>adsfasdf{this.props.router.path}</h1>
            </div>);
  }
}
