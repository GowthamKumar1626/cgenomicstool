import axios from "axios";
import {
  TOOL_LIST_REQUEST,
  TOOL_LIST_SUCCESS,
  TOOL_LIST_FAIL,
  TOOL_DETAILS_REQUEST,
  TOOL_DETAILS_SUCCESS,
  TOOL_DETAILS_FAIL,
} from "../constants/toolsConstans";

export const listTools = () => async (dispatch) => {
  try {
    dispatch({
      type: TOOL_LIST_REQUEST,
    });
    const { data } = await axios.get("/api/tools/");
    dispatch({
      type: TOOL_LIST_SUCCESS,
      payload: data,
    });
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

export const listToolDetails = (id) => async (dispatch) => {
  try {
    dispatch({
      type: TOOL_DETAILS_REQUEST,
    });
    const { data } = await axios.get(`/api/tools/${id}`);
    dispatch({
      type: TOOL_DETAILS_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: TOOL_DETAILS_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.message
          : error.message,
    });
  }
};
