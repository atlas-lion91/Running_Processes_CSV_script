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
    except psutil.NoSuchProcess:
        print(f"Error: Process with PID {process_info['pid']} does not exist anymore.")
    except psutil.AccessDenied:
        print(f"Error: Access denied to fetch details for process with PID {process_info['pid']}.")
    except psutil.ZombieProcess:
        print(f"Error: Process with PID {process_info['pid']} is a zombie process.")
    except Exception as e:
        print(f"Unexpected error: {e}")

with open('process.csv', 'w', newline='') as csvfile:
    fieldnames = ['pid', 'name', 'exe', 'cpu_percent', 'memory_percent']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)


    writer.writeheader()
    for process in all_processes:
        writer.writerow(process)

print("CSV file created successfully!")
