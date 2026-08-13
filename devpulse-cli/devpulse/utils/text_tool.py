# devpulse/utils/text_tool.py

import csv
import json
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

def analyze_file(file_path: str):
    """Analyzes line, word, and character counts of a target text file."""
    path = Path(file_path)
    if not path.is_file():
        console.print(f"[bold red]Error:[/] File '{file_path}' does not exist.")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = len(content.splitlines())
    words = len(content.split())
    chars = len(content)

    summary = f"[bold]Lines:[/] {lines}\n[bold]Words:[/] {words}\n[bold]Characters:[/] {chars}"
    console.print(Panel(summary, title=f"File Stats: {path.name}", border_style="green", expand=False))

def convert_csv_to_json(csv_path: str, output_path: str = None):
    """Converts a CSV file into a structured JSON file."""
    src = Path(csv_path)
    if not src.is_file():
        console.print(f"[bold red]Error:[/] File '{csv_path}' not found.")
        return

    dest = Path(output_path) if output_path else src.with_suffix(".json")

    with open(src, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    with open(dest, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    console.print(f"[bold green]Success:[/] Converted '{src.name}' -> '{dest.name}' ({len(data)} rows processed).")