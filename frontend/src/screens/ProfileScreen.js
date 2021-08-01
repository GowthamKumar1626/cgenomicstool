import React, { useState, useEffect } from "react";
import { Form, Button, Row, Col, Card } from "react-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { USER_UPDATE_PROFILE_RESET } from "../constants/userConstants";
import { getUserDetails, updateUserProfile } from "../actions/userActions";
import {
  listResults,
  deleteResult,
  downloadResult,
} from "../actions/resultsListActions";
import { Link } from "react-router-dom";

function ProfileScreen({ location, history }) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [message, setMessage] = useState("");

  const dispatch = useDispatch();

  const userDetails = useSelector((state) => state.userDetails);
  const { error, loading, user } = userDetails;

  const userLogin = useSelector((state) => state.userLogin);
  const { userInfo } = userLogin;

  const userUpdateProfile = useSelector((state) => state.userUpdateProfile);
  const { success } = userUpdateProfile;

  const resultsList = useSelector((state) => state.resultsList);
  const { results } = resultsList;

  const resultDelete = useSelector((state) => state.resultDelete);
  const {
    loading: loadingDelete,
    error: errorDelete,
    success: successDelete,
  } = resultDelete;

  useEffect(() => {
    if (!userInfo) {
      history.push("/login");
    } else {
      if (!user || !user.name || success || userInfo._id !== user._id) {
        dispatch({ type: USER_UPDATE_PROFILE_RESET });
        dispatch(getUserDetails("profile"));
        dispatch(listResults());
      } else {
        setName(user.name);
        setEmail(user.email);
      }
      dispatch(listResults());
    }
  }, [dispatch, history, userInfo, user, success, successDelete]);

  const submitHandler = (e) => {
    e.preventDefault();

    if (password !== confirmPassword) {
      setMessage("Passwords do not match");
    } else {
      dispatch(
        updateUserProfile({
          id: user._id,
          name: name,
          email: email,
          password: password,
        })
      );
      setMessage("");
    }
  };

  const resultDownloadHandler = (id) => {
    dispatch(downloadResult(id));
  };

  const resultDeleteHandler = (id) => {
    if (window.confirm("Are you sure you want to delete this result?")) {
      dispatch(deleteResult(id));
    }
  };

  return (
    <Row>
      <Col md={4}>
        <Card>
          <Card.Header>
            <h3>User Profile</h3>
          </Card.Header>
          <Card.Body>
            {message && <Message variant="danger">{message}</Message>}
            {error && <Message variant="danger">{error}</Message>}
            {loading && <Loader />}

            <Form onSubmit={submitHandler}>
              <Form.Group controlId="name" className="my-1">
                <Form.Label>Name</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Enter name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                />
              </Form.Group>
              <Form.Group controlId="email" className="my-1">
                <Form.Label>Email</Form.Label>
                <Form.Control
                  required
                  type="email"
                  placeholder="Enter email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                />
              </Form.Group>
              <Form.Group controlId="password" className="my-1">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Enter password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </Form.Group>
              <Form.Group controlId="passwordConfirm" className="my-3">
                <Form.Label>Re-type Password</Form.Label>
                <Form.Control
                  type="password"
                  placeholder="Re-type password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                />
              </Form.Group>
              <Button type="submit" variant="primary">
                Update
              </Button>
            </Form>
          </Card.Body>
        </Card>
      </Col>
      {loadingDelete && <Loader />}
      <Col md={8}>
        {errorDelete && <Message variant="danger">{errorDelete}</Message>}
        <Card>
          <Card.Header>
            <h3>Results</h3>
          </Card.Header>
          <Card.Body>
            {results.map((result) => (
              <Row key={result.result_id} className="my-2">
                <Col md={7}>
                  <Link to={`/results/${result.result_id}`}>
                    <h5>{result.result_id}</h5>
                  </Link>
                </Col>
                <Col md={3}>
                  Date: {result.created_at.split("T")[0]}
                  <br></br>
                  Time: {result.created_at.split("T")[1].slice(1, 8)}
                </Col>
                <Col md={1}>
                  <i
                    className="fas fa-download"
                    onClick={() => resultDownloadHandler(result.result_id)}
                  ></i>
                </Col>
                <Col md={1}>
                  <i
                    className="fas fa-trash pe-auto"
                    onClick={() => resultDeleteHandler(result.result_id)}
                  ></i>
                </Col>
              </Row>
            ))}
          </Card.Body>
        </Card>
      </Col>
    </Row>
  );
}

export default ProfileScreen;
