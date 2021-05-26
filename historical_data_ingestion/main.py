from src.jobs.ingestion import Ingestion


class Main:
    if __name__ == "__main__":
        ingstion = Ingestion()
        ingstion.ingest_historical_data()
