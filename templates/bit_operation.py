# use ord() to get the ordinal value of charactors
print([ord(c) for c in 'money'])

#  check the bit-length of any integer number
print((12).bit_length())

# Bitwise operation
# and &
"""
For each pair of bits occupying the same position in the two numbers, 
it returns a one only when both bits are switched on, i.e. 1
(a&b)_i = (a*b)_i
"""

# or |
"""
For each corresponding pair of bits, it returns a one if at least one of them is switched on.
(a|b)_i = a_i + b_i - a_i * b_i
"""

# xor ^
"""
For each corresponding pair of bits, it returns a one if only one of them is switched on.
(a^b)_i = (a_i + b_i)mod 2
"""

# Not ~
"""
turns zeros to ones and turns ones to zeros.
a_i = 1 - a_i

WARNING: used with unsigned integers.
if signed integers:
~156 = -157
~156 &255 = 99
bin(156)
'0b10011100'
bin(-157)
'-0b10011101'
~156
-157
bin(255)
'0b11111111'
~156&255
99
bin(99)
'0b1100011'
"""
"""
x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). 
This is the same as multiplying x by 2**y.
x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
x & y
Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.
x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.
~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1. 
This is the same as -x - 1.
x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that bit in y is 0, 
and it's the complement of the bit in x if that bit in y is 1.

How negative number is handled.
https://stackoverflow.com/questions/46044936/bitwise-and-between-negative-and-positive-numbers
"""