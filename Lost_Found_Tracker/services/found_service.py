from config.db_config import get_database

db = get_database()
found_collection = db["found_items"]

def report_found_item(finder_name, item_name, description, location, date, contact):
    found_item = {
        "finder_name": finder_name,
        "item_name": item_name,
        "description": description,
        "location_found": location,
        "date_found": date,
        "contact": contact,
        "claimed_by": None
    }
    found_collection.insert_one(found_item)
    return "Found item reported successfully!"

def get_found_items():
    return list(found_collection.find({}, {"_id": 0}))
