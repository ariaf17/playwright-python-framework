# utils/config.py
import os
from dotenv import load_dotenv

load_dotenv()  # loads .env if present

BASE_URL = os.getenv("BASE_URL", "https://example.com/").strip()

if not BASE_URL.startswith("http"):
    raise ValueError(f"BASE_URL looks invalid: {BASE_URL!r}")
