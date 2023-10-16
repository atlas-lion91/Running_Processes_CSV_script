import os
import psutil
import csv

# Retreive all running processes
all_processes = []
for process in psutil.process_iter():
    try:
        # Retrieve process details as a named tuple
        process_info = process.as_dict(attrs=['pid', 'name', 'exe', 'cpu_percent', 'memory_percent'])
        
        # Append to the list of all processes
        all_processes.append(process_info)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

with open('process.csv', 'w', newline='') as csvfile:
    fieldnames = ['pid', 'name', 'exe', 'cpu_percent', 'memory_percent']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


    writer.writeheader()
    for process in all_processes:
        writer.writerow(process)

print("CSV file created successfully!")
