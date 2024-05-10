# Benchmarking Class

This file contains Benchmarking class used to obtain process performance such as **CPU Percent**, **Memory Usages**, and **Processing Time**.

## Avaiable Methods
* __init__() : automatically obtain your PID and intialize Process vars
* get_cpu_percent() : return **CPU Usage** in percent
* get_memory_text_usage() : return **Memory Usage** for **text** in MB
* get_memory_data_usage() : return **Memory Usage** for **data** in MB
* get_memory_rss_usage() : return **Memory Usage** for **Resident Set Size** in MB
* get_memory_vms_usage() : return **Memory Usage** for **Virtual Memory Size** in MB
* set_start_time() : set **start time**
* set_end_time() : set **end time**
* get_processing_time() : get subtraction from **end time** and **start time**
