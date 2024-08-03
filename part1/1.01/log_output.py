import time
import uuid
from datetime import datetime

def random_string():
    return str(uuid.uuid4())

def log_output():
    ran_str = random_string()
    while True:
        ts = datetime.now().isoformat()
        print(f"{ts}: {ran_str}")
        time.sleep(5)

if __name__ == "__main__":
    log_output()