from fastapi import FastAPI
from .auth import router as auth_router
from .tasks import router as task_router
from .teams import router as team_router

app = FastAPI()

# Include routers for different API functionality
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(task_router, prefix="/tasks", tags=["tasks"])
app.include_router(team_router, prefix="/teams", tags=["teams"])
