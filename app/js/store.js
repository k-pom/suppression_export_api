
import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

// stores
import routerReducer from './reducers/router';

// wire up the application
const createStoreWithMiddleware = applyMiddleware(thunk)(createStore);

export const store = createStoreWithMiddleware(combineReducers({
  router: routerReducer
}));
