import os
from datetime import datetime
from time import sleep

# LOCAL
from ElasConnect import ElasConnect
from ElasModules import ElasModules
from ElasIndex import ElasIndex
from ElasCompare import ElasCompare
from ElasPut import PutDoc

while True:
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    target_time = "2023-10-25 20:21:00"

    if current_time == target_time:
        print("It's 11:55 PM UTC. Running the provided code.")

        def check_directory(directory='logs/'):
            if not os.path.exists(directory):
                os.mkdir(directory)


        # Connect to Elastic and get data
        connector = ElasConnect().elas_connect()
        data = connector.cat.indices(index="*", format="json")
        modules = ElasModules().elas_modules
        index_data = ElasIndex(data, modules).get_index_data()

        check_directory()

        dps = ElasCompare(index_data)
        dps.compare_index()
        dps.add_tdps()
        PutDoc("grg", connector).put_doc()

        sleep(84600)