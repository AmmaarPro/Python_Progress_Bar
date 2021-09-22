import sys
import time

stream = sys.stdout
for i in range(101):
    stream.write('\b' * (len(str(i) + '% Loaded') + 10))
    stream.write("Loading: " + str(i) + '% Loaded')
    stream.flush()
    time.sleep(0.3)
