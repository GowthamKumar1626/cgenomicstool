import React, { useEffect } from "react";
import { Card, Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { listResultDetails } from "../actions/resultsListActions";
import { codes } from "../constants/GeneClasses";
// import { Markup } from "interweave";
import Loader from "../components/Loader";

function ResultOverviewScreen({ match, history, location }) {
  const resultDetails = useSelector((state) => state.resultDetails);
  const { loading, result } = resultDetails;

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  const dispatch = useDispatch();
  useEffect(() => {
    if (!userInfo) {
      history.push("/login");
    }
    dispatch(listResultDetails(match.params.id));
    // const dataframeElement = (document.getElementsByClassName(
    //   "dataframe"
    // )[0].innerHTML = result.upload_results);
  }, [dispatch, match, history, userInfo]);

  return (
    <div>
      <h2>Result Overview</h2>
      <Card className="my-3">
        {loading && <Loader />}
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
      <Row>
        <Col md={3}>
          <Card>
            <Card.Header>Color Mappings</Card.Header>
            <Card.Body className="overflow-auto">
              <div>
                {codes.map((code) => (
                  <Row key={code.name}>
                    <Col md={9}>
                      <p>{code["geneName"]}</p>
                    </Col>
                    <Col md={3}>
                      <div
                        style={{
                          backgroundColor: code["colorCode"],
                          height: 20,
                          width: 40,
                        }}
                      ></div>
                    </Col>
                  </Row>
                ))}
              </div>
            </Card.Body>
          </Card>
        </Col>
        <Col md={9}>
          <Card>
            <Card.Header>HeatMap</Card.Header>
            <Card.Body></Card.Body>
          </Card>
        </Col>
      </Row>

      {/* <Card>
        <Card.Header>
          <h2>Details</h2>
        </Card.Header>
        <Card.Body className="overflow-auto">
        <Card.Body>
          <div className="dataframe"></div>
          <Markup content={result.upload_results} />
        </Card.Body>
      </Card> */}
    </div>
  );
}

export default ResultOverviewScreen;
