import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension";

import { toolsListReducer } from "./reducers/toolsListReducer";
import {
  resultsListReducer,
  resultDetailsReducer,
} from "./reducers/resultsListReducer";

import {
  userLoginReducer,
  userRegisterReducer,
  userDetailsReducer,
  userUpdateProfileReducer,
} from "./reducers/userReducer";

import {
  crosstabRequestReducer,
  crosstabInputsListReducer,
} from "./reducers/crosstabReducer";

const reducer = combineReducers({
  toolList: toolsListReducer,
  userLogin: userLoginReducer,
  userRegister: userRegisterReducer,
  userDetails: userDetailsReducer,
  userUpdateProfile: userUpdateProfileReducer,
  resultsList: resultsListReducer,
  resultDetails: resultDetailsReducer,
  crosstab: crosstabRequestReducer,
  crosstabInputsList: crosstabInputsListReducer,
});

const userInfoFromStorage = localStorage.getItem("userInfo")
  ? JSON.parse(localStorage.getItem("userInfo"))
  : null;

const crosstabInputsFromStorage = localStorage.getItem("crosstabInputs")
  ? JSON.parse(localStorage.getItem("crosstabInputs"))
  : null;

const initialState = {
  userLogin: { userInfo: userInfoFromStorage },
  crosstabInputsList: { crosstabInputs: crosstabInputsFromStorage },
};
const middleware = [thunk];
const store = createStore(
  reducer,
  initialState,
  composeWithDevTools(applyMiddleware(...middleware))
);

export default store;
