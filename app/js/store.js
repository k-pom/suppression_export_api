
import { createStore, applyMiddleware, combineReducers } from 'redux';
import thunk from 'redux-thunk';

// stores
import routerReducer from './reducers/router';
import loginReducer from './reducers/login';
import domainReducer from './reducers/domains';

// wire up the application
const createStoreWithMiddleware = applyMiddleware(thunk)(createStore);

export const store = createStoreWithMiddleware(combineReducers({
  router: routerReducer,
  login: loginReducer,
  domains: domainReducer
}));
