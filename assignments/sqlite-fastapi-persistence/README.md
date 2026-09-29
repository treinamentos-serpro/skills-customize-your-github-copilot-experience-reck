# 📘 Assignment: SQLite and Data Persistence with FastAPI

## 🎯 Objective

Learn how to connect a FastAPI application to a SQLite database and persist data across requests. This assignment focuses on CRUD operations, data validation, and basic database integration in Python.

## 📝 Tasks

### 🛠️ Set Up the Database and API

#### Descrição
Create a small FastAPI application that connects to a SQLite database and exposes a simple API for managing records.

#### Requisitos
O programa concluído deve:

- create a FastAPI app and configure SQLite for local data storage
- define a Pydantic model for the data being stored
- create a table in the database to hold records
- return JSON responses from the API endpoints
- test the app locally with a browser or API client

### 🛠️ Add CRUD Endpoints

#### Descrição
Implement basic create, read, update, and delete operations so the API can persist and retrieve records from the SQLite database.

#### Requisitos
O programa concluído deve:

- add a `POST` endpoint to create a new record
- add a `GET` endpoint to list all records
- add a `GET` endpoint to fetch one record by id
- add a `PUT` or `PATCH` endpoint to update a record
- add a `DELETE` endpoint to remove a record
- validate user input and handle missing records gracefully
