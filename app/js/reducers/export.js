import { EXPORTS_LOADED } from '../actions/exports';

export const initialState = {
    exports: [],
    domain: false
};

export default function store(state=initialState, action) {
    switch (action.type) {
        case EXPORTS_LOADED:
            console.log(action.data)
            return Object.assign({}, state, {exports: action.data.exports, domain: action.data.domain});
        default:
            return state
    }
};
