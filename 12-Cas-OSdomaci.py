import psutil

cpu_usage=psutil.cpu_percent(interval=2)
physical_cores=psutil.cpu_count(logical=False)
logical_cores=psutil.cpu_count(logical=True)
current_process=psutil.Process()
number_threads=current_process.num_threads()
print(f"CPU usage in percents: {cpu_usage}")
print(f"Number of physical cores: {physical_cores}")
print(f"Number of logical cores: {logical_cores}")
print(f"Number of threads in active processes: {number_threads}")