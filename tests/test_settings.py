from core.config.settings import Settings


def test_settings_load_defaults():
    settings = Settings()

    assert settings.app_name == "Sales AI Agent API"
    assert settings.database_url.startswith("postgresql+psycopg://")
    assert settings.openai_api_key is None
    assert settings.research_provider == "mock"
