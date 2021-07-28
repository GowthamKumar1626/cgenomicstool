import React, { useEffect } from "react";
import { Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";

import ToolOverview from "../components/ToolOverview";
import { listTools } from "../actions/toolListActions";

function HomeScreen() {
  const dispatch = useDispatch();
  const toolList = useSelector((state) => state.toolList);
  const { error, loading, tools } = toolList;
  useEffect(() => {
    dispatch(listTools());
  }, [dispatch]);
  return (
    <div>
      <h1>Tools</h1>
      {loading ? (
        <h3>Loading ....</h3>
      ) : error ? (
        <h3>{error} </h3>
      ) : (
        <Row>
          {tools.map((tool) => (
            <Col key={tool.name} sm={12} md={6} lg={4} xl={3}>
              <ToolOverview tool={tool} />
            </Col>
          ))}
        </Row>
      )}
    </div>
  );
}

export default HomeScreen;
