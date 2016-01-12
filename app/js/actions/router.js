
export const SET_PATH = 'SET_PATH';


export function setPath(path) {
  console.log(path);

  return (dispatch) => {
    dispatch({type: SET_PATH, path: path});
  };
}
