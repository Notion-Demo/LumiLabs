from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .models import Team, User
from .database import SessionLocal

router = APIRouter()

# Dependency for getting the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a team
@router.post("/teams/")
def create_team(name: str, user_ids: list[int], db: Session = Depends(get_db)):
    team = Team(name=name)
    db.add(team)
    db.commit()
    db.refresh(team)
    
    # Add users to the team
    for user_id in user_ids:
        db_user = db.query(User).filter(User.id == user_id).first()
        if not db_user:
            raise HTTPException(status_code=404, detail=f"User with id {user_id} not found")
        team.members.append(db_user)
    db.commit()
    return team

# Get all teams
@router.get("/teams/")
def get_teams(db: Session = Depends(get_db)):
    teams = db.query(Team).all()
    return teams
