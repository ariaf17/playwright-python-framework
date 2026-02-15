import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com/").strip()
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME", "").strip()
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD", "").strip()

if not BASE_URL.startswith("http"):
    raise ValueError(f"BASE_URL looks invalid: {BASE_URL!r}")

if not SAUCE_USERNAME or not SAUCE_PASSWORD:
    raise ValueError("Missing SAUCE_USERNAME / SAUCE_PASSWORD in environment (.env).")
