import {
  RESULT_LIST_REQUEST,
  RESULT_LIST_SUCCESS,
  RESULT_LIST_FAIL,
  RESULT_DETAILS_REQUEST,
  RESULT_DETAILS_SUCCESS,
  RESULT_DETAILS_FAIL,
  RESULT_DELETE_REQUEST,
  RESULT_DELETE_SUCCESS,
  RESULT_DELETE_FAIL,
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

export const resultDetailsReducer = (state = { result: {} }, action) => {
  switch (action.type) {
    case RESULT_DETAILS_REQUEST:
      return { loading: true, ...state };

    case RESULT_DETAILS_SUCCESS:
      return { loading: false, result: action.payload };

    case RESULT_DETAILS_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};

export const resultDeleteReducer = (state = {}, action) => {
  switch (action.type) {
    case RESULT_DELETE_REQUEST:
      return { loading: true };

    case RESULT_DELETE_SUCCESS:
      return { loading: false, success: true };

    case RESULT_DELETE_FAIL:
      return { loading: false, error: action.payload };

    default:
      return state;
  }
};
