import React from "react";
import Crosstab from "../components/Crosstab";
import Message from "../components/Message";

function renderSwitch(tool) {
  switch (tool) {
    case "crosstab":
      return <Crosstab />;
    case "gene Organisation":
      return <p>{`Coming Soon .... `}</p>;
    default:
      return <p>{`Tools is not in our database .... `}</p>;
  }
}

function ToolDetailScreen({ match }) {
  return (
    <div>
      {renderSwitch(match.params.id)}
      <div className="my-3">
        <Message variant="warning">Please login to access tool</Message>
      </div>
    </div>
  );
}

export default ToolDetailScreen;
