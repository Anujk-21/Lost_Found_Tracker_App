from config.db_config import get_database

db = get_database()
lost_collection = db["lost_items"]
found_collection = db["found_items"]

def match_lost_found():
    lost_items = list(lost_collection.find({}, {"_id": 0}))
    found_items = list(found_collection.find({}, {"_id": 0}))

    matches = []
    for lost in lost_items:
        for found in found_items:
            if lost["item_name"].lower() == found["item_name"].lower():
                matches.append({
                    "Lost Item": lost["item_name"],
                    "Lost By": lost["user_name"],
                    "Lost Location": lost["location_lost"],
                    "Found By": found["finder_name"],
                    "Found Location": found["location_found"],
                    "Contact": found["contact"]
                })
    
    return matches
