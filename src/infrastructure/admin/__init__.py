from sqladmin import Admin

from src.infrastructure.admin.models.post import PostAdmin


def setup_admin_models(admin_app: Admin) -> None:
    admin_app.add_view(PostAdmin)
