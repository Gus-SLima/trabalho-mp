from velha import Velha
assert Velha([[2,2,2],[2,2,2],[1,1,1]])==-2
assert Velha([[1,1,1],[2,2,2],[1,1,1]])==-2
assert Velha([[1,1,1],[1,2,1],[2,2,2]])is None
assert Velha([[1,0,1],[2,2,0],[2,1,0]])is None
assert Velha([[1,1,1],[2,1,2],[2,2,1]])==1
assert Velha([[2,2,2],[1,2,1],[0,1,1]])==2
