import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import CrosstabCard from "../components/CrosstabCard";

import { listToolDetails } from "../actions/toolsActions";

function renderSwitch(tool) {
  switch (tool) {
    case "Crosstab":
      return <CrosstabCard />;
    case "Gene Organisation":
      return <Message variant="warning">{`Coming Soon .... `}</Message>;
    default:
      return (
        <Message variant="danger">{`Tools is not in our database .... `}</Message>
      );
  }
}

function ToolDetailScreen({ match }) {
  const dispatch = useDispatch();
  const toolDetails = useSelector((state) => state.toolDetails);
  const { loading, error, tool } = toolDetails;
  useEffect(() => {
    dispatch(listToolDetails(match.params.id));
  }, [dispatch, match]);

  return (
    <div>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <div>
          <h2>{tool.name}</h2>
          {renderSwitch(tool.name)}
        </div>
      )}
      {/* {tool.name === "Crosstab" ? (
        <CrosstabCard />
      ) : (
        <Message variant="warning">{`Coming Soon .... `}</Message>
      )} */}
      {}
    </div>
  );
}

export default ToolDetailScreen;
