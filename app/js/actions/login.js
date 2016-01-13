
export const LOGGED_IN = 'LOGGED_IN';

export function verifyLogin(apiKey){

    console.log("Verifying ", apiKey);
    return (dispatch) => {
        return new Promise(function(success, failure){
            success({
                apiKey: apiKey,
                valid: (apiKey=='valid')
            });
      }).then(function(response){
          dispatch({type: LOGGED_IN, data: response})
      });
    };

}
