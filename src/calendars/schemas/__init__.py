from .availability import Availability, AvailabilityCreate
from .calendar import Calendar, CalendarCreate
from .event import Event, EventCreate

print(f"Loaded {Availability}, {AvailabilityCreate} from {__file__}")
print(f"Loaded {Calendar}, {CalendarCreate} from {__file__}")
print(f"Loaded {Event}, {EventCreate} from {__file__}")