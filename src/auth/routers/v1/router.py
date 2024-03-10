from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ....users import service as user_service
from ... import service as auth_service

from typing import Annotated

from sqlalchemy.orm import Session
from ....db.database import get_db
from ....users import crud, schemas

router = APIRouter(prefix="/v1/auth",    tags=["auth"])


@router.get("/users/me/", response_model=schemas.User, description="batata")
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(user_service.get_current_active_user)]
):
    return current_user

@router.post("/tokens")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session = Depends(get_db)
) -> schemas.Token:
    user = auth_service.authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth_service.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth_service.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return schemas.Token(access_token=access_token, token_type="bearer")
