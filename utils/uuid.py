import datetime
import uuid


def generate_uuid():
    return str(uuid.uuid4())


def get_current_date_time():
    return datetime.datetime.now()
