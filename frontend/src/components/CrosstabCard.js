import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Row, Col, Form, Button, Card } from "react-bootstrap";
import { Link } from "react-router-dom";
import Loader from "../components/Loader";
import Message from "../components/Message";

function CrosstabCard() {
  const [genome_column_name, setGenomeColumnName] = useState("");
  const [gene_column_name, setGeneColumnName] = useState("");
  const [chop_genome_name_at, setChopGenomeNameAt] = useState("");
  const [data_format, setDataFormat] = useState("");
  const [dataset, setDataset] = useState("");
  const [phylo_path, setPhyloPath] = useState("");

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
          <Form.Group controlId="genome_column_name" className="mb-3">
            <Row className="my-1">
              <Col>
                <Form.Label>Genome column name: </Form.Label>
              </Col>
              <Col>
                <Form.Control
                  required
                  type="text"
                  name="genome_column_name"
                  value={genome_column_name}
                  onChange={(e) => setGenomeColumnName(e.target.value)}
                />
              </Col>
            </Row>
          </Form.Group>
          <Form.Group controlId="gene_column_name" className="mb-3">
            <Row className="my-1">
              <Col>
                <Form.Label>Gene column name: </Form.Label>
              </Col>
              <Col>
                <Form.Control
                  required
                  type="text"
                  name="gene_column_name"
                  value={gene_column_name}
                  onChange={(e) => setGeneColumnName(e.target.value)}
                />
              </Col>
            </Row>
          </Form.Group>
          <Form.Group controlId="chop_genome_name_at" className="mb-3">
            <Row className="my-1">
              <Col>
                <Form.Label>Chop genome name: </Form.Label>
              </Col>
              <Col>
                <Form.Control
                  type="text"
                  name="chop_genome_name_at"
                  value={chop_genome_name_at}
                  onChange={(e) => setChopGenomeNameAt(e.target.value)}
                />
              </Col>
            </Row>
          </Form.Group>
          <Row className="my-1">
            <Col>
              <Form.Label>Data fromat: </Form.Label>
            </Col>
            <Col>
              <Form.Control
                type="text"
                name="data_format"
                value={data_format}
                onChange={(e) => setDataFormat(e.target.value)}
              />
            </Col>

            {/* <Col>
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
            </Col> */}
          </Row>
          <Row className="my-3">
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
        </Card.Body>
      </Card>
    </div>
  );
}

export default CrosstabCard;
