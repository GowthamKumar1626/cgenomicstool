import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { listResultDetails } from "../actions/resultsListActions";

function ResultOverviewScreen({ match }) {
  const resultDetails = useSelector((state) => state.resultDetails);
  const { product } = resultDetails;

  const dispatch = useDispatch();
  useEffect(() => {
    dispatch(listResultDetails(match.params.id));
  }, [dispatch, match]);
  return (
    <div>
      <h2>Result Overview</h2>
      <h4>{match.params.id}</h4>
      <h4>{product.created_at}</h4>
    </div>
  );
}

export default ResultOverviewScreen;
