import asyncio
import argparse
from dotenv import load_dotenv
import os, traceback
from core.fetcher import fetch_all
from core.processor import process_data
from core.reporter import generate_report



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
        traceback.print_exc()



if __name__ == "__main__":
    asyncio.run(main())
