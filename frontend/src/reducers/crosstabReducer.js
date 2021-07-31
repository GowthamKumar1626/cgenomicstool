import {
  CROSSTAB_INPUT_SEND_REQUEST,
  CROSSTAB_INPUT_SEND_SUCCESS,
  CROSSTAB_INPUT_SEND_FAIL,
} from "../constants/crosstabConstants";

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
