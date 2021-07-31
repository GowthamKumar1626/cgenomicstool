import React, { useState, useEffect } from "react";
import axios from "axios";

import NewCrosstab from "../components/NewCrosstab";

function renderSwitch(tool) {
  switch (tool) {
    case "Crosstab":
      return <NewCrosstab />;
    case "Gene Organisation":
      return <p>{`Coming Soon .... `}</p>;
    default:
      return <p>{`Tools is not in our database .... `}</p>;
  }
}

function ToolDetailScreen({ match }) {
  const [tool, setTool] = useState([]);
  useEffect(() => {
    async function fetchTool() {
      let str = match.params.id;
      const { data } = await axios.get(
        `/tools/${str.charAt(0).toUpperCase() + str.slice(1)}`
      );
      setTool(data);
    }
    fetchTool();
  }, [match]);

  return <div>{renderSwitch(tool.name)}</div>;
}

export default ToolDetailScreen;
