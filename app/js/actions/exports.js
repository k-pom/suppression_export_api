
export const EXPORTS_LOADED = 'EXPORTS_LOADED';
import { store } from '../store';


export function listExports(apiKey, domain){
    return (dispatch) => {
        return new Promise(function(success, failure){
            $.ajax({
                url: "/domains/" + domain + '/exports',
                headers: { "X-Auth-Token": apiKey },
                success: success
            });
      }).then(function(response){
          console.log('refreshing exports')
          dispatch({type: EXPORTS_LOADED, data: {exports: response.exports, domain: domain}});
      });
    };

}

export function deleteExport(apiKey, ex){
    return (dispatch) => {
        return new Promise(function(success, failure){
            $.ajax({
                method: 'delete',
                url: '/exports/' + ex.id,
                headers: { "X-Auth-Token": apiKey },
                success: success
            });
      }).then(function(response){

          store.dispatch(listExports(apiKey, ex.domain));
      });
    };
}

export function createExport(apiKey, domain, type){
    return (dispatch) => {
        return new Promise(function(success, failure){
            $.ajax({
                method: 'post',
                url: '/domains/' + domain + '/exports',
                headers: { "X-Auth-Token": apiKey },
                data: JSON.stringify({"type": type}),
                success: success
            });
      }).then(function(response){
          store.dispatch(listExports(apiKey, domain));
      });
    };
}
