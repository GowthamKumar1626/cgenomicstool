import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Row, Col } from "react-bootstrap";
import Tool from "../components/Tool";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { listTools } from "../actions/toolsActions";

// import { products } from "../products";

function ToolScreen() {
  const dispatch = useDispatch();
  const toolsList = useSelector((state) => state.toolsList);
  const { error, loading, tools } = toolsList;

  useEffect(() => {
    dispatch(listTools());
  }, [dispatch]);

  return (
    <div>
      <h1>Tools offered</h1>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : (
        <Row>
          {tools.map((tool) => (
            <Col key={tool._id} sm={12} md={6} lg={4} xl={3}>
              <Tool tool={tool} />
            </Col>
          ))}
        </Row>
      )}
    </div>
  );
}

export default ToolScreen;
