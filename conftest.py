from __future__ import annotations

from pathlib import Path
import pytest

from utils.config import BASE_URL


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


def pytest_configure(config: pytest.Config) -> None:
    # Ensure reports directories exist
    Path("reports/screenshots").mkdir(parents=True, exist_ok=True)
    Path("reports/traces").mkdir(parents=True, exist_ok=True)
