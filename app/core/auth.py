"""
Authentication Module for FastAPI Application

This module provides functionalities for user authentication
and token generation within a FastAPI application.
It utilizes JWT (JSON Web Tokens) for user authentication
and employs the Bcrypt hashing scheme for secure password handling.

Contents:
    - Dependencies
    - OAuth2 Configuration
    - Auth Class: Provides methods for user authentication
    and token generation.
    - authenticate_user Function: Authenticates users based
    on provided credentials.

Dependencies:
    - datetime: Standard library for handling date and time information.
    - timedelta: Standard library class for managing time intervals.
    - fastapi: Framework for building APIs using FastAPI.
    - OAuth2PasswordBearer: Class for handling OAuth2 token-based
    authentication.
    - JWTError: Class for handling JWT-related errors.
    - jwt: Module for encoding and decoding JSON Web Tokens.
    - CryptContext: Class for secure password hashing.
    - ALGORITHM, SECRET_KEY: Constants for JWT configuration.
    - UserInterface, User: Classes for interacting with user data.
    - TokenData, UserSchema: Classes for token data and user schema.

OAuth2 Configuration:
    - oauth2_schema: Instance of OAuth2PasswordBearer for token-based
    authentication.

Auth Class:
    This class provides methods for user authentication and token generation.

    Attributes:
        ACCESS_TOKEN_EXPIRE_MINUTES (int): Default expiration time for
        access tokens in minutes.

    Methods:
        verify_password(plain_password, hashed_password): Verify a plain
        password against its hashed representation.
        get_password_hash(password): Generate a secure hash for a password.
        create_access_token(data, expires_delta=None): Create an access token
        with optional expiration.
        get_current_user(token, user): Get the current user based on
        a provided JWT access token.
        get_current_active_user(current_user): Get the current active user
        based on the user data model.

authenticate_user Function:
    This function authenticates users based on provided credentials.

    Args:
        username (str): The user's email or username.
        password (str): The user's plain text password.

    Returns:
        Union[UserSchema, bool]: The authenticated user schema or False if
        authentication fails.
"""
from datetime import datetime, timedelta
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from app.core.settings import ALGORITHM, SECRET_KEY
from app.interfaces.prisma.users import UserInterface
from app.prisma.client.models import User

# from app.schemas.token import TokenData
from app.schemas.user import UserSchema

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/v1/auth/token")


class Auth:
    """
    This class provides methods for user authentication and token generation
    within a FastAPI application.

    Attributes:
        ACCESS_TOKEN_EXPIRE_MINUTES (int): The default expiration time for
        access tokens in minutes.

    Methods:
        verify_password(plain_password, hashed_password):
            Verify the provided plain password against its
            hashed representation.

        get_password_hash(password):
            Generate a secure hash for the provided password.

        create_access_token(data, expires_delta=None):
            Create an access token with the provided data and
            optional expiration.

        get_current_user(token, user):
            Get the current user based on the provided JWT access token.

        get_current_active_user(current_user):
            Get the current active user based on the user data model instance.
    """

    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password, hashed_password):
        """
        Verify the plain password against its hashed representation.

        Args:
            plain_password (str): The plain text password.
            hashed_password (str): The hashed password to compare against.

        Returns:
            bool: True if the passwords match, False otherwise.
        """
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        """
        Generate a secure hash for the provided password.

        Args:
            password (str): The plain text password to be hashed.

        Returns:
            str: The hashed password.
        """
        return self.pwd_context.hash(password)

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        """
        Create an access token with the provided data and optional expiration.

        Args:
            data (dict): The data to be encoded into the token.
            expires_delta (timedelta, optional): Optional
            expiration time for the token.

        Returns:
            str: The encoded JWT access token.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt

    @staticmethod
    async def get_current_user(
        token: Annotated[str, Depends(oauth2_schema)], user: UserSchema
    ):
        """
        Get the current user based on the provided token.

        Args:
            token (str): The JWT access token.
            user (UserSchema): The user schema for the current user.

        Returns:
            User: The user data model instance.

        Raises:
            HTTPException: If credentials cannot be validated.
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
            # token_data = TokenData(username=username)
        except JWTError as err:
            raise credentials_exception from err
        # user = get_user(fake_users_db, username=token_data.username)
        if user is None:
            raise credentials_exception
        return user

    @staticmethod
    async def get_current_active_user(
        current_user: Annotated[User, Depends(get_current_user)]
    ):
        """
        Get the current active user.

        Args:
            current_user (User): The current user data model instance.

        Returns:
            User: The current active user data model instance.

        Raises:
            HTTPException: If the user is inactive.
        """
        # pylint: disable=E1101
        if not current_user.is_active:
            # pylint: enable=E1101
            raise HTTPException(status_code=400, detail="Inactive user")
        return current_user


async def authenticate_user(username: str, password: str) -> UserSchema:
    """
    Authenticate a user based on provided credentials.

    Args:
        username (str): The user's email or username.
        password (str): The user's plain text password.

    Returns:
        Union[UserSchema, bool]: The authenticated user schema or False
        if authentication fails.
    """
    user = await UserInterface().user_orm.find_first(where={"email": username})

    if not Auth().verify_password(password, user.hashed_password):
        return False
    return user
