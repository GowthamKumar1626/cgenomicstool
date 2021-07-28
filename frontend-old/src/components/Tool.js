import React from "react";
import { Card } from "react-bootstrap";
import { Link } from "react-router-dom";

function Tool({ tool }) {
  return (
    <Card className="my-3">
      <Link to={`/tools/${tool.href}`}>
        <Card.Img src={tool.image} className="card-img-top" />
      </Link>

      <Card.Body>
        <Link to={`/tools/${tool.href}`}>
          <Card.Title as="div">
            <strong>{tool.name}</strong>
          </Card.Title>
        </Link>
        <Card.Text as="div">
          <div className="my-3">{tool.description}</div>
        </Card.Text>
      </Card.Body>
    </Card>
  );
}

export default Tool;
