from models import EventPlace
from sqlalchemy.sql import asc, func

def upsert_event_place(admin_unit_id, organizer_id, name):
    result = EventPlace.query.filter(and_(EventPlace.name == name, EventPlace.admin_unit_id == admin_unit_id, EventPlace.organizer_id == organizer_id)).first()
    if result is None:
        result = EventPlace(name = name, admin_unit_id=admin_unit_id, organizer_id=organizer_id)
        result.location = Location()
        db.session.add(result)

    return result

def get_event_places(admin_unit_id):
    return EventPlace.query.filter(EventPlace.admin_unit_id==admin_unit_id).order_by(func.lower(EventPlace.name)).all()