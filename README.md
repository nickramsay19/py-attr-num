# Numeric arithmetic in plain English | py-attr-num
> Created by Nicholas Ramsay

This is an abomination of a python class, please don't actually use it. Here's what it does:

```py
from AttrNum import AttrNum

# create a very useful attr num instance that performs arithmetic in plain english
n = AttrNum(5)
assert n.plus_1() == 6
assert n.plus_one() == 6 # or use english numbers
assert n.PLUS_oNe() == 6 # upper or lower case is allowed
assert n._____plus______one_____() == 6 # very forgiving with spaces
assert n.plus_one == 6 # can be an attribute as well (harder than it looks)

# lets see its true power!
assert AttrNum(5).plus_one_minus_two_multiplied_by_six() == -6 # allows some grammar
assert AttrNum(100).divided_by_ten_and_multiplied_with_three_and_then_added_with_twenty() == 50 # "by", "and", "with", "to", "then"
assert AttrNum(88).divided_by_eight_is_equal_to_eleven() == True # can evaluate boolean expressions

# supports floating point arithmetic
assert AttrNum(1).multiplied_by_zero_point_three_three_three() == 0.333
assert AttrNum(1).percent_of_two_hundred() == 2

# accepts string values
assert AttrNum('five') == 5
assert AttrNum('five hundred') == 500 # we can use spaces instead of underscores in a string if we want

# all comparisons supported by functools.total_ordering
assert AttrNum('one plus two') == AttrNum('four minus one')
assert AttrNum('one plus two') <= AttrNum('four minus one plus one')
assert AttrNum('one plus two') < AttrNum('four minus one plus one')
assert AttrNum('two hundred') >= AttrNum("one hundred")
assert AttrNum('two hundred') > AttrNum("one hundred")

# and most importantly:
assert AttrNum('tree fiddy') == 3.50

# all assertions pass! what a very useful class!
```