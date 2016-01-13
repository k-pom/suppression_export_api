
import { LOGGED_IN } from '../actions/login';


export const initialState = {
    loggedIn: false
};


export default function store(state=initialState, action) {
    switch (action.type) {
        case LOGGED_IN:
            return Object.assign({}, state, {loggedIn: action.loggedIn});
        default:
            return state
    }
};
