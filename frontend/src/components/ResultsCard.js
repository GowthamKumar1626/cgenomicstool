import React from "react";
import { Row, Col } from "react-bootstrap";
import { Link } from "react-router-dom";

function ResultsCard({ result }) {
  const resultDownloadHandler = (e) => {
    console.log("Download");
  };

  const resultDeleteHandler = (result_id) => {
    console.log(result_id);
  };
  return (
    <div>
      <h1>Result Overview</h1>
      <Row className="my-3">
        <Col md={4}>
          <Row>
            <h5>Result id:</h5>
            <h5>Crosstab</h5>
            <h5>Actions</h5>
          </Row>
        </Col>
        <Col md={8}>
          <Row>
            <h5>ID-323523523</h5>
            <Link to={`/results/${result.saved_dataset}`}>
              <h5>{result.saved_dataset} </h5>
            </Link>
            <Row>
              <Col md={1}>
                <i
                  className="fas fa-download"
                  onClick={resultDownloadHandler}
                ></i>
              </Col>
              <Col md={1}>
                <i className="fas fa-trash" onClick={resultDeleteHandler}></i>
              </Col>
            </Row>
          </Row>
        </Col>
      </Row>
    </div>
  );
}

export default ResultsCard;
