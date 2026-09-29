# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework, including request handling, JSON responses, data modeling, and basic CRUD operations in Python.

## 📝 Tasks

### 🛠️ Create the API Application

#### Descrição
Set up a minimal FastAPI application that exposes endpoints for a simple collection of items or products. Use Python type hints and a basic data model to structure the API responses.

#### Requisitos
O programa concluído deve:

- create a FastAPI application instance and configure a basic route
- define a Pydantic model for the resource being served
- add at least one `GET` endpoint to return a list or a single item
- start the app locally with `uvicorn` and verify that the API responds correctly

### 🛠️ Add CRUD Endpoints

#### Descrição
Expand the application with create, read, update, and delete operations to simulate a small in-memory backend for storing items.

#### Requisitos
O programa concluído deve:

- add a `POST` endpoint that creates a new item
- add a `GET` endpoint to retrieve all items
- add a `PUT` or `PATCH` endpoint to update an item
- add a `DELETE` endpoint to remove an item
- return clear JSON responses and validate input data before storing it
