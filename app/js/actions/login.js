
export const LOGGED_IN = 'LOGGED_IN';
import {loadDomains} from './domains';
import { store } from '../store';

export function verifyLogin(apiKey){

    return (dispatch) => {
        return new Promise(function(success, failure){
            $.get("/users/" + apiKey, success)
      }).then(function(response){
          store.dispatch(loadDomains(apiKey));
          dispatch({type: LOGGED_IN, data: response});  // TODO: On false login, fail, not success
      });
    };

}
