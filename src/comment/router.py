from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert, delete
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session

from .models import comment

from .schemas import CommentCreate

router = APIRouter(
    prefix="/comment",
    tags=['Comment'],
)


@router.get("/")
async def get_comment(comment_from_user_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(comment).where(comment.c.user_id == comment_from_user_id)
        result = await session.execute(query)
        return {'status': 'success',
                'data': result.all(),
                'details': None}
    except Exception as e:
        raise HTTPException(status_code=404, detail={'status': 'error',
                                                     'message': e,
                                                     'details': None})


@router.post("/")
async def add_comment(new_comment: CommentCreate, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(comment).values(**new_comment.dict())
        await session.execute(stmt)
        await session.commit()
        return {'status': 'success'}
    except Exception as e:
        raise HTTPException(status_code=404, detail={'status': 'error',
                                                     'message': e,
                                                     'details': None})


@router.delete("/")
async def del_comment(comment_id: int, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = delete(comment).where(comment.c.id == comment_id)
        await session.execute(stmt)
        await session.commit()
        return {'status': 'success'}
    except Exception as e:
        raise HTTPException(status_code=404, detail={'status': 'error',
                                                     'message': e,
                                                     'details': None})
