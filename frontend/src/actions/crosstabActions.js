import {
  CROSSTAB_INPUTS_REQUEST,
  CROSSTAB_INPUTS_SUCCESS,
  CROSSTAB_INPUTS_FAIL,
  CROSSTAB_INPUT_SEND_REQUEST,
  CROSSTAB_INPUT_SEND_SUCCESS,
  CROSSTAB_INPUT_SEND_FAIL,
} from "../constants/crosstabConstants";
import axios from "axios";

export const crosstabInputs = (filename) => async (dispatch, getState) => {
  try {
    dispatch({ type: CROSSTAB_INPUTS_REQUEST });

    const {
      userLogin: { userInfo },
    } = getState();

    const config = {
      headers: {
        "Content-type":
          "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        Authorization: `Bearer ${userInfo.token}`,
      },
    };
    let form_data = new FormData();
    form_data.append("dataset", filename);

    const { data } = await axios.post(
      "/crosstab/process-inputs/",
      form_data,
      config
    );

    dispatch({ type: CROSSTAB_INPUTS_SUCCESS, payload: data });
    localStorage.setItem("crosstabInputs", JSON.stringify(data));
  } catch (error) {
    dispatch({
      type: CROSSTAB_INPUTS_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

export const sendCrosstabRequest =
  (
    genome_column_name,
    gene_column_name,
    chop_genome_name_at,
    data_format,
    dataset,
    phylo_path
  ) =>
  async (dispatch, getState) => {
    try {
      dispatch({
        type: CROSSTAB_INPUT_SEND_REQUEST,
      });

      const {
        userLogin: { userInfo },
      } = getState();

      const config = {
        headers: {
          "Content-type":
            "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
          Authorization: `Bearer ${userInfo.token}`,
        },
      };

      let form_data = new FormData();
      form_data.append("genome_column_name", genome_column_name);
      form_data.append("gene_column_name", gene_column_name);
      form_data.append("chop_genome_name_at", chop_genome_name_at);
      form_data.append("data_format", data_format);
      form_data.append("dataset", dataset);
      form_data.append("phylo_path", phylo_path);

      const { data } = await axios.post("/crosstab/", form_data, config);

      // {
      //   genome_column_name: genome_column_name,
      //   gene_column_name: gene_column_name,
      //   chop_genome_name_at: chop_genome_name_at,
      //   data_format: data_format,
      //   dataset: dataset,
      //   phylo_path: phylo_path,
      // }
      dispatch({
        type: CROSSTAB_INPUT_SEND_SUCCESS,
        payload: data,
      });

      //   localStorage.setItem("crosstabResult", JSON.stringify(data));
    } catch (error) {
      dispatch({
        type: CROSSTAB_INPUT_SEND_FAIL,
        payload:
          error.response && error.response.data.detail
            ? error.response.data.detail
            : error.message,
      });
    }
  };
