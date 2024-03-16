from .crud.availability import get_availabilities, get_availability, create_availability, delete_availability
from .crud.calendar import get_calendars, get_calendar, create_calendar, delete_calendar
from .crud.event import get_events, get_event, create_event, delete_event
from .models import availability as models_availability, calendar as models_calendar, event as models_event
from .routes.v1 import availabilities as router_availabilities, calendars as router_calendars, events as router_events
from .schemas import availability as schemas_availability, calendar as schemas_calendar, event as schemas_event

print(f"Loaded {get_availabilities}, {get_availability}, {create_availability}, {delete_availability} from {__file__}")
print(f"Loaded {get_calendars}, {get_calendar}, {create_calendar}, {delete_calendar} from {__file__}")
print(f"Loaded {get_events}, {get_event}, {create_event}, {delete_event} from {__file__}")

print(f"Loaded {router_availabilities}, {router_calendars}, {router_events},from {__file__}")
print(f"Loaded {models_availability}, {models_calendar}, {models_event},from {__file__}")
print(f"Loaded {schemas_availability}, {schemas_calendar}, {schemas_event},from {__file__}")