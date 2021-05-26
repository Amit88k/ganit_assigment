import os

cwd = os.getcwd()
os.chdir(cwd)

from src.jobs.load_historical_data import LoadHistoricalData
from src.shared.common_functions import CommonFunction
from src.jobs.save_data import DB


class Main:
    if __name__ == "__main__":
        db = DB()
        uris = db.create_db_uris()
        spark = CommonFunction.get_spark_instance(uris)
        load_historical_data = LoadHistoricalData(spark)
        raw_df = load_historical_data.read_historical_data(db)
        processed_df = load_historical_data.process_data(raw_df, db)


#  spark-submit --packages org.mongodb.spark:mongo-spark-connector_2.11:2.4.0 --py-files src.zip main.py