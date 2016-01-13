
import React, { Component, PropTypes } from 'react'
import { verifyLogin } from '../actions/login';
import { store } from '../store';


export default class NavBar extends Component {

    proptypes: {
        login: PropTypes.object.isRequired
    }

    updateApiKey(e){
        console.log("Doing it...")
        store.dispatch(verifyLogin(e.target.value));
    }

    render() {
        var icon;
        if(this.props.login.valid){
            icon = <span className="glyphicon glyphicon-ok icon-success" aria-hidden="true"></span>;
        } else {
            icon = <span className="glyphicon glyphicon-remove icon-error" aria-hidden="true"></span>;
        }

        return (
            <nav className="navbar navbar-inverse navbar-fixed-top">
              <div className="container-fluid">
                <div className="navbar-header">
                  <a className="navbar-brand" href="#">Suppression Exporter</a>
                </div>
                <div id="navbar" className="navbar-collapse collapse">
                  <ul className="nav navbar-nav navbar-right">
                    <li><a href="/docs">Documentation</a></li>
                    <li><a href="http://www.mailgun.com">Mailgun</a></li>
                  </ul>
                  <form className="navbar-form navbar-right">
                    {(this.props.login.apiKey == "") ? "" : icon }
                        <input type="text"
                           className="form-control"
                           placeholder="ApiKey..."
                           onBlur={e => this.updateApiKey(e)}
                        //    value={this.state.login.apiKey}
                           />
                  </form>
                </div>
              </div>
            </nav>
        )
    }
}
