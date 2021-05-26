import json
import os
from os import path
from pathlib import Path

import requests
from datetime import date, timedelta
from dotenv import load_dotenv
from src.shared.constants import IngestionConstants


class Ingestion :
    """
    class to ingest data from the api to local disk
    """

    def __init__(self) :
        load_dotenv()
        pass

    def get_historical_data_api_url(self, api_key, base_url, today) :
        historical_data_api_url = base_url + str(today) + "?access_key=" + api_key  # + "&symbols=" + symbols
        return historical_data_api_url

    def write_json(self, new_data, historical_data_path, day) :
        file_name= Path(historical_data_path + str(day)+".json")
        with open(file_name, 'w') as file:
            file_data = new_data
            file.write(json.dumps(file_data))

    def ingest_historical_data(self) :
        api_key = os.getenv("API_KEY")
        base_url = IngestionConstants.BASE_URL
        # symbols = IngestionConstants.SYMBOLS

        today = date.today()
        for i in range(int(IngestionConstants.NUMBER_OF_DAYS_TO_LOAD_HISTORICAL_DATA)) :
            day = today - timedelta(days=i)
            historical_data_api_url = self.get_historical_data_api_url(api_key, base_url, day)
            response = requests.get(historical_data_api_url)
            json_data = json.loads(response.text)
            historical_data_path = IngestionConstants.HISTORICAL_DATA_FILE_PATH
            self.write_json(json_data, historical_data_path, day)
