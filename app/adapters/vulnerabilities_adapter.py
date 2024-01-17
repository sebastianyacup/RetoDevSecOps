from flask import render_template

from scripts.json_processor import JsonProcessor
from scripts.extract_latest import get_latest_json_url

def take_latest_json():
    json_processor = JsonProcessor()
    reportes = json_processor.process_latest_json_from_file("latest_report.json")

    return render_template('vulnerabilidades.html', reportes=reportes)

def run_analysis():
    REPO_NAME = 'sebastianyacup/RetoDevSecOps'

    latest_json_url = get_latest_json_url(REPO_NAME)

    if latest_json_url:
        json_processor = JsonProcessor()
        json_processor.process_latest_json(latest_json_url)