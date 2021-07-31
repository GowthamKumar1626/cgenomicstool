import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Row, Col, Form, Card, Button } from "react-bootstrap";
import { Link } from "react-router-dom";
import Loader from "../components/Loader";
import Message from "../components/Message";
import ResultsCard from "../components/ResultsCard";
import {
  crosstabInputs,
  sendCrosstabRequest,
} from "../actions/crosstabActions";

function CrosstabCard({ location, history }) {
  const [dataset, setDataset] = useState("");
  const [genomeName, setGenomeName] = useState("");
  const [geneName, setGeneName] = useState("");
  const [dataFormat, setDataFormat] = useState("");
  const [phyloPath, setPhyloPath] = useState("");

  // sendCrosstabRequest

  const dispatch = useDispatch();

  const crosstab = useSelector((state) => state.crosstabInputsList);
  const { errorDataset, loadingDataset, crosstabInputsList } = crosstab;

  const crosstabResults = useSelector((state) => state.crosstab);
  const { error, loading, crosstabResult } = crosstabResults;

  const submitHandler = (event) => {
    event.preventDefault();
    setDataset(event.target.files[0]);
    dispatch(crosstabInputs(event.target.files[0]));
  };

  const submitColumnDetailsHandler = (event) => {
    event.preventDefault();
    console.log(genomeName, geneName, dataFormat, phyloPath, dataset);
    dispatch(
      sendCrosstabRequest(
        genomeName,
        geneName,
        "strain",
        dataFormat,
        dataset,
        phyloPath
      )
    );
  };

  return (
    <div>
      <Row className="my-1">
        <Col>
          <h2>Crosstab</h2>
        </Col>
        <Col className="float-right">
          <Link to="/" className="btn btn-light my-3">
            Go back
          </Link>
        </Col>
      </Row>
      <Row>
        <Col md={4}>
          <Card>
            <Card.Header as="h5">Upload dataset</Card.Header>
            <Card.Body>
              {errorDataset && (
                <Message variant="danger">{errorDataset}</Message>
              )}
              {loadingDataset && <Loader />}
              <Form>
                <Form.Group controlId="dataset" className="mb-3">
                  <Row className="my-3">
                    <Col>
                      <Form.Label>Dataset: </Form.Label>
                    </Col>
                    <Col>
                      <Form.Control
                        type="file"
                        accept=".xls,.xlsx,.csv,.txt,.tsv"
                        onChange={submitHandler}
                      />
                    </Col>
                  </Row>
                </Form.Group>
              </Form>
            </Card.Body>
            <Card.Footer className="text-center">
              <p>Select your dataset</p>
            </Card.Footer>
          </Card>
        </Col>
        <Col md={8}>
          <Card>
            <Card.Header>Choose Inputs</Card.Header>
            <Card.Body>
              {!crosstabInputsList ? (
                <Message variant="warning">
                  Upload dataset to choose inputs
                </Message>
              ) : (
                <Form onSubmit={submitColumnDetailsHandler}>
                  <Form.Group controlId="genome_column" className="mb-3">
                    <Row>
                      <Col md={4}>
                        <Form.Label>Name of Genome column</Form.Label>
                      </Col>
                      <Col md={8}>
                        <Form.Select
                          required
                          aria-label="Select name of Genome Colum"
                          onChange={(e) => setGenomeName(e.target.value)}
                        >
                          <option>Select column name</option>
                          {crosstabInputsList.map((element) => (
                            <option key={element} value={element}>
                              {element}
                            </option>
                          ))}
                        </Form.Select>
                      </Col>
                    </Row>
                  </Form.Group>
                  <Form.Group controlId="gene_column" className="mb-3">
                    <Row>
                      <Col md={4}>
                        <Form.Label>Name of Gene column</Form.Label>
                      </Col>
                      <Col md={8}>
                        <Form.Select
                          required
                          aria-label="Select name of Genome Colum"
                          onChange={(e) => setGeneName(e.target.value)}
                        >
                          <option>Select column name</option>
                          {crosstabInputsList.map((element) => (
                            <option key={element} value={element}>
                              {element}
                            </option>
                          ))}
                        </Form.Select>
                      </Col>
                    </Row>
                  </Form.Group>
                  <Form.Group controlId="data_format" className="mb-3">
                    <Row>
                      <Col md={4}>
                        <Form.Label>Datset Format</Form.Label>
                      </Col>
                      <Col md={8}>
                        <Form.Select
                          required
                          aria-label="Select name of Genome Colum"
                          onChange={(e) => setDataFormat(e.target.value)}
                        >
                          <option>Select Dataformat</option>
                          <option value="CGE">CGE</option>
                          <option value="PATRIC">PATRIC</option>
                        </Form.Select>
                      </Col>
                    </Row>
                  </Form.Group>
                  <Form.Group controlId="phylo_path" className="mb-3">
                    <Row className="my-3">
                      <Col md={4}>
                        <Form.Label>Phylo path </Form.Label>
                      </Col>
                      <Col md={8}>
                        <Form.Control
                          type="file"
                          accept=".newick"
                          onChange={(e) => setPhyloPath(e.target.files[0])}
                        />
                      </Col>
                    </Row>
                  </Form.Group>
                  <Message variant="info">
                    Note: These values are fetched from uploaded dataset
                  </Message>
                  {error && <Message variant="danger">{error}</Message>}
                  {loading && <Loader />}

                  <Row>
                    <Button
                      variant="primary"
                      type="submit"
                      className="px-1 my-2"
                    >
                      Submit
                    </Button>
                  </Row>
                </Form>
              )}
            </Card.Body>
          </Card>
        </Col>
      </Row>
      {!crosstabResult ? null : (
        <Row className="my-3">
          <ResultsCard result={crosstabResult} />
        </Row>
      )}
    </div>
  );
}

export default CrosstabCard;
