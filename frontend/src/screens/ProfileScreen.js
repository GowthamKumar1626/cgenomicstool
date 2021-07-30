import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Form, Button, Row, Col, Table, Card } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";
import { useDispatch, useSelector } from "react-redux";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { getUserDetails } from "../actions/userActions";

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

  useEffect(() => {
    if (!userInfo) {
      history.push("/login");
    } else {
      if (!user || !user.name) {
        dispatch(getUserDetails("profile"));
      } else {
        setName(user.name);
        setEmail(user.email);
      }
    }
  }, [user, history, userInfo, dispatch]);

  //   const submitHandler = (e) => {
  //     e.preventDefault();

  //     if (password != confirmPassword) {
  //       setMessage("Passwords do not match");
  //     } else {
  //       dispatch(
  //         updateUserProfile({
  //           id: user._id,
  //           name: name,
  //           email: email,
  //           password: password,
  //         })
  //       );
  //       setMessage("");
  //     }
  //   };
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
            <Form>
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
                  required
                  type="password"
                  placeholder="Enter password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                />
              </Form.Group>
              <Form.Group controlId="passwordConfirm" className="my-1">
                <Form.Label>Re-type Password</Form.Label>
                <Form.Control
                  required
                  type="password"
                  placeholder="Re-type password"
                  value={confirmPassword}
                  onChange={(e) => setConfirmPassword(e.target.value)}
                />
              </Form.Group>
              <Button type="submit" variant="primary">
                Register
              </Button>
            </Form>
            <Row className="py-3">
              <Col>
                Have an account? <Link>Update</Link>
              </Col>
            </Row>
          </Card.Body>
        </Card>
      </Col>
      <Col md={8}>
        <Card>
          <Card.Header>
            <h3>Results</h3>
          </Card.Header>
          <Card.Body></Card.Body>
        </Card>
      </Col>
    </Row>
  );
}

export default ProfileScreen;
