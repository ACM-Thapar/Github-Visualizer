import { createStore, applyMiddleware, combineReducers } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';

const initialState = {
  sidebarShow: true,
}

const middleware = [thunk];

const changeState = (state = initialState, { type, ...rest }) => {
  switch (type) {
    case 'set':
      return { ...state, ...rest }
    default:
      return state
  }
}

const rootReducer = () =>{
  combineReducers()
}

const store = createStore(changeState, initialState, composeWithDevTools(applyMiddleware(...middleware)))
export default store


// import rootReducer from './reducers';


// const store = createStore(rootReducer, initialState, composeWithDevTools(applyMiddleware(...middleware)));

// export default store;