from .availability import get_availabilities, get_availability, create_availability, delete_availability
from .calendar import get_calendars, get_calendar, create_calendar, delete_calendar
from .event import get_events, get_event, create_event, delete_event

print(f"Loaded {get_availabilities}, {get_availability}, {create_availability}, {delete_availability} from {__file__}")
print(f"Loaded {get_calendars}, {get_calendar}, {create_calendar}, {delete_calendar} from {__file__}")
print(f"Loaded {get_events}, {get_event}, {create_event}, {delete_event} from {__file__}")