from importlib import import_module
import sys

problem = sys.argv[1]
if(len(sys.argv) == 3):
    path = "./{}/sample".format(problem)
else:
    path = "./{}/in".format(problem)
solution = import_module("{}.{}".format(problem, problem))
solution.main(path)