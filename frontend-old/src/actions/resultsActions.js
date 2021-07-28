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

import axios from "axios";
import Cookies from "js-cookie";

export const listResults = () => async (dispatch) => {
  try {
    dispatch({
      type: RESULT_LIST_REQUEST,
    });
    const { data } = await axios.get("/api/results/");
    dispatch({
      type: RESULT_LIST_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: RESULT_LIST_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const deleteResult = (id) => async (dispatch) => {
  try {
    const csrftoken = Cookies.get("csrftoken");
    const config = {
      headers: {
        "Content-type": "application/json",
        "X-CSRFToken": csrftoken,
      },
    };
    const { data } = await axios.delete(`/api/results/${id}/delete/`, config);
    dispatch({
      type: DELETE_RESULT,
      payload: id,
    });
  } catch (error) {
    console.log(error);
  }
};

export const listResultDetails = (id) => async (dispatch) => {
  try {
    dispatch({
      type: RESULT_DETAILS_REQUEST,
    });
    const { data } = await axios.get(`/api/results/${id}`);
    dispatch({
      type: RESULT_DETAILS_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: RESULT_DETAILS_FAIL,
      payload:
        error.response && error.response.data.message
          ? error.response.data.detail
          : error.message,
    });
  }
};
