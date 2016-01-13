
import React from 'react';
import { render } from 'react-dom';
import { Provider } from 'react-redux';

// app container and router
import Application from './components/application';
import { router } from './router';
import { store } from './store';
import { verifyLogin } from './actions/login';

// render the application
render(
  <Provider store={store}><Application /></Provider>,
  document.getElementById('container')
);

router.init('/');
store.dispatch(verifyLogin('jfdklas'));
