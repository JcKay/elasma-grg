import os
from datetime import datetime
from time import sleep

# LOCAL
from ElasConnect import ElasConnect
from ElasModules import ElasModules
from ElasIndex import ElasIndex
from ElasCompare import ElasCompare
from ElasPut import PutDoc


processing = True
while processing:
    # current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    # target_time = "2023-10-25 23:58:00"
    current_time = datetime.now()
    target_time = current_time.replace(hour=15, minute=15, second=0)

    if current_time == target_time:
        print(f"[{datetime.now().date()}]\n"
              f"It's 11:55 PM UTC. Running the provided code.")

        def check_directory(_directory):
            if not os.path.exists(_directory):
                os.mkdir(_directory)


        # Connect to Elastic and get data
        connector = ElasConnect().elas_connect()
        data = connector.cat.indices(index="*", format="json")
        modules = ElasModules().elas_modules
        index_data = ElasIndex(data, modules).get_index_data()

        directory = '/root/elasma-grg/logs/'
        check_directory(directory)

        dps = ElasCompare(index_data, directory)
        dps.compare_index()
        dps.add_tdps()
        PutDoc("grg", connector, directory).put_doc()
        processing = False
        print(f"{datetime.now()} # Processing Completed.")
