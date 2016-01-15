
import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import NavBar from './header'
import Domains from './domains'
import Exports from './exports'
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
                    <div className='container '>
                        <div className='col-md-2'>
                            <Domains domains={store.domains}/>
                        </div>
                        <div className='col-md-10'>
                            <Exports />
                        </div>
                    </div>
                </div>);
    }
}
