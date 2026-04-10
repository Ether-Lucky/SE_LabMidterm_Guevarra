# Software Quality Analysis

## Overview

This document explains the software quality attributes applied in the development of the MVC-based calculator application. The analysis is based on the ISO/IEC 25010 software quality model and focuses on two relevant quality attributes: **Functional Suitability** and **Reliability**. It also explains how automated testing and CI/CD contribute to improving overall software quality.

---

## 1. Functional Suitability

Functional Suitability refers to how well a system provides the functions that meet stated and implied user needs. It includes correctness, completeness, and appropriateness of the implemented features.

In the calculator module, Functional Suitability is demonstrated through the implementation of core arithmetic operations such as addition, subtraction, multiplication, and division. Each operation is handled by the model layer, ensuring that the system produces correct outputs based on valid inputs.

Input validation in the controller also contributes to functional suitability by ensuring that only numerical values are processed. This prevents incorrect or unintended behavior caused by invalid user input.

### Support from Testing

Automated testing directly supports Functional Suitability by verifying that all operations behave as expected. The test cases include:
- Positive test case for valid arithmetic operations (e.g., addition)
- Negative test case for invalid input handling
- Edge cases such as division by zero and large number computations

These tests ensure that the calculator consistently produces correct results and handles invalid scenarios appropriately.

---

## 2. Reliability

Reliability refers to the ability of the system to perform consistently under defined conditions without failure. It also includes fault tolerance and error handling.

In this application, reliability is achieved through proper exception handling in the model and controller layers. For example, division by zero is explicitly handled to prevent system crashes. Additionally, invalid inputs are caught and managed gracefully, ensuring that the application remains stable during unexpected user behavior.

### Support from Testing

Reliability is reinforced through automated tests that simulate failure scenarios. For example:
- Division by zero test ensures the system does not crash and raises a controlled error
- Invalid input tests confirm that the system properly rejects non-numeric values

These tests ensure that the system behaves consistently even when encountering erroneous inputs.

---

## 3. Role of CI/CD in Software Quality

Continuous Integration and Continuous Deployment (CI/CD) is implemented using GitHub Actions. The CI pipeline automatically executes all test cases whenever changes are pushed to the development branch.

The CI/CD pipeline improves software quality in the following ways:

- **Early Detection of Errors:** Issues are identified immediately after code changes are pushed.
- **Automated Testing:** All test cases are executed without manual intervention, reducing human error.
- **Consistency:** Every code update is validated using the same environment and test suite.
- **Reliability Assurance:** The pipeline fails automatically if any test case fails, preventing unstable code from being integrated.

This ensures that only verified and stable code progresses through the development workflow, improving overall system reliability.

---

## Conclusion

The calculator application demonstrates strong adherence to ISO/IEC 25010 quality standards, particularly Functional Suitability and Reliability. Automated testing ensures correctness and robustness of features, while CI/CD integration enhances consistency and prevents defective code from being merged. Together, these practices improve the overall software quality and maintainability of the system.