from fastapi import APIRouter
from models.user_model import User
from views.user_view import UserCrud

router = APIRouter(tags=["User"])


@router.get("/")
async def get_all_users():
    users = await UserCrud().get_all_users()
    return {"users": users}


@router.get("/{user_id}")
async def get_single_user(user_id: int):
    """
    @summary: Get a single user
    @param user_id: The id of the user
    @type user_id: int
    @return: The user

    """
    user = await UserCrud().get_user(user_id)
    return {"user": user}


@router.patch("/{user_id}")
async def update_user(user_id: int, user: User):
    """
    @summary: Update a user
    @param user_id: The id of the user
    @type user_id: int
    @param user: The user to update
    @type user: UserSchema
    @return: The user

    """
    user = await UserCrud().update_user(user_id, user)
    return {"user": user}
