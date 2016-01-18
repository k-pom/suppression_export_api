
import { Router } from 'director';
import { setPath } from './actions/router';
import { store } from './store';

export const router = new Router();

router.on("?((\w|.)*)", function (path) {
  store.dispatch(setPath(path));
});
