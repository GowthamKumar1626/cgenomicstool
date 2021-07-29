import React from "react";
import { Alert } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

function Message({ variant, href, children }) {
  return (
    <Alert key="1" variant={variant}>
      {children}
      {href ? (
        <div style={{ display: "inline" }}>
          <LinkContainer to={href}>
            <Alert.Link> Clik here </Alert.Link>
          </LinkContainer>
          to submit results
        </div>
      ) : (
        ""
      )}
    </Alert>
  );
}

export default Message;
