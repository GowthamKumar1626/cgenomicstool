import {
  RESULT_LIST_REQUEST,
  RESULT_LIST_SUCCESS,
  RESULT_LIST_FAIL,
} from "../constants/resultsConstants";

export const resultsListReducer = (state = { results: [] }, action) => {
  switch (action.type) {
    case RESULT_LIST_REQUEST:
      return { loading: true, results: [] };
    case RESULT_LIST_SUCCESS:
      return { loading: false, results: action.payload };
    case RESULT_LIST_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};