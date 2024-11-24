# Project Matteo

This is a basic project on having a hosted website delivering a <value> to the users

## Phase 1
- Have a fully functional SIP calculator: 
    - Should have classes
    - Should have a streamlit application frontend
    - Should have a grahical interface
- Should be a hosted service

## Phase 2
- Integration of a database to store key information

## Phase 3 
- Go on to build a full-to forecast flow for multiple investments


content = """
# Python Project Folder Structure

## **1. Core Application**
- **`src/`**  
  The source code of the project. This is often the root folder containing the main application logic.

---

## **2. Core Functionality**
- **`services/`**  
  Contains business logic, service classes, and modules responsible for interacting with external APIs, databases, or other systems.
  
- **`models/`**  
  For database models, ORM classes (e.g., SQLAlchemy, Django models), or data structures.

- **`controllers/`** *(Optional)*  
  For handling incoming requests and routing them to services or models (common in web apps).

- **`utils/`**  
  Helper functions, utilities, or reusable modules that don't fit in other categories.

---

## **3. Configuration**
- **`config/`**  
  Contains configuration files for the project, such as environment variables, constants, or app-specific settings.

---

## **4. Testing**
- **`tests/`**  
  Holds unit tests, integration tests, and test fixtures. Common substructure:
  - `unit/` (Unit tests)
  - `integration/` (Integration tests)
  - `mocks/` (Mock data or functions)

---

## **5. Documentation**
- **`docs/`**  
  Includes project documentation, API docs, architecture diagrams, or markdown files.

---

## **6. Static or External Files**
- **`static/`** *(Optional)*  
  For static files such as images, CSS, JavaScript, or pre-built assets.

- **`templates/`** *(Optional)*  
  HTML or Jinja templates (common in web frameworks like Flask or Django).

---

## **7. Scripts and Utilities**
- **`scripts/`**  
  One-off scripts for running tasks like database migrations, seeding data, or maintenance.

---

## **8. Logs and Data**
- **`logs/`**  
  For log files generated during application runtime.

- **`data/`**  
  Includes datasets, CSVs, or other input/output data.

---

## **9. Deployment**
- **`deploy/`** *(Optional)*  
  Configuration for deployment, such as Dockerfiles, Kubernetes manifests, or CI/CD scripts.

---

## **10. Others**
- **`middlewares/`** *(Optional)*  
  Custom middlewares for frameworks that support them (e.g., Flask, Django).

- **`plugins/`** *(Optional)*  
  Add-ons or extension modules.

- **`exceptions/`** *(Optional)*  
  Custom exception classes for the application.

---