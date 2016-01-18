
import React, { Component, PropTypes } from 'react'
import { connect } from 'react-redux'
import { store } from '../store';
import { deleteExport, createExport } from '../actions/exports';


class ExportRow extends Component {

    proptypes: {
        export: PropType.object.isRequired,
        login: PropType.object.isRequired
    }

    deleteExport(e, apiKey, ex){
        store.dispatch(deleteExport(apiKey, ex));
    }

    render(){
        var icon;
        if (this.props.export.type == 'bounces'){
            icon = <span className="glyphicon glyphicon-remove-circle" aria-hidden="true"></span>
        } else if (this.props.export.type == 'unsubscribes'){
            icon = <span className="glyphicon glyphicon-ban-circle" aria-hidden="true"></span>
        } else if (this.props.export.type == 'complaints'){
            icon = <span className="glyphicon glyphicon-trash" aria-hidden="true"></span>
        } else{
            icon = <span>{this.props.export.type}</span>
        }

        var downloadButton = <a className='btn btn-default' href={this.props.export.filename}>Download</a>


        return (<tr className='domainRow'>
                    <td>{icon}</td>
                    <td>{this.props.export.type}</td>
                    <td>{this.props.export.status}</td>
                    <td>{this.props.export.total}</td>
                    <td>{this.props.export.created_at}</td>
                    <td>{(this.props.export.status == "completed" && this.props.export.total > 0) ? downloadButton : "" }</td>
                    <td>
                        <span className='btn btn-danger' onClick={e => this.deleteExport(e, this.props.login.apiKey, this.props.export)}>
                            Delete
                        </span>
                    </td>
                </tr>)
    }
}


@connect((store) => ({exports: store.exports, login: store.login }))
export default class Exports extends Component {

    proptypes: {
        exports: PropTypes.object.isRequired
    }

    createExport(e, apiKey, domain, type){
        store.dispatch(createExport(apiKey, domain, type));
    }


    render() {
        if(!this.props.login.valid){
            return <p>Enter a valid api key above</p>
        } else if (!this.props.exports.domain){
            return <p>Choose a domain from the left</p>
        }

        var rows = [];
        var login = this.props.login;
        this.props.exports.exports.forEach(function(ex) {
            rows.push(<ExportRow key={ex.id} login={login} export={ex} />);
        });

        return (
            <div>
                <h4>{this.props.exports.domain}</h4>

                <div className="btn-group">
                    <button type="button" className="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Create Export <span className="caret"></span>
                    </button>
                    <ul className="dropdown-menu">
                        <li>
                            <a href="#" onClick={e => this.createExport(e, this.props.login.apiKey, this.props.exports.domain, 'bounces')}>
                                Bounce
                            </a>
                        </li>
                        <li>
                            <a href="#" onClick={e => this.createExport(e, this.props.login.apiKey, this.props.exports.domain, 'unsubscribes')}>
                                Unsubscribes
                            </a>
                        </li>
                        <li>
                            <a href="#" onClick={e => this.createExport(e, this.props.login.apiKey, this.props.exports.domain, 'complaints')}>
                                Complaints
                            </a>
                        </li>
                    </ul>
                </div>
                <table className='table'>
                    <thead>
                        <tr>
                            <th></th>
                            <th>Type</th>
                            <th>Status</th>
                            <th>Total</th>
                            <th>Created At</th>
                            <th></th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        {rows}
                    </tbody>
                </table>
            </div>
        );
    }
}
