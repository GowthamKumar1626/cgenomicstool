import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { useDispatch, useSelector } from "react-redux";
import { Container, Row, Col, Form, Button } from "react-bootstrap";
import Loader from "../components/Loader";
import Message from "../components/Message";
import { login } from "../actions/userActions";
import ReCAPTCHA from "react-google-recaptcha";

function LoginScreen({ location, history }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [isCaptchaVerified, setIsCaptchaVerified] = useState("");
  const [captchaVerifiedMessage, setCaptchaVerifiedMessage] = useState("");

  const dispatch = useDispatch();

  const redirect = location.search ? location.search.split("=")[1] : "/";

  const userLogin = useSelector((state) => state.userLogin);
  const { error, loading, userInfo } = userLogin;

  useEffect(() => {
    if (userInfo) {
      history.push(redirect);
    }
  }, [history, userInfo, redirect]);

  const submitHandler = (event) => {
    event.preventDefault();
    if (email && password) {
      if (isCaptchaVerified) {
        dispatch(login(email, password));
      } else {
        setCaptchaVerifiedMessage("Please verify captcha");
      }
    } else {
      setCaptchaVerifiedMessage("Please fill email and password");
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
          <h1>Sign In</h1>
          {error && <Message variant="danger">{error}</Message>}
          {loading && <Loader />}
          <Form onSubmit={submitHandler}>
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

            <Row className="my-3">
              <Col>
                <ReCAPTCHA
                  sitekey="6LcsrzAcAAAAAJkg8KvEVYgwmG3kAW8olOf1faXl"
                  onChange={onChangeCaptcha}
                />
              </Col>
              <Col>
                <Button type="submit" variant="primary" className="my-1 w-50">
                  SIGN IN
                </Button>
                <Row className="py-1">
                  <Col>
                    New User?{" "}
                    <Link
                      to={
                        redirect
                          ? `/register?redirect=${redirect}`
                          : "/register/"
                      }
                    >
                      REGISTER
                    </Link>
                  </Col>
                </Row>
              </Col>
            </Row>

            {captchaVerifiedMessage ? (
              <Message variant="danger">{captchaVerifiedMessage}</Message>
            ) : null}
          </Form>
        </Col>
      </Row>
    </Container>
  );
}

export default LoginScreen;
