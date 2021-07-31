import React, { useEffect } from "react";
import { Card, Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { listResultDetails } from "../actions/resultsListActions";

function ResultOverviewScreen({ match }) {
  const resultDetails = useSelector((state) => state.resultDetails);
  const { result } = resultDetails;

  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(listResultDetails(match.params.id));
  }, [dispatch, match]);
  return (
    <div>
      <h2>Result Overview</h2>
      <Card>
        <Card.Header>
          <h2>Result ID</h2>
          {result.result_id}
        </Card.Header>
        <Card.Body>
          <Row>
            <Col md={3}>Created at</Col>
            <Col md={9}>{result.created_at}</Col>
          </Row>
        </Card.Body>
      </Card>
    </div>
  );
}

export default ResultOverviewScreen;
