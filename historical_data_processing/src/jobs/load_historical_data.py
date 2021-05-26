import os
from datetime import date

from src.shared.constants import Constants
from pyspark.sql import functions as F
from src.shared.constants import DBConstants


class LoadHistoricalData :

    def __init__(self, spark) :
        self.spark = spark

    def read_historical_data(self, db) :
        df = self.spark.read.json(Constants.HISTORICAL_DATA_PATH, multiLine=True)
        df.show()
        df.printSchema()

        db.save_data(df, DBConstants.DB_NAME, DBConstants.RAW_HISTORICAL_DATA_COLLECTION)
        return df

    def drop_duplicates(self, df, key):
        df = df.dropDuplicates([key])
        return df

    def save_processed_data_on_local(self, df) :
        today = date.today()
        processed_data_file_name = Constants.PROCESSED_DATA_PATH + str(today) + ".csv"
        df.coalesce(1).write.option("header", "true").csv(processed_data_file_name)

    def process_data(self, df, db):
        print("inside processed data function")
        # data cleansing, drop duplicates for a date
        cleansed_df = self.drop_duplicates(df, "date")
        db.save_data(cleansed_df, DBConstants.DB_NAME, DBConstants.CLEANSED_HISTORICAL_DATA_COLLECTION)

        # Flatten the cleansed_df and filter required rates
        df = cleansed_df.select(F.col("date"), F.col("base"), F.col("rates.EUR"), F.col("rates.USD"), F.col("rates.JPY"),
                        F.col("rates.CAD"), F.col("rates.GBP"), F.col("rates.NZD"), F.col("rates.INR"))
        df.show()
        self.save_processed_data_on_local(df)
        db.save_data(df, DBConstants.DB_NAME, DBConstants.PROCESSED_HISTORICAL_DATA_COLLECTION)






