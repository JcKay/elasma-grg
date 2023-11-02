from datetime import datetime
import pytz
from ElasLogs import ElasLogs


class PutDoc:

    def __init__(self, name, connector, directory):
        self.name = name
        self.connector = connector
        self.elasLogs = ElasLogs(directory)
        self.filenames_list = self.elasLogs.file_list

    def put_doc(self):
        index_name = f"{self.name.lower()}-elasma"
        self.connector.indices.create(index=index_name, ignore=400)

        for string in self.filenames_list:
            indices = self.elasLogs.read_previous_logs(filename=string)
            doc = {
                "_timestamp": datetime.now(pytz.utc).isoformat(),
                "log_type": string,
                "index_name": indices['index'],
                "store_size": indices['store_size'],
                "pri_store_size": indices['pri_store_size'],
                "daily_pri_store_size": indices['daily_pri_store_size']
            }
            self.connector.index(index=index_name, document=doc)

        self.connector.indices.refresh(index=index_name)
        print("Documents added successfully to the index:", index_name)
