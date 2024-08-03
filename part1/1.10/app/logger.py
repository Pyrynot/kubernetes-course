from datetime import datetime
import time
import hashlib
import os

log_file_path = "/shared/log.txt"
temp_file_path = "/shared/temp_log.txt"

def log_output():
    while True:
        current_timestamp = datetime.now().isoformat()
        hash_value = hashlib.sha256(current_timestamp.encode()).hexdigest()
        with open(temp_file_path, "w") as temp_file:
            temp_file.write(f"{current_timestamp}: {hash_value}")
        os.replace(temp_file_path, log_file_path)
        time.sleep(5)

if __name__ == "__main__":
    log_output()
