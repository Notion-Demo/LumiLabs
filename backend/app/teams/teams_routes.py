from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Team
from database import get_db

router = APIRouter()

@router.post("/")
def create_team(name: str, db: Session = Depends(get_db)):
    team = Team(name=name)
    db.add(team)
    db.commit()
    db.refresh(team)
    return team

@router.get("/")
def list_teams(db: Session = Depends(get_db)):
    return db.query(Team).all()
