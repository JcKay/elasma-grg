import os
import json
from datetime import datetime


def log_frame(source, dps):
    source.update({"daily_pri_store_size": dps})
    return source


def tdps_frame(_source, dps):
    _source = {
        "index": "Total Daily Primary Store Size",
        "daily_pri_store_size": str(round((dps / 1024), 3)) + " GB",
        "date": datetime.now().isoformat(),
        "store_size": "None",
        "pri_store_size": "None",
    }
    return _source


class ElasLogs:
    def __init__(self, directory="logs/"):
        self.directory = directory
        self.file_list = os.listdir(directory)

    def read_previous_logs(self, filename):
        if os.path.isfile(os.path.join(self.directory, filename)):
            with open(os.path.join(self.directory, filename), 'r') as file:
                last_line = file.readlines()[-1:]
                if len(last_line) < 1:
                    return None
                else:
                    line_in_json = json.loads(last_line[0])
                    return line_in_json

    def add_to_logs(self, filename, source, dps):
        with open(os.path.join(self.directory, filename), 'a') as file:
            if filename == 'tdpss-':
                formatted_eid = tdps_frame(source, dps)
            else:
                formatted_eid = log_frame(source, dps)
            formatted_eid = json.dumps(formatted_eid)
            file.write(formatted_eid + "\n")
