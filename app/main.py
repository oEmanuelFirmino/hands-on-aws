from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.settings import Settings
from app.core.settings import RootResponse, HealthResponse, ApplicationInfo, ServerInfo


def create_app() -> FastAPI:
    settings = Settings()

    app = FastAPI(title=settings.app_name, debug=settings.debug)

    app.state.settings = settings

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=settings.allowed_credentials,
        allow_methods=settings.allowed_methods,
        allow_headers=settings.allowed_headers,
    )

    @app.get("/", response_model=RootResponse)
    async def root() -> RootResponse:
        return RootResponse(
            application=ApplicationInfo(
                name=settings.app_name,
                description=settings.description,
                environment=settings.environment,
            ),
            server=ServerInfo(
                host=settings.host,
                port=settings.port,
                debug=settings.debug,
            ),
        )

    @app.get("/health", response_model=HealthResponse)
    async def health_check() -> HealthResponse:
        return HealthResponse(
            status="ok", message="O serviço está funcionando corretamente!"
        )

    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=app.state.settings.host,
        port=app.state.settings.port,
        reload=True,
    )
