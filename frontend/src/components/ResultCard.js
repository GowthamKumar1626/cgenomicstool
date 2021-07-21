import React from "react";
import { Row, Col, Card } from "react-bootstrap";

function renderToolUsed(id) {
  switch (id) {
    case 1:
      return "Crosstab";
    case 2:
      return "Gene Organisation";
    default:
      return "Tool is not in our database";
  }
}

function ResultCard({ result }) {
  return (
    <div>
      <Card>
        <Card.Header as="h5">Overview</Card.Header>
        <Card.Body>
          <Row>
            <Col>
              <p>Title: </p>
            </Col>
            <Col>
              <p>Demo Result</p>
            </Col>
          </Row>
          <Row>
            <Col>
              <p>Result ID: </p>
            </Col>
            <Col>
              <p>{result.job_id}</p>
            </Col>
          </Row>
          <Row>
            <Col>
              <p>Tool used: </p>
            </Col>
            <Col>
              <p>{renderToolUsed(result.tool_used)}</p>
            </Col>
          </Row>
          <Row>
            <Col>
              <p>Created at: </p>
            </Col>
            <Col>
              <p>{result.created_at}</p>
            </Col>
          </Row>
          <Row>
            <Col>
              <p>Expires at: </p>
            </Col>
            <Col>
              <p>{result.expires_at}</p>
            </Col>
          </Row>
          <Row>
            <Col>
              <p>Status: </p>
            </Col>
            <Col>
              <p>Success</p>
            </Col>
          </Row>
          <Row>
            <Col>
              <p>Crosstab Data: </p>
            </Col>
            <Col>
              <p>{result.result_data}</p>
            </Col>
          </Row>
        </Card.Body>
      </Card>
    </div>
  );
}

export default ResultCard;
