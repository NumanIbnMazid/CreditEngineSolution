import json
from pathlib import Path


def insert_sorted(array, item, low=0, high=0, mid=0):
    if high == None:
        high = len(array)

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid
        if array[mid]["text"][0].lower() == item["text"][0].lower():
            # *** array insert ***
            array.insert(mid, item)
            return mid

        # Search the left half
        elif array[mid]["text"][0].lower() > item["text"][0].lower():
            return insert_sorted(array=array, item=item, low=low, high=mid-1, mid=mid)

        # Search the right half
        else:
            if mid + 1 >= len(array):
                # *** array insert ***
                array.insert(mid, item)
                return -1
            else:
                return insert_sorted(array=array, item=item, low=mid + 1, high=high, mid=mid)

    else:
        # *** array insert ***
        array.insert(mid, item)
        return -1


def simulate_city_data(originalJsonFile, newJsonFile):
    finalized_data = []

    # Opening JSON file
    f = open(originalJsonFile)

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    # Iterating through the json
    # list
    low = 0
    for i, v in enumerate(data):
        if i == 0:
            finalized_data.append({
                "id": v["name"],
                "text": v["name"]
            })
        if v["name"]:
            insert_sorted(
                array=finalized_data,
                item={"id": v["name"], "text": v["name"]},
                high=len(finalized_data)
            )

    # Closing file
    f.close()

    with open(newJsonFile, 'w') as f:
        json.dump(finalized_data, f)


# Read Path
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "staticfiles"
# original file
city_data_file = f"{STATIC_DIR}/data/world-cities.json"
# simulated file
city_data_simulated_file = f"{STATIC_DIR}/data/cities.json"
# Simulate World Cities Data in JSON
simulate_city_data(originalJsonFile=city_data_file, newJsonFile=city_data_simulated_file)
