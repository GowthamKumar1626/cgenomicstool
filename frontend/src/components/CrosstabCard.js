import React from "react";
import { Row, Col, Form, Button, Card } from "react-bootstrap";

function CrosstabCard() {
  return (
    <Card>
      <Card.Header as="h5">Inputs</Card.Header>
      <Card.Body>
        <Form.Group>
          <Form.Group>
            <Row>
              <Col>
                <Form.Label>Dataset: </Form.Label>
              </Col>
              <Col>
                <Form.File id="dataset-csv" />
              </Col>
            </Row>

            <Row className="my-2">
              <Col>
                <Form.Label>Phylogenetic File: </Form.Label>
              </Col>
              <Col>
                <Form.File id="phylo-newick" />
              </Col>
            </Row>

            <Row className="my-2">
              <Col>
                <Form.Label>Column name containing Genomes: </Form.Label>
                <Form.Control
                  size="sm"
                  type="text"
                  placeholder="Eg: Genome Name"
                />
                <Form.Label>Column name containing Gene: </Form.Label>
                <Form.Control size="sm" type="text" placeholder="Eg: Gene" />
              </Col>
              <Col>
                <Form.Label>Dataset Format: </Form.Label>
                <Form.Control size="sm" type="text" placeholder="Eg: CGE" />
              </Col>
            </Row>
          </Form.Group>
          <Button variant="primary" type="submit" className="px-1 my-1">
            Submit
          </Button>
        </Form.Group>
      </Card.Body>
    </Card>
  );
}

export default CrosstabCard;
