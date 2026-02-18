📘 Python Arithmetic Operators & Basic Programs

This repository contains Python programs demonstrating:

Arithmetic Operators

Currency Notes Calculation

Square Root & Cube Root

Swapping Two Numbers (Different Methods)

Single Line & Multiple Assignment

1️⃣ Arithmetic Operators in Python

Arithmetic Operators are used to perform mathematical operations.

If two or more values are connected using arithmetic operators, it is called an Arithmetic Expression.

Types of Arithmetic Operators
Operator	Meaning	Example (a=10, b=3)	Output
+	Addition	a + b	13
-	Subtraction	a - b	7
*	Multiplication	a * b	30
/	Division (Float)	a / b	3.3333
//	Floor Division	a // b	3
%	Modulo (Remainder)	a % b	1
**	Exponentiation	a ** b	1000
2️⃣ Currency Notes Calculation Program

This program calculates the number of ₹500, ₹200, and ₹100 notes required for a given withdrawal amount.

Logic Used:

Floor division (//) to calculate number of notes

Modulo (%) to calculate remaining amount

Example:
If amount = 1300

Output:

500 notes = 2

200 notes = 1

100 notes = 1

3️⃣ Square Root & Cube Root Program
Square Root:
b = a ** (1/2)

Cube Root:
c = a ** (1/3)


Uses exponentiation operator **.

4️⃣ Swapping Two Numbers (Different Methods)

This project includes multiple swapping methods:

✅ Method 1: Using Temporary Variable
k = a
a = b
b = k

✅ Method 2: Python Multiple Assignment (Best Method)
a, b = b, a

✅ Method 3: Using Addition & Subtraction
a = a + b
b = a - b
a = a - b

✅ Method 4: Using Multiplication & Division
a = a * b
b = a // b
a = a // b


(Note: Not safe if one value is 0)

✅ Method 5: Using Bitwise XOR
a = a ^ b
b = a ^ b
a = a ^ b

5️⃣ Single Line & Multiple Assignment
Single Line Assignment
a = 10
b = 20

Multiple Assignment
a, b = 10, 20
