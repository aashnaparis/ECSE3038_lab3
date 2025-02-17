# Tank Management API

This is a FastAPI-based application for managing tank data. It allows you to create, retrieve, update, and delete tank records.

## Features

- **Create a new tank**: Add a new tank with a unique ID, location, latitude, and longitude.
- **Retrieve all tanks**: Get a list of all tanks.
- **Retrieve a single tank**: Fetch details of a specific tank by its ID.
- **Update a tank**: Partially update a tank's details (location, latitude, or longitude).
- **Delete a tank**: Remove a tank by its ID.

## Models

- **Tank**: Represents a tank with fields `id` (UUID), `location` (str), `lat` (float), and `long` (float).
- **Tank_Update**: Used for partial updates, allowing optional fields.

## Endpoints

- **GET `/tank`**: Retrieve all tanks.
- **GET `/tank/{id}`**: Retrieve a single tank by ID.
- **POST `/tank`**: Create a new tank.
- **DELETE `/tank/{id}`**: Delete a tank by ID.
- **PATCH `/tank/{id}`**: Partially update a tank by ID.

## Error Handling

- **404 Not Found**: Returned when a tank with the specified ID does not exist.
- **400 Bad Request**: Returned when a tank update contains invalid data.

## Lab
This was the third lab of my new and improved of ECSE3038.

## Two Truths and a Lie
What you think?
- **I love bananas**
- **I once allegedly stole from a charity to give to a better charity**
- **I swam for Jamaica one time in Barbados**

heheheh you figure it out
