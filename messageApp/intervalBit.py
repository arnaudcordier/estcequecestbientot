"""
 IntervalBit are written :
  *   : all
  6   : exact
  5-9 : range
 It is possible to put several using «,» delimiter : 5-9,12-16,18
"""

class IntervalBit():
	def __init__(self, intervalString, position):
		self._intervalString = intervalString
		self._name           = BitsDefinition.getName(position)
		self._boundary       = BitsDefinition.getBoundary(position)
		self._intervals      = self._intervalList(intervalString)
		self._duration       = BitsDefinition.getDuration(position)

	# Check if a given interger can fit in boundaries
	def doesItFit(self, timeInt):
		for bits in self._intervals:
			if (bits[0] == '*') or (bits[0] <= timeInt and timeInt <= bits[1]):
				return bits
		return None

	# Create list of intervals boundaries
	def _intervalList(self, intervalString):
		intervals = []
		for bits in intervalString.split(','):
			# all = '*'
			if (bits == '*'):
				intervals.append(['*','*'])
				continue
			bit = [int(x) for x in bits.split('-')]
			# if exact, duplicate the key
			if len(bit) == 1:
				bit.append(int(bits))
			# check if it fits in predefined boundaries
			if (self._boundary[0] <= bit[0] and bit[0] <= self._boundary[1] and
				  self._boundary[0] <= bit[1] and bit[1] <= self._boundary[1]):
				intervals.append(bit)
			else:
				print(str(self), bits, "could not fit in boundary", str(self._boundary))
		return intervals

	def __str__(self):
		return "<" + self._name + ":" + self._intervalString + ">"


class BitsDefinition():
	boundaries = ((2000,3000), (1,12),  (1,31),         (1,7),         (0,23), (0,59))
	durations  = (  365,        31,      24,             24,            60,     1)
	names      = ('Year',      'Month', 'Day of month', 'Day of week', 'Hour', 'Minute')
	
	def getBoundary(index):
		return BitsDefinition.boundaries[index-1]
	
	def getDuration(index):
		return BitsDefinition.durations[index-1]
	
	def getName(index):
		return BitsDefinition.names[index-1]
