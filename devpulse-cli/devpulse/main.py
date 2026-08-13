# devpulse/main.py

import argparse
import json
from devpulse.utils.weather import fetch_weather_data
from devpulse.utils.text_tool import analyze_file, convert_csv_to_json

def main():
    parser = argparse.ArgumentParser(prog="devpulse")
    subparsers = parser.add_subparsers(dest="command")

    # Weather Subcommand
    weather_parser = subparsers.add_parser("weather")
    weather_parser.add_argument("city", type=str)
    weather_parser.add_argument("--json", action="store_true")

    # Stats Subcommand
    stats_parser = subparsers.add_parser("stats")
    stats_parser.add_argument("file", type=str)
    stats_parser.add_argument("--json", action="store_true")

    args = parser.parse_args()

    if args.command == "weather":
        data, err = fetch_weather_data(args.city)
        if args.json:
            print(json.dumps({"data": data, "error": err}))
        else:
            print(data if data else err)

    elif args.command == "stats":
        # Read file stats
        try:
            from pathlib import Path
            path = Path(args.file)
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            result = {
                "fileName": path.name,
                "lines": len(content.splitlines()),
                "words": len(content.split()),
                "chars": len(content)
            }
            if args.json:
                print(json.dumps(result))
            else:
                print(result)
        except Exception as e:
            if args.json:
                print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()