"""
 IntervalBit are written :
  *   : all
  6   : exact
  5-9 : range
 It is possible to put several using «,» delimiter : 5-9,12-16,18
"""

class IntervalBit():
	def __init__(self, intervalString, position):
		self.intervalString = intervalString
		self.name           = BitsDefinition.getName(position)
		self.boundary       = BitsDefinition.getBoundary(position)
		self.intervals      = self._intervalList(intervalString)
		self.duration       = BitsDefinition.getDuration(position)

	# Check if a given interger can fit in boundaries
	def doesItFit(self, timeInt):
		for bits in self.intervals:
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
			if (self.boundary[0] <= bit[0] and bit[0] <= self.boundary[1] and
				  self.boundary[0] <= bit[1] and bit[1] <= self.boundary[1]):
				intervals.append(bit)
			else:
				print(str(self), bits, "could not fit in boundary", str(self.boundary))
		return intervals

	def __str__(self):
		return "<" + self.name + ":" + self.intervalString + ">"


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
