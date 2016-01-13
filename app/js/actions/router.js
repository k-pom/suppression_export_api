
export const SET_PATH = 'SET_PATH';


export function setPath(path) {
  return (dispatch) => {
    dispatch({type: SET_PATH, path: path});
  };
}
