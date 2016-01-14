
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
                    <div className='container '>
                        <div className='col-md-2'>
                            <Domains domains={store.domains}/>
                        </div>
                        <div className='col-md-10'>

                            <p>
                                {this.props.login.valid ? 'Select a domain from the left' : 'Enter your API key above'}
                            </p>
                        </div>
                    </div>
                </div>);
    }
}
