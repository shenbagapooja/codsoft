# 🧮 Simple Calculator

A lightweight Python script that runs in your terminal and performs basic arithmetic operations.

---

## 🎯 About

This is a beginner-friendly calculator built in Python. It takes two numbers and an operator as input and returns the result instantly.

### Operations Supported
* **Addition (`+`)**
* **Subtraction (`-`)**
* **Multiplication (`*`)**
* **Division (`/`)**

---

## 📌 How to Run

Make sure Python is installed, then run the script using the following command in your terminal:

## 🚀 Usage

1. Enter the first number when prompted.
2. Enter the second number when prompted.
3. Enter one of the supported operators: `+`, `-`, `*`, `/`
4. The result will be displayed instantly in the terminal.

## 📌 Code Structure

The program follows a clean, linear architecture divided into four distinct phases:

* **Input Generation:** It collects two numeric inputs and casts them to floating-point numbers, followed by a string input for the operator.
* **Conditional Logic (if-elif-else):** It evaluates the operator string sequentially to determine which mathematical code block to execute.
* **Error Handling (Nested):** Within the division block, a secondary conditional check ensures the denominator is not zero before proceeding.
* **Output Display:** It prints the final calculated value or a predefined error message string.

## 🏷️ Key Features

* **Dynamic Data Typing:** By using `float()`, the code flexibly accepts both integers and decimals rather than restricting the user to whole numbers.
* **Robust Edge-Case Handling:** The nested `if second == 0:` check prevents the program from crashing with a `ZeroDivisionError`.
* **Input Validation:** The final `else` block acts as a catch-all that gracefully manages unsupported operator inputs without breaking execution.
