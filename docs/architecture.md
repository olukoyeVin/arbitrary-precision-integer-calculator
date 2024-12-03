# Architecture of the BigInt Calculator

This document describes the architecture of the `BigInt` class, which provides arbitrary-precision integer operations, and the REPL interface that allows interactive usage.

## Overview

The `BigInt` calculator is designed to overcome the limitations of fixed-precision integers in programming languages. It enables operations on integers of arbitrary size without relying on libraries or native support for such functionality.

### Key Components

1. **BigInt Class**
   - Encapsulates all operations for arbitrary-precision integers.
   - Implements addition, subtraction, multiplication, division (quotient and remainder), factorial, and comparison.
   - Ensures correctness and performance with algorithms inspired by elementary arithmetic.

2. **Interactive REPL**
   - Provides a command-line interface for users to interact with the calculator.
   - Parses user input and invokes appropriate operations on `BigInt` instances.

---

## `BigInt` Class Design

### Attributes
- `value`: A string representing the non-negative integer in base 10. This ensures no overflow regardless of the size of the number.

### Core Algorithms
#### 1. **Addition**
   - Performs digit-wise addition from the least significant digit to the most significant.
   - Handles carry propagation efficiently.

#### 2. **Subtraction**
   - Implements digit-wise subtraction with borrow handling.
   - Only supports non-negative results (as negative integers are out of scope for this implementation).

#### 3. **Multiplication**
   - Uses a nested loop to compute the product of individual digits, propagating carries as needed.
   - Stores intermediate results in an array for efficient carry management.

#### 4. **Division**
   - Uses repeated subtraction to compute the quotient and remainder.
   - Handles division by zero explicitly by raising an exception.

#### 5. **Factorial**
   - Uses iterative multiplication to compute the factorial of a number.
   - Efficiently handles large results using the existing multiplication logic.

#### 6. **Comparison**
   - Compares two `BigInt` values based on string length and lexicographic order.

### Error Handling
- Input validation ensures only non-negative integers are accepted.
- Explicit handling for exceptional cases such as division by zero and negative results from subtraction.

---

## REPL Design

The Read-Eval-Print Loop (REPL) serves as an interface for the `BigInt` class:
- **Input Parsing**: Recognizes mathematical operators (`+`, `-`, `*`, `/`, `!`) and splits operands.
- **Execution**: Maps user commands to corresponding `BigInt` methods.
- **Output Formatting**: Displays results in a human-readable format, including quotient and remainder for division.

---

## Design Principles

1. **Simplicity**:
   - The `BigInt` class is self-contained and does not rely on external libraries.
   - Algorithms are straightforward and easy to understand.

2. **Scalability**:
   - Supports arbitrarily large numbers without performance degradation for typical use cases.

3. **Robustness**:
   - Extensive input validation and error handling.
   - Includes comprehensive unit tests for all operations.

4. **Reusability**:
   - The `BigInt` class can be used independently in other projects requiring arbitrary-precision integers.

---

## Limitations
- Only supports non-negative integers.
- Advanced operations (e.g., logarithms, non-decimal bases) are out of scope for this implementation.

## Future Improvements
- Extend support to signed integers.
- Optimize multiplication using algorithms like Karatsuba.
- Add support for advanced mathematical functions (e.g., power, roots).
