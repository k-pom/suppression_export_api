import { DOMAINS_LOADED } from '../actions/login';

export const initialState = {
    domainList: [],
};

export default function store(state=initialState, action) {
    switch (action.type) {
        case DOMAINS_LOADED:
            console.log(action.data)
            return Object.assign({}, state, {domainList: action.data.domains});
        default:
            return state
    }
};
