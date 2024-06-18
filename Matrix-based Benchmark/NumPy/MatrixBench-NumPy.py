import numpy as np
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
        self.matrix_A = np.random.rand(self.size, self.size).astype(np.float32)
        self.matrix_B = np.random.rand(self.size).astype(np.float32)
    
    def do_operation(self):
        # Do Floating Point Operation
        self.start_time = time()
        _ = np.linalg.solve(self.matrix_A, self.matrix_B)
        self.end_time = time()

    def do_calculate(self):
        # Calculate Floating Point Operation per Second (FLOPS)
        self.elapsed_time = self.end_time - self.start_time
        self.num_operations = (2 / 3) * self.size **3
        self.flops = self.num_operations / self.elapsed_time
        self.average += self.flops
        
    def run(self):
        print("# Linpack-like Matrix-based Floating Point Benchmark #")
        print("# Using NumPy as Core #")
        print(f"# Matrix Size : {self.size} #")
        print(f"# Iterations : {self.iters} #")
        print("# Please Wait #")
        
        for i in range(1, self.iters+1):
            self.create_matrices()
            self.do_operation()
            self.do_calculate()
        
        self.avg_flops: float = (self.average/self.iters) / 1000000
        print(f"=> Result : {self.avg_flops:.2f} MFLOPS")


def main():
    # Adjust Matrix Size
    size = 512
    # Adjust Iteration Time
    iters = 1000
    # Run Benchmark
    bench = MatrixBench(iters=iters, size=size)
    bench.run()
    
    
main()
