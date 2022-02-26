import React from "react";
import { Container, Button, Form } from "react-bootstrap";
export const Forms = () => {
  return (
    <Container fluid="md">
      <Form>
        <Form.Group className="mb-3" controlId="formBasicEmail">
          <Form.Label>Email</Form.Label>
          <Form.Control type="email" placeholder="Ingrese  email" />
          <Form.Text className="text-muted">
            Nunca compartiremos el email.
          </Form.Text>
        </Form.Group>
        <Form.Group className="mb-3" controlId="formBasicPassword">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" placeholder="Ingrese el Password" />
        </Form.Group>

        <Button variant="primary" type="submit">
          Submit
        </Button>
      </Form>
    </Container>
  );
};
