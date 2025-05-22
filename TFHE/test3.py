import time
import numpy as np

from concrete import fhe

def add(x, y):
    return x + y

compiler = fhe.Compiler(add, {"x": "encrypted", "y": "encrypted"})

inputset = [(2, 3), (0, 0), (1, 6), (7, 7), (7, 1), (3, 2), (6, 1), (1, 7), (4, 5), (5, 4)]

print(f"Compilation...")
circuit = compiler.compile(inputset)

print(f"Key generation...")
circuit.keygen()

t=time.time()
print(circuit.encrypt_run_decrypt(2,6))
print(f"Took {time.time()-t}s")

