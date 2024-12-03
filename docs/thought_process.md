# Thought Process for BigInt Calculator

This document outlines the reasoning and approach taken while designing and implementing the BigInt calculator.

## Problem Understanding

### Objective
To implement an arbitrary-precision integer calculator from scratch, without relying on native support or external libraries. The implementation must:
1. Support fundamental operations (addition, subtraction, multiplication, division, factorial, etc.).
2. Be extensible and robust.
3. Highlight clear problem-solving and coding skills.

### Constraints
- Native data types cannot handle numbers of arbitrary size.
- Must work efficiently with inputs of varying sizes, including edge cases.

## Approach

1. **Initial Analysis**
   - Determine core functionality (e.g., basic arithmetic, factorial).
   - Identify potential edge cases (e.g., zero inputs, very large numbers, invalid inputs).

2. **Breaking Down the Problem**
   - Focus on individual operations (e.g., addition, subtraction) and implement them as standalone functions.
   - Validate functionality iteratively before integrating.

3. **Design Decisions**
   - **String Representation**: Use strings to represent numbers, as they naturally support arbitrary size and maintain precision.
   - **Manual Arithmetic**: Mimic elementary-school arithmetic to handle digit-by-digit operations.
   - **Self-Containment**: Avoid external libraries to demonstrate a ground-up solution.

4. **Testing and Validation**
   - Develop comprehensive test cases to ensure correctness.
   - Include edge cases (e.g., leading zeros, zero as input).

## Implementation Process

1. **Addition**
   - Start from the least significant digit and proceed leftwards.
   - Implement carry propagation for digit overflow.

2. **Subtraction**
   - Use digit-by-digit subtraction with borrow handling.
   - Restrict results to non-negative integers for simplicity.

3. **Multiplication**
   - Use nested loops to simulate digit-wise multiplication.
   - Store intermediate results in an array for efficient carry management.

4. **Division**
   - Implement repeated subtraction for quotient calculation.
   - Return both quotient and remainder.

5. **Factorial**
   - Use iterative multiplication to compute the factorial of large numbers.

6. **Testing**
   - Create a dedicated `test_big_int.py` file to validate all operations.
   - Include normal cases, edge cases, and stress tests for large inputs.

## Reflection

This project highlights the importance of understanding algorithms at a fundamental level. By mimicking basic arithmetic, it was possible to overcome the lack of native support for arbitrary-precision integers.

The choice to focus on depth (a robust implementation of a subset of operations) rather than breadth (attempting many features) reflects the project's goal: demonstrate problem-solving skills and deliver quality code.

## Lessons Learned

1. **Algorithm Design**: Understanding how basic arithmetic works at a low level is crucial for implementing such functionality from scratch.
2. **Error Handling**: Ensuring robust input validation prevents unexpected failures.
3. **Scalability**: Even simple algorithms can handle large inputs effectively with proper design.

## Future Scope

1. **Optimization**: Use advanced algorithms (e.g., Karatsuba multiplication) to improve performance.
2. **Advanced Features**: Support signed integers, non-decimal bases, and additional mathematical functions.
3. **Enhanced REPL**: Add support for more complex expressions and user-friendly error messages.