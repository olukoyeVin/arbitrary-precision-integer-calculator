# arbitrary-precision-integer-calculator
This repository contains an implementation of an arbitrary-precision integer calculator, designed without relying on native arbitrary-precision support or external libraries. The calculator supports fundamental arithmetic operations and factorials with meticulous attention to algorithmic depth and robust edge-case handling.
Features
Core Functionality:
Addition, Subtraction, Multiplication, Division (with remainder), and Factorials.
Handles very large integers efficiently using custom algorithms.
Robust Design:
Input validation and normalization (e.g., removing leading zeros, handling invalid inputs).
Graceful handling of boundary conditions like division by zero and subtracting larger numbers.
Efficiency:
Implements digit-by-digit arithmetic optimized for performance.
Modular design for ease of extension (e.g., adding support for additional operations).
Read-Eval-Print Loop (REPL):
Interactive interface for performing calculations.
Supports expressions like 12345 + 6789, 100!, and 100 / 3.
# Usage
Running the Calculator
Clone the repository:
git clone https://github.com/your-username/big-int-calculator.git
cd big-int-calculator

Run the calculator:
python calculator/big_int.py

Interact with the REPL:
>> 12345 + 6789
19134
>> 100!
933262154439441526816992388562667004907159682643816214685929638952175999932299156089414639761565182862536979208272237582511852109168640000000000000000000000
# Running Tests
The repository includes a suite of unit tests to validate the core functionality:
python -m unittest discover -s calculator -p "test_*.py"
# Design Insights
This implementation was approached with a focus on depth, prioritizing the following aspects:

Custom Data Representation:
Numbers are stored as reversed lists of digits, allowing efficient manipulation without relying on Python's native integer handling.

Algorithm Design:
Addition and Subtraction: Simple digit-by-digit processing with carry/borrow handling.
Multiplication: A grade-school algorithm extended for arbitrary precision.
Division: Iterative long-division method, returning both quotient and remainder.
Factorials: Efficient computation using iterative multiplication.

Error Handling:
Division by zero raises a clear exception.
Subtraction rejects negative results, providing clear feedback.

Extensibility:
The modular design allows easy addition of new features like non-decimal bases or rational arithmetic.

# What Makes This Solution Interesting
Precision and Scalability: Every operation handles arbitrarily large numbers without compromising correctness.
Clarity and Documentation: Thoughtful comments and structured code make the solution approachable and maintainable.
Edge-Case Handling: From handling leading zeros to robust error management, the implementation is comprehensive.
