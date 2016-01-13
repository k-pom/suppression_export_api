
import React, { Component, PropTypes } from 'react'
// import { getDomain } from '../actions/domain';
import { store } from '../store';


export default class Domains extends Component {

    proptypes: {
        domains: PropTypes.object.isOptional
    }

    render() {
        console.log(this.props)
        return (
            <div>-<ul>{this.props.domains}</ul>-</div>
        )
    }
}
