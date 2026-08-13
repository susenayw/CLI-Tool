# devpulse/main.py

import argparse
from devpulse.utils.weather import fetch_weather
from devpulse.utils.text_tool import analyze_file, convert_csv_to_json

def main():
    parser = argparse.ArgumentParser(
        prog="devpulse",
        description="A high-utility CLI tool for weather data and file manipulation."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # Weather Subcommand
    weather_parser = subparsers.add_parser("weather", help="Fetch live weather report for a city")
    weather_parser.add_argument("city", type=str, help="Name of the city (e.g., Medan, Tokyo)")

    # Text Stats Subcommand
    stats_parser = subparsers.add_parser("stats", help="Get text file statistics")
    stats_parser.add_argument("file", type=str, help="Path to the text file")

    # CSV to JSON Subcommand
    convert_parser = subparsers.add_parser("convert", help="Convert CSV file to JSON")
    convert_parser.add_argument("file", type=str, help="Path to the source CSV file")
    convert_parser.add_argument("-o", "--output", type=str, help="Optional output JSON path")

    args = parser.parse_args()

    if args.command == "weather":
        fetch_weather(args.city)
    elif args.command == "stats":
        analyze_file(args.file)
    elif args.command == "convert":
        convert_csv_to_json(args.file, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()