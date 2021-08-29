import React, { useEffect } from "react";
import { Card, Row, Col } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import { listResultDetails } from "../actions/resultsListActions";
// import { crosstabPlot } from "../actions/crosstabActions";
// import { codes } from "../constants/GeneClasses";

// import { Markup } from "interweave";
import Loader from "../components/Loader";
// import Plot from "../components/Plot";
import Cell from "../components/Cell";

function ResultOverviewScreen({ match, history, location }) {
  const resultDetails = useSelector((state) => state.resultDetails);
  const { loading, result } = resultDetails;

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  // const crosstabPlotDetails = useSelector((state) => state.crosstabPlot);
  // const { loading: loadingPlot,crosstabImage: crosstabImage } = crosstabPlotDetails;

  const dispatch = useDispatch();
  useEffect(() => {
    if (!userInfo) {
      history.push("/login");
    }
    dispatch(listResultDetails(match.params.id));
    // dispatch(crosstabPlot(match.params.id));
    // const dataframeElement = (document.getElementsByClassName(
    //   "dataframe"
    // )[0].innerHTML = result.upload_results);
  }, [dispatch, match, history, userInfo]);

  let style = {
    height: 25,
  };

  // Each - 25
  // 10 - 350
  // 9 - 325
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
      <Card className="my-3">
        <Card.Header>HeatMap</Card.Header>
        <Card.Body id="plot-table" className="overflow-auto">
          {/* <Plot /> */}
          <div className="timeline-body">
            <div className="timeline-cells" style={style}>
              <Cell color={"rgba(3, 160, 3, 0.6)"} />
            </div>
          </div>

          {/* <Card.Img
            src={result.image}
            className="crosstab-image overflow-auto"
          /> */}
        </Card.Body>
      </Card>
      {/* <Row>
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
      </Row> */}

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
