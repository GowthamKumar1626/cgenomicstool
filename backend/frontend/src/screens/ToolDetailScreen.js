import React from "react";
import Crosstab from "../components/Crosstab";

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
      <div className="my-3"></div>
    </div>
  );
}

export default ToolDetailScreen;
