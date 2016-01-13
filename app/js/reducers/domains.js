loadDomains
import { DOMAINS_LOADED } from '../actions/domains';


export const initialState = {
    domains: [],
};


export default function store(state=initialState, action) {
    switch (action.type) {
        case DOMAINS_LOADED:
            console.log(action)
            return Object.assign({}, state, action.data);
        default:
            return state
    }
};
