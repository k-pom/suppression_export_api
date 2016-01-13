
import { LOGGED_IN } from '../actions/login';


export const initialState = {
    valid: false,
    apiKey: ""
};


export default function store(state=initialState, action) {
    switch (action.type) {
        case LOGGED_IN:
            console.log("I care about login change")
            return Object.assign({}, state, action.data);
        default:
            return state
    }
};
