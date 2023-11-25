from datetime import datetime

from pydantic import BaseModel


class CommentCreate(BaseModel):
    id: int
    content: str
    user_id: int
    at_date: datetime
    is_active: bool
    is_verified: bool
