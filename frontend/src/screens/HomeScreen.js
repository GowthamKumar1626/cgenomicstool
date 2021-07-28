import React, { useState, useEffect } from "react";
import { Row, Col } from "react-bootstrap";
import axios from "axios";

import ToolOverview from "../components/ToolOverview";

function HomeScreen() {
  const [tools, setTools] = useState([]);
  useEffect(() => {
    async function fetchToolsOverview() {
      const { data } = await axios.get("/tools/");
      setTools(data);
    }
    fetchToolsOverview();
  }, []);
  return (
    <div>
      <h1>Tools</h1>
      <Row>
        {tools.map((tool) => (
          <Col key={tool.name} sm={12} md={6} lg={4} xl={3}>
            <ToolOverview tool={tool} />
          </Col>
        ))}
      </Row>
    </div>
  );
}

export default HomeScreen;
