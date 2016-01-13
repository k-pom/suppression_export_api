
import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import NavBar from './header'


@connect((store) => ({router: store.router, login: store.login }))
export default class Application extends Component {

    proptypes: {
        router: PropTypes.object.isRequired
    }

    render() {
        return (<div>
                    <NavBar login={this.props.login} />
                    <h1>initialheader-{this.props.router.path}</h1>
                </div>);
    }
}
