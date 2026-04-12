#NOTE: Non-Daemon tasks are tasks that are awaited and will complete before the program exits. They are useful for tasks that need to finish their work before the program can safely exit, such as saving data or cleaning up resources.



import threading
import time

def monitoring_task():
    while True:
        print("Monitoring system health...")
        time.sleep(2)  # Simulate time taken to monitor


monitoring_thread = threading.Thread(target=monitoring_task,)
monitoring_thread.start()
monitoring_thread.start()
print("Main program is running...")
