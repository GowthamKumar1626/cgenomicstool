import {
  TOOL_LIST_REQUEST,
  TOOL_LIST_SUCCESS,
  TOOL_LIST_FAIL,
} from "../constants/toolsConstants";

export const toolsListReducer = (state = { tools: [] }, action) => {
  switch (action.type) {
    case TOOL_LIST_REQUEST:
      return { loading: true, tools: [] };
    case TOOL_LIST_SUCCESS:
      return { loading: false, tools: action.payload };
    case TOOL_LIST_FAIL:
      return { loading: false, error: action.payload };
    default:
      return state;
  }
};

// export default toolsListReducer;
