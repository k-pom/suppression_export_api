
export const LOGGED_IN = 'LOGGED_IN';

export function verifyLogin(apiKey){

    return (dispatch) => {
        return new Promise(function(success, failure){
            $.get("/users/" + apiKey, success)
      }).then(function(response){
          dispatch({type: LOGGED_IN, data: response})
      });
    };

}
