import asyncio
import argparse
from dotenv import load_dotenv
import traceback, logging, os
from core.fetcher import fetch_all
from core.processor import process_data
from core.reporter import generate_report
from datetime import datetime


os.makedirs("output/", exist_ok=True)

logging.basicConfig(
    filename="output/techpulse.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s",
    filemode="a"
)

# Create a seperation for each time script runs
logger = logging.getLogger(__name__)
logger.info("\n" + "="*80)
logger.info(f"New Session Started at {datetime.now().isoformat()}")



def parse_args():
    parser = argparse.ArgumentParser(description="Tech Pulse -- Tech Aggregator")
    parser.add_argument("--topics", type=str, required=True,
                        help="Comma seperated list of topics. eg. 'AI, 'Tesla'")
    parser.add_argument("--limit", type=int, default=5,
                        help="Max items per source.")
    return parser.parse_args()


async def main():
    load_dotenv()
    args = parse_args()
    topics = [t.strip() for t in args.topics.split(",")]
    limit = args.limit

    # Fetch data
    try:
        raw_data = await fetch_all(topics, limit=limit)
        processed = process_data(raw_data)
        generate_report(processed)
    except Exception as err:
        print(f"Error while fetching data: {err}")
        logging.error(f"Error while fetching data: {err} \n{traceback.format_exc()}")


if __name__ == "__main__":
    asyncio.run(main())
