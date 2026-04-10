# SE_LabMidterm_Guevarra

# Calculator ni Lucky

A simple calculator application built with Python and CustomTkinter, developed as a Software Engineering laboratory project. The system follows the MVC (Model-View-Controller) architecture and demonstrates automated unit testing, CI/CD integration using GitHub Actions, and software quality analysis based on ISO/IEC 25010.

---

## Project Structure

```
project_root/
├── main.py  
├── src/  
│   ├── model/  
│   │   └── calculator.py       # Business logic (add, subtract, multiply, divide)  
│   ├── controller/  
│   │   └── controller.py       # Handles interaction between model and view  
│   └── view/  
│       └── view.py             # CustomTkinter user interface  
│
├── tests/  
│   ├── test_addition.py  
│   ├── test_invalid_input.py  
│   ├── test_divide_by_zero.py  
│   └── test_large_numbers.py  
│
├── .github/  
│   └── workflows/  
│       └── ci.yml              # GitHub Actions CI pipeline  
│
├── quality_analysis.md         # ISO/IEC 25010 software quality analysis  
├── requirements.txt  
└── README.md
```

---

## Key Highlights

-  MVC Architecture – Separation of logic, UI, and control flow for maintainability  
- Modern UI – Built using CustomTkinter with a responsive calculator interface  
-  Error Handling – Input validation and safe division implemented in the model layer  
-  Automated Testing – Pytest-based unit tests covering positive, negative, and edge cases  
-  CI/CD Pipeline – GitHub Actions automatically runs tests on every push to develop branch  
-  Software Quality Analysis – ISO/IEC 25010-based evaluation of system quality attributes  

---

## Prerequisites

- Python 3.11 or higher  
- Git  
- pip package manager  

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git  
cd your-repo-name
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Application

```bash
python main.py
```

---

## Running Unit Tests

Run all tests:

```bash
pytest
```

Run tests with verbose output:

```bash
python -m pytest tests/ -v
```

Run specific test files:

```bash
python -m pytest tests/test_addition.py -v  
python -m pytest tests/test_invalid_input.py -v  
python -m pytest tests/test_divide_by_zero.py -v  
python -m pytest tests/test_large_numbers.py -v
```

---

## CI/CD Pipeline

This project uses GitHub Actions for Continuous Integration.

### What it does:
- Installs dependencies  
- Runs all automated tests using pytest  
- Automatically triggers on every push to develop branch  
- Fails the pipeline if any test fails  

### View CI Status:
Go to the Actions tab in the GitHub repository.

---

## Quality Analysis

See quality_analysis.md for:
- Functional Suitability (ISO/IEC 25010)  
- Reliability  
- How automated testing supports quality  
- How CI/CD improves system stability  

---

## Notes

This project demonstrates:
- Clean MVC architecture  
- Automated testing practices  
- DevOps fundamentals (CI/CD)  
- Software quality engineering principles  

---
