
export const DOMAINS_LOADED = 'DOMAINS_LOADED';

export function loadDomains(apiKey){

    console.log("Getting domains");
    return (dispatch) => {
        return new Promise(function(success, failure){
            $.get("/domains")
      }).then(function(response){
          console.log("Got domains");
          console.log(response);
          dispatch({type: DOMAINS_LOADED, data: response})
      });
    };

}
