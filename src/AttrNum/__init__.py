from __future__ import annotations
import re
import functools

class _CallableFloat(float):
    def __new__(cls, value):
        FAKE_FLOAT_CLASS = float.__new__(cls, value)
        FAKE_FLOAT_CLASS.__instancecheck__ = lambda slf, instance: issubclass(float, type(instance))
        FAKE_FLOAT_CLASS.__subclasscheck__ = lambda slf, subclass: issubclass(float, subclass)
        return FAKE_FLOAT_CLASS
        
    def __call__(self):
        return float(self)

@functools.total_ordering
class AttrNum:
	@staticmethod
	def __parse(expr: str):
		tokens: list[str] = re.split('_| ', expr.lower())
		
		for i in range(len(tokens)):
			tokens[i] = tokens[i].replace('by', '') # e.g "six_divided_by_four" -> "6/4"
			tokens[i] = tokens[i].replace('with', '')
			tokens[i] = tokens[i].replace('to', '')
			tokens[i] = tokens[i].replace('is', '')
			tokens[i] = tokens[i].replace('and', '')
			tokens[i] = tokens[i].replace('then', '')
			tokens[i] = tokens[i].replace('plus', '+')
			tokens[i] = tokens[i].replace('added', '+')
			tokens[i] = tokens[i].replace('add', '+')
			tokens[i] = tokens[i].replace('minus', '-')
			tokens[i] = tokens[i].replace('negative', '-')
			tokens[i] = tokens[i].replace('subtract', '-')
			tokens[i] = tokens[i].replace('times', '*')
			tokens[i] = tokens[i].replace('multiply', '*')
			tokens[i] = tokens[i].replace('multiplied', '*')
			tokens[i] = tokens[i].replace('divided', '/')
			tokens[i] = tokens[i].replace('divide', '/')
			tokens[i] = tokens[i].replace('squared', '**float(2.0)')
			tokens[i] = tokens[i].replace('point', '.')
			tokens[i] = tokens[i].replace('dot', '.')
			tokens[i] = tokens[i].replace('percent', '*float(0.01)')
			tokens[i] = tokens[i].replace('of', '*')
			tokens[i] = tokens[i].replace('ten', '10')
			tokens[i] = tokens[i].replace('eleven', '11')
			tokens[i] = tokens[i].replace('twelve', '12')
			tokens[i] = tokens[i].replace('thirteen', '13')
			tokens[i] = tokens[i].replace('fourteen', '14')
			tokens[i] = tokens[i].replace('fifteen', '15')
			tokens[i] = tokens[i].replace('sixteen', '16')
			tokens[i] = tokens[i].replace('seventeen', '17')
			tokens[i] = tokens[i].replace('eighteen', '18')
			tokens[i] = tokens[i].replace('nineteen', '19')
			tokens[i] = tokens[i].replace('twenty', '20')
			tokens[i] = tokens[i].replace('hundred', '00')
			tokens[i] = tokens[i].replace('zero', '0')
			tokens[i] = tokens[i].replace('one', '1')
			tokens[i] = tokens[i].replace('two', '2')
			tokens[i] = tokens[i].replace('three', '3')
			tokens[i] = tokens[i].replace('four', '4')
			tokens[i] = tokens[i].replace('five', '5')
			tokens[i] = tokens[i].replace('six', '6')
			tokens[i] = tokens[i].replace('seven', '7')
			tokens[i] = tokens[i].replace('eight', '8')
			tokens[i] = tokens[i].replace('nine', '9')
			tokens[i] = tokens[i].replace('equals', '==')
			tokens[i] = tokens[i].replace('equal', '==')

			tokens[i] = tokens[i].replace('tree', '3')
			tokens[i] = tokens[i].replace('fiddy', '.5')

			tokens[i] = tokens[i].replace('pi', 'float(3.1415926)')
			tokens[i] = tokens[i].replace('e', 'float(2.71828182)')

		joined = ''.join(tokens)

		# convert each integer substring with a float conversion
		with_floats = re.sub("(?<!\.|\d)(\d+)(?!\.|\d)", "float(\g<1>)", joined)

		# replace all immediately adjacent numbers with an implicit multiplication
		with_impl_mults = re.sub("(float\(\d+(?:\.\d+)?\))(float\(\d+(?:\.\d+)?\))", "\g<1>*\g<2>", with_floats)

		return with_impl_mults

	def __init__(self, val):
		if isinstance(val, int) or isinstance(val, float):
			self._val = float(val)
		elif isinstance(val, str):
			self._val = float(eval(AttrNum.__parse(val)))
		else:
			raise TypeError('\"val\" must be of type \"int\", \"float\" or \"str\".')

	def __getattr__(self, attr: str) -> float:
		return _CallableFloat(eval(str(self._val) + AttrNum.__parse(attr)))

	def __eq__(self, other: AttrNum | int) -> bool:
		if isinstance(other, AttrNum):
			return self._val == other._val
		elif isinstance(other, int) or isinstance(other, float):
			return self._val == float(other)
		else:
			raise TypeError('Can only compare AttrNum objects to integers, floats or AttrNum objects')

	def __lt__(self, other: AttrNum | int) -> bool:
		if isinstance(other, AttrNum):
			return self._val < other._val
		elif isinstance(other, int) or isinstance(other, float):
			return self._val < float(other)
		else:
			raise TypeError('Can only compare AttrNum objects to integers, floats orr AttrNum objects')





