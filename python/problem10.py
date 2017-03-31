
import math
import time
import numpy as np

class Timer:
	def __init__(self):
		self.labels = []
		self.times = [time.time()]
	def poke(self, name=''):
		self.labels.append(name)
		self.times.append(time.time())
	def report(self):
		diff_times = [self.times[i] - self.times[i-1] for i in range(1,len(self.times))]
		total_time = sum(diff_times)
		all_labels = self.labels + ['total']
		all_times = diff_times + [total_time]
		return '\n'.join('%s: %.3f' % item for item in zip(all_labels, all_times))

timer = Timer()

maximum = 2000000

is_prime = np.full(maximum, True)
is_prime[0] = False
is_prime[1] = False

timer.poke('create array')

for factor in range(2, int(math.sqrt(maximum))+1):
	if is_prime[factor]:
		is_prime[factor*factor::factor] = False

timer.poke('perform sieve')

print(np.sum(np.arange(maximum)[is_prime]))

timer.poke('sum primes')

print(timer.report())