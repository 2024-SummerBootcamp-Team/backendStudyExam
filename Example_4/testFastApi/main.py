from datetime import timezone, datetime

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import TeamHMember
from database import SessionLocal
from typing import List
from schemas import MemberCreate, MemberResponse

app = FastAPI()

dummyData = {
    'name': []
}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "안녕하세요! TeamH 서버에 오신 것을 환영합니다!"}


@app.get("/members/", response_model=List[MemberResponse])
async def show_all_members(db: Session = Depends(get_db)):
    db_members = db.query(TeamHMember).all()
    return db_members


@app.post("/members/", response_model=MemberResponse)
async def add_member(member: MemberCreate, db: Session = Depends(get_db)):
    db_member = db.query(TeamHMember).filter(member.name == TeamHMember.name).first()
    if db_member:
        raise HTTPException(status_code=400, detail="팀원 이름이 이미 있어요!")
    new_member = TeamHMember(name=member.name, text="굿잡", created_at=datetime.now())
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member


@app.get("/members/{name}", response_model=MemberResponse)
async def get_member(name: str, db: Session = Depends(get_db)):
    db_member = None
    if db_member is None:
        raise HTTPException(status_code=404, detail="팀원 이름을 찾을 수 없어요!")
    return db_member
