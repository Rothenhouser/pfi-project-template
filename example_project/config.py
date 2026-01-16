from pathlib import Path

from dotenv import load_dotenv

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJ_ROOT / "data"
REPORTS_DIR = PROJ_ROOT / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"

# Lade Umgebungsvariablen von einem .env File.
load_dotenv()
