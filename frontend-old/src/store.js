import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";
import { toolListReducers, toolDetailReducers } from "./reducers/toolsReducers";
import {
  resultListReducers,
  resultDetailReducers,
} from "./reducers/resultsReducers";

const reducer = combineReducers({
  toolsList: toolListReducers,
  toolDetails: toolDetailReducers,
  resultsList: resultListReducers,
  resultDetails: resultDetailReducers,
});

const initialState = {};

const middleware = [thunk];

const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
