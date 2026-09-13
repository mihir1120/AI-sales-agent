from fastapi import FastAPI

from core.config.settings import get_settings
from core.schemas.health import HealthResponse
from apps.api.app.routes.research import router as research_router


settings = get_settings()

app = FastAPI(title=settings.app_name)
app.include_router(research_router)


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok", service=settings.app_name)
