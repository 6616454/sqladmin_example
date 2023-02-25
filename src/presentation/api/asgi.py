import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from src.config import load_config
from src.infrastructure.db.main import create_engine, create_pool
from src.presentation.admin.main import build_admin_app
from src.presentation.api.controllers import setup_routes
from src.presentation.api.di import setup_di


def build_app() -> FastAPI:
    config = load_config()

    app = FastAPI(title=config.api.title, default_response_class=ORJSONResponse)

    engine = create_engine(db_config=config.db)

    setup_routes(app.router)
    setup_di(app, create_pool(engine))

    build_admin_app(app=app, engine=engine)

    return app


if __name__ == "__main__":
    uvicorn.run(app="src.presentation.api.asgi:build_app", factory=True)
