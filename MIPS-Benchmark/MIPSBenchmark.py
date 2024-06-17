import numpy as np
from time import time

class MIPSBenchmark:
    def __init__(self, iters: int):
        self.iters = iters
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0
        self.total_instructions = 0
        self.mips = 0

    def ips_operation(self):
        # Run basic 7 ALU operations
        _ = np.random.randint(10) + np.random.randint(10)
        _ = np.random.randint(10) - np.random.randint(10)
        _ = np.random.randint(10) * np.random.randint(10)
        _ = np.random.randint(10) // (np.random.randint(10) + 1) # Prevent Division by Zero
        _ = np.random.choice([True, False]) & np.random.choice([True, False])
        _ = np.random.choice([True, False]) | np.random.choice([True, False])
        _ = np.random.choice([True, False]) ^ np.random.choice([True, False])

    def calculate(self):
        self.elapsed_time = self.end_time - self.start_time
        self.total_instructions = self.iters*7
        self.mips = (self.total_instructions / self.elapsed_time) / 1000000
        print(f"=> Executed {self.total_instructions} within {self.elapsed_time}\n=> Result : {self.mips:.2f} MIPS")

    def run(self):
        print("# MIPS CPU Benchmark #")
        print("# Running 7 Basic ALU Ops #")

        self.start_time = time()
        for i in range(1, self.iters+1):
            print(f"=> Running Iteration #{str(i)}", end="\r")
            self.ips_operation()
        print("\n")
        self.end_time = time()

        self.calculate()


def main():
    iters = 1000000 # Minimum 1,000,000 times
    bench = MIPSBenchmark(iters=iters)
    bench.run()


main()
