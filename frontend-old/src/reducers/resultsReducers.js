import {
  RESULT_LIST_REQUEST,
  RESULT_LIST_SUCCESS,
  RESULT_LIST_FAIL,
  RESULT_DETAILS_REQUEST,
  RESULT_DETAILS_SUCCESS,
  RESULT_DETAILS_FAIL,
  DELETE_RESULT,
  DELETE_REQUEST_FAIL,
} from "../constants/resultsConstants";

export const resultListReducers = (
  state = {
    results: [],
  },
  action
) => {
  switch (action.type) {
    case RESULT_LIST_REQUEST:
      return {
        loading: true,
        results: [],
      };
    case RESULT_LIST_SUCCESS:
      return {
        loading: false,
        results: action.payload,
      };
    case RESULT_LIST_FAIL:
      return {
        loading: false,
        error: action.payload,
      };
    case DELETE_RESULT:
      return {
        loading: false,
        results: state.results.filter(
          (result) => result.job_id !== action.payload
        ),
      };
    case DELETE_REQUEST_FAIL:
      return {
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};

export const resultDetailReducers = (
  state = {
    result: {},
  },
  action
) => {
  switch (action.type) {
    case RESULT_DETAILS_REQUEST:
      return {
        loading: true,
        ...state,
      };
    case RESULT_DETAILS_SUCCESS:
      return {
        loading: false,
        result: action.payload,
      };
    case RESULT_DETAILS_FAIL:
      return {
        loading: false,
        error: action.payload,
      };
    default:
      return state;
  }
};
