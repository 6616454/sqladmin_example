from fastapi import APIRouter, Depends

from src.business_logic.services.posts_get import PostsGetService
from src.presentation.api.di.providers.services import posts_get_service

router = APIRouter(
    prefix='/posts',
    tags=['posts']
)


@router.get('/')
async def get_posts(service: PostsGetService = Depends(posts_get_service)):
    return await service.execute()
