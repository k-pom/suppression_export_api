
import { LOGGED_IN } from '../actions/login';


export const initialState = {
    valid: false,
    apiKey: ""
};


export default function store(state=initialState, action) {
    switch (action.type) {
        case LOGGED_IN:
            return Object.assign({}, state, action.data);
        default:
            return state
    }
};
