import React from "react";
import { Row, Col, Form, Button, Card } from "react-bootstrap";
import { Link } from "react-router-dom";

function CrosstabCard() {
  return (
    <div>
      <Row className="my-1">
        <Col>
          <h2>Crosstab</h2>
        </Col>
        <Col>
          <Link to="/" className="btn btn-light my-3">
            Go back
          </Link>
        </Col>
      </Row>
      <Card>
        <Card.Header as="h5">Inputs</Card.Header>
        <Card.Body>
          <Form.Group controlId="formFile" className="mb-3">
            <Row className="my-1">
              <Col>
                <Form.Label>Genome column name: </Form.Label>
              </Col>
              <Col>
                <Form.Control type="text" />
              </Col>
            </Row>
            <Row className="my-1">
              <Col>
                <Form.Label>Gene column name: </Form.Label>
              </Col>
              <Col>
                <Form.Control type="text" />
              </Col>
            </Row>
            <Row className="my-1">
              <Col>
                <Form.Label>Chop genome name: </Form.Label>
              </Col>
              <Col>
                <Form.Control type="text" />
              </Col>
            </Row>
            <Row className="my-1">
              <Col>
                <Form.Label>Data fromat: </Form.Label>
              </Col>
              <Col>
                <Form.Check
                  inline
                  label="CGE"
                  name="data-format"
                  type="radio"
                  id={`inline-radio-1`}
                />
                <Form.Check
                  inline
                  label="PATRIC"
                  name="data-format"
                  type="radio"
                  id={`inline-radio-1`}
                />
              </Col>
            </Row>
            <Row className="my-1">
              <Col>
                <Form.Label>Dataset: </Form.Label>
              </Col>
              <Col>
                <Form.Control type="file" />
              </Col>
            </Row>
            <Row className="my-1">
              <Col>
                <Form.Label>Phylogenetic File: </Form.Label>
              </Col>
              <Col>
                <Form.Control type="file" />
              </Col>
            </Row>
            <Button variant="primary" type="submit" className="px-1 my-2">
              Submit
            </Button>
          </Form.Group>
        </Card.Body>
      </Card>
    </div>
  );
}

export default CrosstabCard;
