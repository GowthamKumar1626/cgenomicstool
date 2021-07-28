import React from "react";
import { Container, Nav, Navbar, NavDropdown } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

function Header() {
  return (
    <header>
      <Navbar bg="primary" variant="dark" expand="lg" collapseOnSelect>
        <Container>
          <LinkContainer to="/">
            <Navbar.Brand>CGenomicsTool</Navbar.Brand>
          </LinkContainer>
          <Navbar.Toggle aria-controls="navbarScroll" />
          <Navbar.Collapse id="navbarScroll">
            <Nav
              className="mr-auto my-2 my-lg-0"
              style={{ maxHeight: "100px" }}
              navbarScroll
            >
              <LinkContainer to="/home">
                <Nav.Link>
                  <i className="fas fa-home"></i> Home
                </Nav.Link>
              </LinkContainer>

              <LinkContainer to="/about-us">
                <Nav.Link>
                  <i className="fas fa-info-circle"></i> About Us
                </Nav.Link>
              </LinkContainer>

              <LinkContainer to="/login">
                <Nav.Link>
                  <i className="fas fa-user"></i> Login
                </Nav.Link>
              </LinkContainer>

              <LinkContainer to="/results">
                <Nav.Link>
                  <i className="fas fa-poll-h"></i> Results
                </Nav.Link>
              </LinkContainer>

              <NavDropdown title="Tools" id="navbarScrollingDropdown">
                <LinkContainer to="/tools/crosstab">
                  <NavDropdown.Item>Crosstab</NavDropdown.Item>
                </LinkContainer>

                <LinkContainer to="/tools/gene-organisation">
                  <NavDropdown.Item>Gene Organisation</NavDropdown.Item>
                </LinkContainer>

                <NavDropdown.Divider />
                <NavDropdown.Item href="#action5">
                  Something else here
                </NavDropdown.Item>
              </NavDropdown>

              {/* <Nav.Link href="#" disabled>
                Link
              </Nav.Link> */}
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  );
}

export default Header;
