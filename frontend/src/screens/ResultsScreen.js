import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Table, Form, Button } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

import { listResults } from "../actions/resultsActions";
import { deleteResult } from "../actions/resultsActions";

import Loader from "../components/Loader";
import Message from "../components/Message";

function ResultsScreen() {
  const dispatch = useDispatch();
  const resultsList = useSelector((state) => state.resultsList);
  const { error, loading, results } = resultsList;

  useEffect(() => {
    dispatch(listResults());
  }, [dispatch]);

  function handleCheckBoxClick() {
    const mainCheckBox = document.getElementById("main-check-box");
    const subCheckBoxes = document.querySelectorAll("#child-check-box");

    switch (mainCheckBox.checked) {
      case true:
        subCheckBoxes.forEach((element) => (element.checked = true));
        break;
      case false:
        subCheckBoxes.forEach((element) => (element.checked = false));
        break;
      default:
        console.log("Wrong Functionality .. ");
    }
  }

  const deleteResultHandler = (id) => {
    dispatch(deleteResult(id));
  };

  return (
    <div>
      <h2>Results</h2>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="danger">{error}</Message>
      ) : results.length > 0 ? (
        <Table striped bordered hover size="xl">
          <thead>
            <tr>
              <th>
                <Form.Check
                  type="checkbox"
                  id="main-check-box"
                  onClick={handleCheckBoxClick}
                />
              </th>
              <th>Result ID</th>
              <th>Tool used</th>
              <th>Created at</th>
              <th>Expires at</th>
              <th />
            </tr>
          </thead>
          <tbody>
            {results.map((result) => (
              <tr key={result.job_id}>
                <td className="text-left align-middle">
                  <Form.Check type="checkbox" id="child-check-box" />
                </td>
                <LinkContainer to={`/results/${result.job_id}`}>
                  <td className="text-left align-middle"> {result.job_id} </td>
                </LinkContainer>

                <td className="text-left align-middle">{result.tool_used}</td>
                <td className="text-left align-middle">{result.created_at}</td>
                <td className="text-left align-middle">{result.expires_at}</td>
                <td className="text-left align-middle">
                  <Button
                    variant="danger"
                    onClick={() => deleteResultHandler(result.job_id)}
                  >
                    <i className="fas fa-trash-alt"></i> Delete
                  </Button>
                </td>
              </tr>
            ))}
          </tbody>
        </Table>
      ) : (
        <Message variant="primary" href="/">{`No results found  `}</Message>
      )}
    </div>
  );
}

export default ResultsScreen;
