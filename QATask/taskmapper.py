import QUANTAXIS as QA
import requests

"""
job:

1. map task to target host
2. target host's webserver recv task ==> make a temp file
3. temp file save to database waiting for QAUnicorn to  scan and run
"""

class QA_Task():
    def __init__(self, taskname, content):
        self.taskname = taskname
        self.content = content

    def map(self, ip, port='8010'):
        r = requests.post(
            'http://{}:{}/command/filemapper?program=python'.format(ip, port),
            {'content': self.content})
