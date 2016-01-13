
import React, { Component, PropTypes } from 'react'


export default class LoginModal extends Component {

    proptypes: {
        apiKey: PropTypes.string.isOptional
    }

    render() {
        if(this.props.apiKey){
          return null;
        }
        return (<h1>You need login</h1>);
    }
}
