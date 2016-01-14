
import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'



class DomainRow extends Component {

    proptypes: {
        domain: PropType.object.isRequired
    }

    render(){
        return (<div className='domainRow'>
                    <a href="#">{this.props.domain.name}</a>
                </div>)
    }
}


@connect((store) => ({domains: store.domains, login: store.login }))
export default class Domains extends Component {

    proptypes: {
        domains: PropTypes.object.isRequired
    }

    render() {
        console.log("PROPS", this.props);


        var rows = [];
        this.props.domains.domainList.forEach(function(domain) {
            rows.push(<DomainRow key={domain.name} domain={domain} />);
        });


        return (
            <div>
                <h4>Domains</h4>
                <hr />
                {rows}
            </div>
        );
    }
}
