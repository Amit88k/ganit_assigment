class Constants:
    SYMBOLS = "EUR,USD,JPY,CAD,GBP,NZD,IND"
    HISTORICAL_DATA_PATH = "/mnt/d/d/self/interviews/assignment_ganit/venv/historical_data_ingestion/data/historical_data/"
    PROCESSED_DATA_PATH = "/mnt/d/d/self/interviews/assignment_ganit/venv/historical_data_processing/data/processed_data/"


class DBConstants:
    DB_NAME = "currency"
    RAW_HISTORICAL_DATA_COLLECTION = "historical_data"
    PROCESSED_HISTORICAL_DATA_COLLECTION = "processed_historical_data"
    CLEANSED_HISTORICAL_DATA_COLLECTION = "cleansed_historical_data"
    ALL_CURRENCIES_COLLECTION = "currencies"
    MONGODB_HOST = "127.0.0.1:27017"


