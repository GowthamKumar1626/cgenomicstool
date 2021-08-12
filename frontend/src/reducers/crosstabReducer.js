import {
  CROSSTAB_INPUTS_REQUEST,
  CROSSTAB_INPUTS_SUCCESS,
  CROSSTAB_INPUTS_FAIL,
  CROSSTAB_INPUT_SEND_REQUEST,
  CROSSTAB_INPUT_SEND_SUCCESS,
  CROSSTAB_INPUT_SEND_FAIL,
  CROSSTAB_IMAGE_REQUEST,
  CROSSTAB_IMAGE_SUCCESS,
  CROSSTAB_IMAGE_FAIL,
} from "../constants/crosstabConstants";

export const crosstabInputsListReducer = (state = {}, action) => {
  switch (action.type) {
    case CROSSTAB_INPUTS_REQUEST:
      return { loading: true };
    case CROSSTAB_INPUTS_SUCCESS:
      return { loading: false, crosstabInputsList: action.payload };
    case CROSSTAB_INPUTS_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};

export const crosstabRequestReducer = (state = {}, action) => {
  switch (action.type) {
    case CROSSTAB_INPUT_SEND_REQUEST:
      return { loading: true };
    case CROSSTAB_INPUT_SEND_SUCCESS:
      return { loading: false, crosstabResult: action.payload };
    case CROSSTAB_INPUT_SEND_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};

export const crosstabPlotReducer = (state = { crosstabImage: {} }, action) => {
  switch (action.type) {
    case CROSSTAB_IMAGE_REQUEST:
      return { loading: true, ...state };
    case CROSSTAB_IMAGE_SUCCESS:
      return { loading: false, crosstabImage: action.payload };
    case CROSSTAB_IMAGE_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};
