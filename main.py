# Recursive Python function to solve the tower of hanoi
import time
def TowerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print ("Move disk 1 from source", source, "to destination", destination)
        return
    TowerOfHanoi(n - 1, source, auxiliary, destination)
    print ("Move disk", n, "from source", source, "to destination", destination)
    TowerOfHanoi(n - 1, auxiliary, destination, source)


# Driver code
n = 2
tid = time.time()
TowerOfHanoi(n, 'A', 'B', 'C')
# A, C, B are the name of rods
mtid = time.time() - tid
print(mtid)

# Contributed By Dilip Jain