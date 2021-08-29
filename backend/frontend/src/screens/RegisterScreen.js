import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { Container, Row, Col, Form, Button } from "react-bootstrap";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { register } from "../actions/userActions";
import ReCAPTCHA from "react-google-recaptcha";

function RegisterScreen({ location, history }) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [message, setMessage] = useState("");
  const [isCaptchaVerified, setIsCaptchaVerified] = useState("");
  const [captchaVerifiedMessage, setCaptchaVerifiedMessage] = useState("");

  const dispatch = useDispatch();

  const redirect = location.search ? location.search.split("=")[1] : "/";

  const userRegister = useSelector((state) => state.userRegister);
  const { error, loading, userInfo } = userRegister;

  useEffect(() => {
    if (userInfo) {
      history.push(redirect);
    }
  }, [history, userInfo, redirect]);

  const submitHandler = (event) => {
    event.preventDefault();
    if (password !== confirmPassword) {
      setMessage("Passwords do not match");
    } else {
      if (email && password && confirmPassword) {
        if (isCaptchaVerified) {
          dispatch(register(name, email, password));
        } else {
          setCaptchaVerifiedMessage("Please verify captcha");
        }
      } else {
        setCaptchaVerifiedMessage("Please fill all details");
      }
    }
  };

  const onChangeCaptcha = (value) => {
    console.log(value);
    setIsCaptchaVerified(value);
  };

  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          <h1>Register</h1>
          {message && <Message variant="danger">{message}</Message>}
          {error && <Message variant="danger">{error}</Message>}
          {loading && <Loader />}
          <Form onSubmit={submitHandler}>
            <Row className="my-3">
              <Col md={5}>
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
              </Col>
              <Col md={7}>
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
              </Col>
            </Row>

            <Form.Group controlId="password" className="my-3">
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

            <Row className="my-3">
              <Col>
                <ReCAPTCHA
                  sitekey="6LcsrzAcAAAAAJkg8KvEVYgwmG3kAW8olOf1faXl"
                  onChange={onChangeCaptcha}
                />
              </Col>
              <Col>
                <Button type="submit" variant="primary" className="my-1 w-50">
                  REGISTER
                </Button>
                <Row className="py-1">
                  <Col>
                    Have an account?{" "}
                    <Link
                      to={redirect ? `/login?redirect=${redirect}` : "/login"}
                    >
                      SIGN IN
                    </Link>
                  </Col>
                </Row>
              </Col>
            </Row>
          </Form>

          {captchaVerifiedMessage ? (
            <Message variant="danger">{captchaVerifiedMessage}</Message>
          ) : null}
        </Col>
      </Row>
    </Container>
  );
}

export default RegisterScreen;
