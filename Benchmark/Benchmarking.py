import psutil
import time
import os

class Benchmarking:
    def __init__(self):
        self.pid = os.getpid()
        self.proc = psutil.Process(self.pid)

    def get_cpu_percent(self):
        self.cpu_percent = self.proc.cpu_percent()
        return self.cpu_percent

    def get_memory_text_usage(self):
        self.memory_text = self.proc.memory_full_info().text / 1024 / 1024
        return self.memory_text
    
    def get_memory_data_usage(self):
        self.memory_data = self.proc.memory_full_info().data / 1024 / 1024
        return self.memory_data

    def get_memory_rss_usage(self):
        self.memory_rss = self.proc.memory_full_info().rss / 1024 / 1024
        return self.memory_rss
    
    def get_memory_vms_usage(self):
        self.memory_vms = self.proc.memory_full_info().vms / 1024 / 1024
        return self.memory_vms

    def set_start_time(self):
        self.start = time.time()

    def set_end_time(self):
        self.end = time.time()

    def get_processing_time(self):
        self.proc_time = self.end - self.start
        return self.proc_time
    
# Main Script Here
def main():
    # Create Object for Benchmark
    benchmark = Benchmarking()
    # Performance Benchmark
    cpu_perc = benchmark.get_cpu_percent() # Call Twice to Avoid 0. Always Call to Get Latest CPU
    cpu_perc = benchmark.get_cpu_percent()
    memory_text = benchmark.get_memory_text_usage()
    memory_data = benchmark.get_memory_data_usage()
    memory_rss = benchmark.get_memory_rss_usage()
    memory_vms = benchmark.get_memory_vms_usage()
    # Processing Time Benchmark
    start_time = benchmark.set_start_time()
    time.sleep(5)
    end_time = benchmark.set_end_time()
    # Get Processing Time
    processing_time = benchmark.get_processing_time()
    # Display Result
    info: str = f"""Process ID : {benchmark.pid}
CPU Usage : {cpu_perc}%
Memory Text : {memory_text} MB
Memory Data : {memory_data} MB
Memory RSS : {memory_rss} MB
Memory VMS : {memory_vms} MB
Processing Time : {processing_time}s"""
    print(info)
    
if __name__ == "__main__":
    main()
