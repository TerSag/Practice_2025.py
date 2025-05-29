import sys
from datetime import datetime

class Logger:
    def __init__(self, stream, time_format):
        self.stream = stream
        self.time_format = time_format

    def log(self, message):
        now = datetime.now().strftime(self.time_format)
        print(f"[{now}] {message}", file=self.stream)

out_stream = sys.stderr
time_formatter = '%Y-%m-%d %H:%M:%S'
logger = Logger(out_stream, time_formatter)

logger.log('message for logging')
