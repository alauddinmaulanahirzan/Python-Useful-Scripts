import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")


import sys
import numpy as np
import scipy as sp
from scipy.stats import uniform
from time import time


class MatrixBench():
    def __init__(self, iters: int, size: int):
        self.iters = iters
        self.size = size
        self.average = 0
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0
        self.flops:float = 0.0

    def create_matrices(self):
        # Create num x num matrix and an num x 1 vector with random floating point numbers
        self.matrix_A = uniform.rvs(size=(self.size, self.size)).astype(np.float32)
        self.matrix_B = uniform.rvs(size=(self.size, 1)).astype(np.float32)
    
    def do_operation(self):
        # Do Floating Point Operation
        self.start_time = time()
        _ = sp.linalg.solve(self.matrix_A, self.matrix_B)
        self.end_time = time()

    def do_calculate(self):
        # Calculate Floating Point Operation per Second (FLOPS)
        self.elapsed_time = self.end_time - self.start_time
        self.num_operations = (2 / 3) * self.size **3
        self.flops = self.num_operations / self.elapsed_time
        self.average += self.flops
        
    def run(self):
        print("# Linpack-like Matrix-based Floating Point Benchmark #")
        print("# Using SciPy as Core (contains Warn: Ill-conditioned Matrix) #")
        for i in range(0, self.iters + 1):
            print(f"=> Epoch #{str(i).zfill(len(str(self.iters)))}", end="\r")
            self.create_matrices()
            self.do_operation()
            self.do_calculate()
        self.avg_flops: float = (self.average/self.iters) / 1000000
        print(f"Result : {self.avg_flops:.2f} MFLOPS")

        
def main():
    # Adjust Matrix Size
    size = 192
    # Adjust Iteration Time
    iters = 10000
    # Run Benchmark
    bench = MatrixBench(iters=iters, size=size)
    bench.run()
    
    
main()
