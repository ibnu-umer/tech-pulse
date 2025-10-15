import json
import logging
from pathlib import Path




OUTPUT_FILE = Path("output/report.json")
logger = logging.getLogger(__name__)

def generate_report(processed_data):
    """
    Generates both console output and a JSON file report.
    """
    if not processed_data:
        print("[reporter] No data to report.")
        logger.info("Failed [reproter] No data to report.")
        return

    # Console summary
    print("\n=== 🧠 TechPulse Report Summary ===\n")
    for topic, items in processed_data.items():
        print(f"🔹 {topic} — {len(items)} results") # show 3 articles as preview
        for i, item in enumerate(items[:3], start=1):
            print(f"   {i}. {item['title']}")
        print()

    # Write JSON report
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(processed_data, f, indent=2, ensure_ascii=False)

    print(f"[reporter] JSON report saved → {OUTPUT_FILE.resolve()}")
    logger.info(f"Success [reporter] JSON report saved → {OUTPUT_FILE.resolve()}")
