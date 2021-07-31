import axios from "axios";

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

export const listResults = () => async (dispatch, getState) => {
  try {
    dispatch({ type: RESULT_LIST_REQUEST });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-type": "application/json",
        Authorization: `Bearer ${userInfo.token}`,
      },
    };

    const { data } = await axios.get("/results/", config);

    dispatch({ type: RESULT_LIST_SUCCESS, payload: data });
  } catch (error) {
    dispatch({
      type: RESULT_LIST_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const listResultDetails = (id) => async (dispatch, getState) => {
  try {
    dispatch({ type: RESULT_DETAILS_REQUEST });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-type": "application/json",
        Authorization: `Bearer ${userInfo.token}`,
      },
    };

    const { data } = await axios.get(`/results/${id}/`, config);

    dispatch({
      type: RESULT_DETAILS_SUCCESS,
      payload: data,
    });
  } catch (error) {
    dispatch({
      type: RESULT_DETAILS_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const deleteResult = (id) => async (dispatch, getState) => {
  try {
    dispatch({
      type: RESULT_DELETE_REQUEST,
    });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-type": "application/json",
        Authorization: `Bearer ${userInfo.token}`,
      },
    };

    // eslint-disable-next-line
    const { data } = await axios.delete(`/results/${id}/`, config);

    dispatch({
      type: RESULT_DELETE_SUCCESS,
    });
  } catch (error) {
    dispatch({
      type: RESULT_DELETE_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};
