# IntroductionToPython

INTRODUCTION TO PYTHON WATERLOO

# FIRST STEPS

floating point number: 
approximation of a number, like pi with only a certain number of digits, stored in a set amount of space and any number past that space are excluded, rough

Pseudocode:
code designed to be more understandable, what is made by humans for human comprehension

integer: can be writtne without fraction, no decimals. Stored exaclty. 

syntax highlighting:
This is when the text changes color as a correct term is detected. Ie Print versus print, the first would not change color because the capital P makes it unrecognizable
Correct: print(45)

syntax for operations
have one space between the number and the mathematic symbol
if one number is a floating point then the answer will also be one
add brackets for order of operations
+ addition
- subtration
/ division ( always results in floating point)
// quotient ( with whole numbers)
* multiplication
** exponent
% gives the remainder

# BUILT IN FUNCTIONS

input and output
side effects- changes made other than the output, ie printig or changing data

for more complex mathematical procedures it is name by input in parenthesies, separated by commas( same as java)

use length("x") to find # of letters in a string
concatenation: gluing two strings tobether use strings with + sign

using symbol in more than one way called operator overloading

most languages have
- fuctions that determine data tupe
- form data of different tupe
- transput input from and output to user
- wayus to request a module of related functio s

function call
instruction to use a certain mathematical operation
oka function application or function invocation

dot notation: 
input stringm then dot, then name of function
ie. "bow".upper() -> BOW
ie "bow".replace("w","y") -> "boy"

to make the output of one expression  the input of another yuou can layer and just put it in parenthesies


if you need special math
import math
then use dot notation like in java

to see all functions in a library do print(dir(___))
you can import only specific functions froma library if uyou want for storage but why
would look like this
from math import sqrt
advantage is that you dont then have to type the nae of the module before the function

more basic math functions like pow and abs do not require an import

docstring
term for info stored in a function

for a specific datat item               print(dir(97))
for all built in functions              print(dir(__builtins__))
for a function                          print(abs.__doc__)

note: the math.pow functions always prodices a floating point #

for a function input use print(input())
for a string use "" inside quotation
for an integer you can do something like print(int(input("enter a number")))
prompt string user friendly but not necessary

if you dont know what type of data you can use print(type(x))

when python does scientific notation python does e+95 instead of *10^95
if the number gets big enough or small enough gets displayed as inf(inity) or 0

fmod calculates and returns the floating point remainder of dividing x by y (%)

ceiling(x) will round x up to the the nearest integer

floor(x) will lower x to the nearest integer

strings
can be with single or double quotes when entered as long as it matches on both sides

inxed is position of a character in a string
for index remember that first position is zero

substring formed by chopping other letter s off the string

prefix -> chopping letters of the end
suffix-> chopping the letter off the beginning

substrings do not have to be engliush

blank spaces do count in the characters of a string

for a string to contain quotation marks, use the other kind to mark the stringand then the other kind on the inside or use escape characters

escape characters
print("\"Double\"quotes")
escape characters are designed to remove the ambiguity about how the other symbol is being used

if you want a backslash in a string just put two backslashes
for a new line ise \n


to determine the length of a string use function len

you can multiply a string if you want a certain numbers of copies together

to use the slice functions to chop a string into pieces is very similar to isolating a specific character 
[:5] means start at character five and discard eerything to the left
[5:] means start at character five and discard eerything to the left
[5:9] will isolate everything from 5-9

you can use - numbers if you are substracting from the end
last character is -1

truncation, math.trunc cuts off everything after the decimal

for ceiling -> math.ceil()
for floor -> math.trunc
for truncation -> math .trunc()


# storing and using information

two steps
- declaration: giving name ( and maybe type of data)
- iitialization or assignment: give the var a balue


identifier: technical name for variable name

python with variables isvery free which means harder to catch errors

all you need is name of variable equals and then value

eg x = 5

variables and constants treated in the same way so pay attention to that

capitalize constants: like in java
lowercase variables
syntax: use underscores as spaces instead of camel case

variable types not specified
to comment use # signs 

identifiers cannot 
- start with a digit
- be a reserved word like for or something that is otherwise used in the code

# CREATING FUNCTIONS

PARAMETER
the changing part in the function

ABSTRACTION
process of ignoring details and finding the common ideas

function divided into  (for y(x) = x^2)
- function name: y
- parameter: x
- function body: x^2

function headerL specifies names of function and parameters
function body: code that determines output

for example, to make a multiplication function

def total( x ,  total_number):
    return x * total_number

    return is used in most languages to specify output

    user defined functions
    functions that we create

    important syntax
    - indent four spaces
    - separate functions with blank lines before and after
    - make sure to end function header with colon

    if function not indented inthe function body it wil not detect it as such and you will get an error

    flow of control
    order in which instructions are excecuted

    names only used in a specific function is local
    names used elsewhere are global