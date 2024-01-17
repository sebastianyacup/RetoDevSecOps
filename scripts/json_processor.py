import json
import os
import requests

from app.infrastructure.persistence.database import save_to_database


class JsonProcessor:
    def process_latest_json(self, json_url):
        response = requests.get(json_url)
        response.raise_for_status()

        json_file_path = os.path.join(os.getcwd(), "Docs", "latest_report.json")
        with open(json_file_path, 'w') as json_file:
            json_file.write(response.content.decode('utf-8'))
        print("JSON procesado y guardado localmente.")

        save_to_database(json_file_path)

    def process_latest_json_from_file(self, json_filename):
        json_file_path = os.path.join(os.getcwd(), "Docs", json_filename)
        with open(json_file_path, 'r') as json_file:
            reportes = json.load(json_file)

        return reportes
