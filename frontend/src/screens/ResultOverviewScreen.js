import React, { useEffect } from "react";
import { Card, Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { listResultDetails } from "../actions/resultsListActions";
import { Markup } from "interweave";

function ResultOverviewScreen({ match, history, location }) {
  const resultDetails = useSelector((state) => state.resultDetails);
  const { result } = resultDetails;

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  const dispatch = useDispatch();
  useEffect(() => {
    if (!userInfo) {
      history.push("/login");
    }
    dispatch(listResultDetails(match.params.id));
  }, [dispatch, match, history, userInfo]);

  return (
    <div>
      <h2>Result Overview</h2>
      <Card className="my-3">
        <Card.Header>
          <h2>Result ID</h2>
          {result.result_id}
        </Card.Header>
        <Card.Body>
          <Row>
            <Col md={3}>Created at</Col>
            <Col md={9}>
              <span>Date: {result.created_at} </span>
            </Col>
          </Row>
        </Card.Body>
      </Card>
      <Card className="my-3">
        <Card.Header>
          <h2>Crosstab Table</h2>
        </Card.Header>
        <Card.Body className="overflow-auto">
          <Markup content={result.upload_results} />
        </Card.Body>
      </Card>
    </div>
  );
}

export default ResultOverviewScreen;
