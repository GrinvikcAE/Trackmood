
from fastapi import FastAPI, Request, status, Depends
from fastapi_users import FastAPIUsers
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError

from auth.base_config import auth_backend, fastapi_users
from auth.models import User
# from src.auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate
from comment.router import router as router_comment
# TODO: Add Celery Tasks
app = FastAPI(
    title="Trackmood"
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content=jsonable_encoder({'detail': exc.errors()}))


app.include_router(
    fastapi_users.get_auth_router(auth_backend, requires_verification=False),
    prefix="/auth/jwt",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_comment)
