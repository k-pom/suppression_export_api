
import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { store } from '../store';
import { listExports } from '../actions/exports';



class DomainRow extends Component {

    proptypes: {
        domain: PropType.object.isRequired,
        login: PropType.object.isRequired
    }

    listExports(e, apiKey, domain){
        store.dispatch(listExports(apiKey, domain));

    }

    render(){
        return (<div className='domainRow'>
                    <a href="#" onClick={e => this.listExports(e, this.props.login.api_key, this.props.domain.name)}>
                        {this.props.domain.name}
                    </a>
                </div>)
    }
}


@connect((store) => ({domains: store.domains, login: store.login }))
export default class Domains extends Component {

    proptypes: {
        domains: PropTypes.object.isRequired
    }

    render() {
        if(this.props.login.valid){
            var rows = [];
            var login = this.props.login
            this.props.domains.domainList.forEach(function(domain) {
                rows.push(<DomainRow key={domain.name} login={login} domain={domain} />);
            });
        }
        return (
            <div>
                <h4>Domains</h4>
                <hr />
                {rows}
            </div>
        );
    }
}
