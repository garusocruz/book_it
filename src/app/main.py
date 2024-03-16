from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..users.routers.v1.router import router as user_router_v1
from ..auth.routers.v1.router import router as auth_router_v1
from ..customers.routers.v1.router import router as customer_router_v1 
from ..places.routers.v1.router import router as place_router_v1 
from ..professionals.routers.v1.router import router as professional_router_v1
from ..schedules.routers.v1.router import router as schedule_router_v1 
from ..calendars.routes.v1 import router as calendars_router_v1

origins = [
    "http://localhost:3000"
]

app = FastAPI(docs_url="/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prefix="/api", router=auth_router_v1)
app.include_router(prefix="/api", router=user_router_v1)
app.include_router(prefix="/api", router=customer_router_v1)
app.include_router(prefix="/api", router=place_router_v1)
app.include_router(prefix="/api", router=professional_router_v1)
app.include_router(prefix="/api", router=schedule_router_v1)
app.include_router(prefix="/api", router=calendars_router_v1)