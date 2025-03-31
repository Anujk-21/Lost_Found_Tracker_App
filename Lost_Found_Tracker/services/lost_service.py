from config.db_config import get_database

db = get_database()
lost_collection = db["lost_items"]

def report_lost_item(user_name, item_name, description, location, date):
    lost_item = {
        "user_name": user_name,
        "item_name": item_name,
        "description": description,
        "location_lost": location,
        "date_lost": date,
        "status": "Lost"
    }
    lost_collection.insert_one(lost_item)
    return "Lost item reported successfully!"

def get_lost_items():
    return list(lost_collection.find({}, {"_id": 0}))
