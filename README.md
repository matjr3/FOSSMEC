# Python CLI Calculator

A menu-driven command-line calculator developed using Python that supports basic arithmetic, advanced mathematical operations, trigonometric functions, number system conversions, and calculation history.

## Project Overview

The Python CLI Calculator is a terminal-based application designed to perform a wide range of mathematical calculations through a simple and interactive interface.

The project combines basic and advanced mathematical operations in a single application. It also includes file handling to store calculation history, allowing users to view and clear previous calculations.

## Features

- **Basic Arithmetic:** Addition, subtraction, multiplication, and division.
- **Advanced Operations:** Square root, cube root, exponentiation, modulus, floor division, factorial, and logarithms.
- **Trigonometric Functions:** Sine, cosine, tangent, cotangent, secant, and cosecant.
- **GCD and LCM:** Calculate the greatest common divisor and least common multiple of two integers.
- **Number System Conversion:** Convert numbers between decimal, binary, octal, and hexadecimal systems.
- **Calculation History:** Automatically saves calculations in a text file.
- **History Management:** View or clear previously stored calculations.
- **Error Handling:** Handles invalid numerical inputs, division by zero, undefined mathematical operations, and numerical overflow.
- **Interactive Menu:** Allows users to perform multiple calculations until they choose to exit.

## Available Commands

The calculator provides 18 menu options.

| Option | Operation |
|---|---|
| 1 | Addition |
| 2 | Subtraction |
| 3 | Multiplication |
| 4 | Division |
| 5 | Square Root |
| 6 | Exponentiation |
| 7 | Modulus (Remainder) |
| 8 | Floor Division |
| 9 | Factorial |
| 10 | Logarithm |
| 11 | Trigonometric Functions |
| 12 | Cube Root |
| 13 | GCD |
| 14 | LCM |
| 15 | Number System Converter |
| 16 | View Calculation History |
| 17 | Clear History |
| 18 | Exit |

### Trigonometric Functions

Option 11 provides six trigonometric functions:

1. Sine (sin)
2. Cosine (cos)
3. Tangent (tan)
4. Cotangent (cot)
5. Secant (sec)
6. Cosecant (cosec)

All trigonometric calculations accept angles in degrees.

### Number System Conversions

Option 15 supports the following conversions:

1. Decimal to Binary
2. Decimal to Octal
3. Decimal to Hexadecimal
4. Binary to Decimal
5. Octal to Decimal
6. Hexadecimal to Decimal

## Technologies Used

- **Python 3.11+** – Programming language
- **Math Module** – Mathematical functions and calculations
- **File Handling** – Storing and managing calculation history
- **VS Code** – Development environment

## Setup Instructions

### Prerequisites

Ensure Python 3.11 or later is installed on your computer.

Verify the installation using:

```bash
python --version
```

### Installation

**1. Clone the repository**

```bash
git clone <repository-url>
```

Alternatively, download the repository as a ZIP file and extract it.

**2. Navigate to the project directory**

```bash
cd <repository-folder>
```

**3. Run the calculator**

```bash
python calculator.py
```

Replace `calculator.py` with your actual Python filename if different.

No additional libraries need to be installed since the project uses Python's standard library.

## Usage Instructions

1. Run the Python program from the terminal.
2. The calculator displays a menu containing 18 options.
3. Enter the number corresponding to the required operation.
4. Provide the numerical inputs requested by the program.
5. The calculated result will be displayed in the terminal.
6. The calculation will be saved automatically in `calculation_history.txt`.
7. Select option 16 to view calculation history or option 17 to clear it.
8. Select option 18 to exit the program.

### Example 1: Addition

```text
CALCULATOR
SELECT OPERATION

1. ADDITION
2. SUBTRACT
3. MULTIPLY
4. DIVIDE
...
18. EXIT

Enter your choice (1-18): 1
Enter first number: 15
Enter second number: 10
The result of addition is: 25.0
```

### Example 2: Trigonometric Function

```text
Enter your choice (1-18): 11

SELECT TRIGONOMETRIC FUNCTION
1. SIN
2. COS
3. TAN
4. COT
5. SEC
6. COSEC

Enter your choice (1-6): 1
Enter the angle in degrees: 30
The sine is: 0.5
```

### Example 3: Number System Conversion

```text
Enter your choice (1-18): 15

SELECT NUMBER SYSTEM CONVERSION
1. Decimal to Binary
2. Decimal to Octal
3. Decimal to Hexadecimal
4. Binary to Decimal
5. Octal to Decimal
6. Hexadecimal to Decimal

Enter your choice (1-6): 1
Enter a decimal number: 25
Binary representation of 25 is: 11001
```

## Calculation History

The calculator automatically stores calculations in a file named `calculation_history.txt`.

The file is created when the program first writes a calculation or error entry.

Example:

```text
Addition: 15.0 + 10.0 = 25.0
Sine: 30.0 degrees = 0.5
Decimal to Binary: 25 = 11001
Factorial: 5 = 120
GCD: 24 and 36 = 12
```

Users can view saved calculations using option 16 and clear the entire history using option 17.

## Error Handling

The calculator includes error handling for several mathematical and input-related conditions, including:

- Division or modulus by zero
- Square root or factorial of negative numbers
- Invalid logarithmic inputs
- Undefined trigonometric functions
- Invalid numerical inputs
- Numerical overflow
- Unsupported complex results in exponentiation

Error messages are displayed to help users identify invalid operations. Many errors are also recorded in the calculation history.

## Conclusion

The Python CLI Calculator demonstrates the implementation of fundamental Python concepts such as loops, conditional statements, mathematical functions, exception handling, and file operations.

The project provides a simple and practical command-line application for performing various mathematical calculations efficiently.
