from importlib import import_module
import sys
import time
problem = sys.argv[1]
if(len(sys.argv) == 3):
    path = "./{}/sample".format(problem)
else:
    path = "./{}/in".format(problem)
solution = import_module("{}.{}".format(problem, problem))

startTime = time.time()
solution.main(path)
endTime = time.time()
print("Time taken: {}ms".format(int((endTime-startTime)*1000)))