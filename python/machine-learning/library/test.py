from yuri_util import info, error, Utils
import numpy as np
import time

start = time.perf_counter_ns()

for i in range(10):
  info() << np.tile(2, (2, 2))**2

end = time.perf_counter_ns()

info() << "time: " << round((end - start) / 1000, 2)  << "ms"

def action(fun: callable, *args):
  fun(*args)

def test(a, b):
  info() << a + b

Utils.action(test, 1, 2)