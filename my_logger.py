import sys
import datetime

def log(message: str):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    error_message = f"[{timestamp}] {message}\n"
    sys.stderr.write(error_message)

if __name__ == "__main__":
    log("Це повідомлення логу йде y stderr.") 