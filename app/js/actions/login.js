
export const LOGGED_IN = 'LOGGED_IN';

export function verifyLogin(apiKey){

    console.log("Verifying...");
    return (dispatch) => {
        return new Promise(function(success, failure){
            console.log("HERE");
            console.log(apiKey);
            success((apiKey=='valid'));
      }).then(function(response){
          dispatch({type: LOGGED_IN, data: response})
      });
    };

}
