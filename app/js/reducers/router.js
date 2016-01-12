
import { SET_PATH } from '../actions/router';


export const initialState = {
  path: ''
};


export default function store(state=initialState, action) {
  console.log(action);

  switch (action.type) {
    case SET_PATH:
      return Object.assign({}, state, {path: action.path});
    default:
      return state
  }
};
