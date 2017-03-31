
import math
import time

class Timer:
	def __init__(self):
		self.labels = []
		self.times = [time.time()]
	def poke(self, name=''):
		self.labels.append(name)
		self.times.append(time.time())
	def report(self):
		diff_times = [self.times[i] - self.times[i-1] for i in range(1,len(self.times))]
		total_time = time.time() - self.times[0]
		all_labels = self.labels + ['total']
		all_times = diff_times + [total_time]
		return '\n'.join('%s: %.3f' % item for item in zip(all_labels, all_times))

timer = Timer()

print(len(set(a**b for a in range(2,101) for b in range(2,101))))

print(timer.report())