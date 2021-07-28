import axios from "axios";

import {
  TOOL_LIST_REQUEST,
  TOOL_LIST_SUCCESS,
  TOOL_LIST_FAIL,
} from "../constants/toolsConstants";

export const listTools = () => async (dispatch) => {
  try {
    dispatch({ type: TOOL_LIST_REQUEST });
    const { data } = await axios.get("/tools/");
    dispatch({ type: TOOL_LIST_SUCCESS, payload: data });
  } catch (error) {
    dispatch({
      type: TOOL_LIST_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};
