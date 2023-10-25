from datetime import datetime
import pytz
import re


class ElasIndex:
    def __init__(self, data, modules):
        self.data = data
        self.modules = modules

    # Check Condition
    def _all_strings_to_check(self):
        all_strings_to_check = []

        for char in self.modules:
            if char.endswith("."):
                modified_name = char.rstrip('.')
                pattern = rf'{modified_name}\.(.*?)\-'  # Regular expression to capture sub-modules
                index_item = [item["index"] for item in self.data]
                sub_modules = set(re.findall(pattern, ' '.join(map(str, index_item))))
                combined_sub_modules = [char + i + "-" for i in sub_modules]
                for module in combined_sub_modules:
                    all_strings_to_check.append(module)
            else:
                all_strings_to_check.append(char)

        return all_strings_to_check

    # In this stage, sort the indexes and get last one.
    # format the dict with data I want and add time.
    def index_filter(self, all_strings_to_check):
        last_indices = {}

        for string in all_strings_to_check:
            indices_for_string = [
                {"index": item["index"], "store_size": item["store.size"], "pri_store_size": item["pri.store.size"]} for
                item in self.data if string in item["index"]]

            if indices_for_string:
                indices_for_string.sort(key=lambda x: x['index'])  # Sort indices alphabetically by index name
                last_index_data = indices_for_string[-1]  # Select the last index after sorting

                if last_index_data.get("pri_store_size").endswith("225b"):
                    print(f"{last_index_data['index']} - ## Skipped 225b ##")
                    continue
                elif last_index_data.get("pri_store_size").endswith("kb"):
                    print(f"{last_index_data['index']} - ## Skipped Storage Size Under 1MB.")
                    continue

                last_indices[string] = {
                    "index": last_index_data["index"],
                    "store_size": last_index_data["store_size"],
                    "pri_store_size": last_index_data["pri_store_size"],
                    "date": datetime.now().isoformat()
                }

        return last_indices

    # Main indices
    def get_index_data(self):

        all_strings_to_check = self._all_strings_to_check()
        _logs = self.index_filter(all_strings_to_check)
        return _logs
