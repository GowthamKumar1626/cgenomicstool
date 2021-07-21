import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";

import { listResultDetails } from "../actions/resultsActions";
import Loader from "../components/Loader";
import Message from "../components/Message";
import ResultCard from "../components/ResultCard";

function ResultDetailScreen({ match }) {
  const dispatch = useDispatch();
  const resultDetails = useSelector((state) => state.resultDetails);
  const { error, loading, result } = resultDetails;

  useEffect(() => {
    dispatch(listResultDetails(match.params.id));
  }, [dispatch, match]);

  return (
    <div>
      <h2>Results Details</h2>
      {loading ? (
        <Loader />
      ) : error ? (
        <Message variant="error">{error}</Message>
      ) : (
        <ResultCard result={result} match={match} />
      )}
    </div>
  );
}

export default ResultDetailScreen;
