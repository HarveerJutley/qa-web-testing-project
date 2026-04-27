![CI](https://github.com/HarveerJutley/qa-web-testing-project/actions/workflows/QA%20Test%20Pipeline/badge.svg?branch=main)
# QA Web Testing Project

## Overview
This project is a QA automation suite built in Python to test a sample web application. It demonstrates manual testing design, API testing, and UI automation using modern testing tools and frameworks.

The goal of this project is to simulate QA workflows used in software development teams to ensure application reliability and validity.

---

## Features
- UI automation testing for login functionality
- API testing using HTTP requests
- Manual test case documentation
- Bug report examples
- Structured test framework using pytest

---

## Tools & Technologies
- Python
- Pytest
- Playwright
- Requests
- Git & GitHub

---
## What is Tested

### UI Tests
- Valid login functionality
- Invalid login handling
- Page navigation and URL validation

### API Tests
- GET request validation
- Response status code checks
- Basic data validation

---

## How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/HarveerJutley/qa-web-testing-project.git
cd qa-web-testing-project
```
### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Run tests
```bash
pytest -v
```
