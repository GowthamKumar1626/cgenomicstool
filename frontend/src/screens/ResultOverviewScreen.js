import React, { useEffect } from "react";
import { Card, Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { listResultDetails } from "../actions/resultsListActions";
import { deleteResult } from "../actions/resultsListActions";
import Loader from "../components/Loader";
import Message from "../components/Message";

function ResultOverviewScreen({ match, history, location }) {
  const resultDetails = useSelector((state) => state.resultDetails);
  const { result } = resultDetails;

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  const resultDelete = useSelector((state) => state.resultDelete);
  const {
    loading: loadingDelete,
    error: errorDelete,
    success: successDelete,
  } = resultDelete;

  const dispatch = useDispatch();
  useEffect(() => {
    if (!userInfo) {
      history.push("/login");
    } else if (!result) {
      history.push("/profile");
    }
    dispatch(listResultDetails(match.params.id));
  }, [dispatch, match, history, result, userInfo, successDelete]);

  const resultDeleteHandler = (id) => {
    if (window.confirm("Are you sure you want to delete this result?")) {
      dispatch(deleteResult(id));
      history.push("/profile");
    }
  };

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
            <Col md={9}>
              <span>Date: {result.created_at} </span>
            </Col>
          </Row>
          <Row>
            <Col md={3}>Result actions</Col>
            <Col md={1}>
              <i
                className="fas fa-trash pe-auto"
                onClick={() => resultDeleteHandler(result.result_id)}
              ></i>
            </Col>
            <Col md={8}>
              {loadingDelete && <Loader />}
              {errorDelete && <Message variant="danger">{errorDelete}</Message>}
            </Col>
          </Row>
        </Card.Body>
      </Card>
    </div>
  );
}

export default ResultOverviewScreen;
