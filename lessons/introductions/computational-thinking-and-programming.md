# Computational thinking (CT)

- Computational thinking (CT) rather than "just computer programming skills"

- Looking at a problem in a way that a computer can helo people to solve it

- Formulating problems in a way that enables us to use a computer to help solve them

- CT is something that people do recursively and abstractly

- people can't write a program without engaging in computational thinking

# CT concepts and approaches

## CT concepts

- Logic --> predicting and analysing
- Algorithms --> making steps and rules
- Decomposition --> breaking down into parts 
- Patterns --> spotting and using similarities
- Abstraction --> removing unnecessary detail
- Evaluation --> making judgement

## CT approaches

- Tinkering --> experimenting and playing
- Creating --> designing and making
- Debugging --> finding and fixing errors
- Persevering --> keeping going
- Collaborating --> working together

# Algorithms
An algorithm is a procedure for solving a problem in terms of the actions to be executed and the order in which those actions are to be executed. An algorithm is merely the sequence of steps taken to solve a problem.

## Pseudocode
Pseudocode is an artificial and informal language that helps programmers develop algorithms. Pseudocode is a "text-based" detail (algorithmic) design tool.

It consists of writing out the computer code in simple, easy-to-understand English before creating it in a specific programming language.

### Examples of pseudo code

Task: Calculate the volume of a cell <br>

- The diameter of a cell is 10 μm.
- What volume does that cell have given it is a perfect sphere?
- Use Python to do the calculation.
- Use variables for the parameters.
- Print the volume to the screen

### Pseudocode
Import the module math <br>
Define the variable(s) to be used <br>
Calculate the volume of a sphere <br>
Output result displaying the volume <br>

### Source code
from math import pi <br>
R = 10.0 <br>
V = (4.0/3.0)*pi*(R*\*3) <br>
print V <br>

Task: Write a program that asks the user for a temperature in Fahrenheit and prints out the same temperature in Celsius.

### Pseudocode:
Get user input <br>
Convert f to float
Convert f to Celsius <br>
Round f to the nearest whole number
Output message displaying Celsius temperature <br>

Example code:
f = raw_input("Please input a temperature in Farhenheit:  ")
f = float(f)
f = (f - 32) * 5.0 / 9.0
f = round(f)
print("Your temperature in Celsius is: %s." %f)


## Formatting rules for pseudocode

- As verbs, use the words Generate, Compute, Process, etc. Words such as set, reset, increment, compute, calculate, add, sum, multiply, ... print, display, input, output, edit, test , etc. with careful indentation tend to foster desirable pseudocode.
- INDENTATION in pseudocode should be identical to its implementation in a programming language. 
- Pseudocode entries SHOULD NOT BE PROSE. NO SENTENCES.
- Do not include data declarations in your pseudocode.
- But do cite variables that are initialized as part of their declarations. E.g. "initialize count to zero" is a good entry.


