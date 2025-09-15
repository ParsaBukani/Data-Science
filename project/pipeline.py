import sys
import subprocess
import argparse
from scripts.detection_model import run_detection_model
from scripts.ocr_model import run_ocr_model

def run_script(script_module: str):
    print(f"\n▶️ Running {script_module}...")
    result = subprocess.run([sys.executable, "-m", script_module])
    if result.returncode != 0:
        print(f"❌ Script {script_module} failed with exit code {result.returncode}.")
        sys.exit(result.returncode)
    print(f"✅ Script {script_module} completed successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run full pipeline with specified Dmode and OCRmode")
    parser.add_argument("--Dmode", type=str, required=True, help="Mode to pass to run_detection_model")
    parser.add_argument("--OCRmode", type=str, required=True, help="Mode to pass to run_ocr_model")
    args = parser.parse_args()

    scripts = [
        "scripts.import_to_db",
        "scripts.feature_engineering",
        "scripts.preprocess",
        "scripts.split_data"
    ]

    for script in scripts:
        run_script(script)

    run_detection_model(mode=args.Dmode)
    run_ocr_model(mode=args.OCRmode)

    print("\n✅ Pipeline execution complete.")
