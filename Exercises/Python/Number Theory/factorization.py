import sympy as sp 
import time
p = 45654411562154846
q = 45654871561154841
print("working...")
start = time.perf_counter()
N = p*q
end = time.perf_counter()
print("factors:",sp.factorint(N)) 
print("total time taken: ",end-start) # 6 seconds; the prime numbers will be FAR bigger than this. 



