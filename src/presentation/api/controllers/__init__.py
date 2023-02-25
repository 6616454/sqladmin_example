from fastapi import APIRouter

from src.presentation.api.controllers.post import router as post_router


def setup_routes(main_router: APIRouter) -> None:
    main_router.include_router(post_router)
