
export const LOGGED_IN = 'LOGGED_IN';
export const DOMAINS_LOADED = 'DOMAINS_LOADED';
import { store } from '../store';

export function verifyLogin(apiKey){
    return (dispatch) => {
        return new Promise(function(success, failure){
            $.get("/users/" + apiKey, success)
      }).then(function(response){

          dispatch({type: LOGGED_IN, data: response});  // TODO: On false login, fail, not success

            if(response.valid){

                $.ajax({
                    url: "/domains",
                    headers: { "X-Auth-Token": apiKey }
                }).then(function(response){
                    console.log("Firing event")
                    dispatch({type: DOMAINS_LOADED, data: response});
                });
            }
      });
    };

}
