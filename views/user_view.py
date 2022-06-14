from fastapi import Depends, HTTPException, status
from schemas.user_schema import UserSchema
from sqlalchemy.orm import Session

from views import get_db


class UserCrud:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def get_user(self, user_id: int):
        user = await self.db.query(UserSchema).filter(UserSchema.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    async def update_user(self, user_id: int, user: UserSchema):
        user_to_update = await self.db.query(UserSchema).filter(UserSchema.id == user_id).first()
        if user_to_update is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        user_to_update.firstname = user.firstname
        user_to_update.lastname = user.lastname
        user_to_update.username = user.username
        user_to_update.email = user.email
        await self.db.commit()
        return user_to_update

    async def delete_user(self, user_id: int):
        user_to_delete = await self.db.query(UserSchema).filter(UserSchema.id == user_id).first()
        if user_to_delete is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        self.db.delete(user_to_delete)
        await self.db.commit()
        return user_to_delete

    async def get_all_users(self):
        users = await self.db.query(UserSchema).all()
        return users
