#NOTE: Daemon tasks are background tasks that run indefinitely and are not awaited. They are useful for tasks that need to run continuously, such as monitoring or logging, without blocking the main program.


import threading
import time

def monitoring_task():
    while True:
        print("Monitoring system health...")
        time.sleep(2)  # Simulate time taken to monitor


monitoring_thread = threading.Thread(target=monitoring_task, daemon=True)
monitoring_thread.start()
print("Main program is running...")
time.sleep(10)  # Simulate main program doing other work
print("Main program is exiting...") 
