# Project Architecture Module

## Introduction
The Project Architecture Module outlines the design, relationships, data modeling, and workflow structures of the Credit Card Approval Prediction System.

## Purpose
To detail the data flows, technical stacks, user interactions, and database entities required to support reliable predictions.

## Objectives
- Document system entity relationships (ER Diagram).
- Map end-to-end execution data flow (Project Flow Diagram).
- Model architectural layers (Technical Architecture Diagram).
- Model user interactions (Use Case Diagram).
- Track development lifecycles (Workflow Diagram).

## Files Present
- [README.md](file:///c:/Users/laksh/CreditCard/02_Project_Architecture/README.md): Architecture documentation.
- **ER Diagram files**:
  - `ER_Diagram.mmd`: Mermaid diagram source.
  - `ER_Diagram.drawio`: Draw.io XML source.
  - `ER_Diagram.png`: Rendered image.
- **Project Flow files**:
  - `Project_Flow.mmd`: Mermaid diagram source.
  - `Project_Flow.drawio`: Draw.io XML source.
  - `Project_Flow.png`: Rendered image.
- **Technical Architecture files**:
  - `Technical_Architecture.mmd`: Mermaid diagram source.
  - `Technical_Architecture.drawio`: Draw.io XML source.
  - `Technical_Architecture.png`: Rendered image.
- **Use Case Diagram files**:
  - `Use_Case_Diagram.drawio`: Draw.io XML source.
  - `Use_Case_Diagram.png`: Rendered image.
- **Workflow Diagram files**:
  - `Workflow_Diagram.drawio`: Draw.io XML source.
  - `Workflow_Diagram.png`: Rendered image.

## System Architecture Overview

### 1. Entity Relationship (ER) Diagram
Models the logical tables and relationships between Applicant details, Credit History records, the Web Application, the Prediction Engine, and final approval results.
- **Applicant** (1) ── (1..N) **Credit Record**
- **Applicant** (1) ── (1) **Prediction Request** ── (1) **ML Model** ── (1) **Prediction Output**

### 2. Project Flow Diagram
Maps out the sequential execution flow from raw dataset collections, exploratory data analyses, preprocessing, model evaluations, best model saving, up to Flask runtime inferences.

### 3. Technical Architecture Diagram
Visualizes the multi-tier application stack:
- **Client Tier**: Web Browser (HTML, CSS, JS, Bootstrap)
- **Web Tier**: Flask Web Server (App Routes, Form Validation)
- **Business/ML Tier**: Preprocessing Pipelines, Encoded scaler transformations, Best ML Classifier (XGBoost/Random Forest)

### 4. Use Case Diagram
Models actor-system actions:
- **Applicant/Client**: Browses Home, views Project Info, enters details, submits form, views results.
- **System**: Performs form validation, processes raw features, executes predictions, renders output.

### 5. Workflow Diagram
Illustrates the development steps: Data Collection -> Data Analysis -> Data Preprocessing -> Model Building -> Web Application -> Deployment.

## Technologies Used
- Mermaid.js (for `.mmd` scripting)
- Draw.io (for XML vector structures)
- Python / Flask (for web server backend)

## Expected Outputs
Rendered PNG flowcharts depicting system blueprints.

## Conclusion
A documented architecture ensures clean modular integration between the data science pipeline and the web deployment layers.
