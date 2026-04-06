from datetime import datetime

def time():
    now = datetime.now()
    print(f"Current time: {now.hour}:{now.minute}:{now.second}")



time()

