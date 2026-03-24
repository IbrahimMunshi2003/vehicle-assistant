import mongoengine

mongoengine.connect(
    db="vehicle_assistant",
    host="your_mongodb_connection_string"
)