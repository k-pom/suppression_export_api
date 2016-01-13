
import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import NavBar from './header'
import Domains from './domains'
import { store } from '../store';


@connect((store) => ({router: store.router, login: store.login }))
export default class Application extends Component {

    proptypes: {
        router: PropTypes.object.isRequired,
        login: PropTypes.object.isRequired
    }

    render() {
        return (<div>
                    <NavBar login={this.props.login} />
                    <div className='container'>
                        <Domains domains={store.domains}/>
                        <h1>initialheader</h1>
                    </div>
                </div>);
    }
}
