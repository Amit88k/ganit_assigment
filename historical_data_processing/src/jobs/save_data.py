import os
import requests

from dotenv import load_dotenv
from src.shared.constants import DBConstants


class DB :
    def __init__(self) :
        load_dotenv()
        pass

    def create_db_uris(self) :
        database = DBConstants.DB_NAME
        collection = DBConstants.RAW_HISTORICAL_DATA_COLLECTION
        mongodb_host_url = DBConstants.MONGODB_HOST
        user_name = os.getenv("DB_USER")
        password = os.getenv("DB_USER_PASSWORD")
        mongodb_host = "mongodb://" + user_name + ":" + password + "@" + mongodb_host_url
        # mongodb_host = "mongodb://user1:12345678@127.0.0.1:27018"
        spark_mongodb_input_uri = mongodb_host + "/" + database + "." + collection + "?authSource=admin"
        spark_mongodb_output_uri = mongodb_host + "/" + database + "." + collection + "?authSource=admin"
        return spark_mongodb_input_uri, spark_mongodb_output_uri

    def save_data(self, df, database, collection):
        df.write\
            .format("com.mongodb.spark.sql.DefaultSource")\
            .mode("overwrite")\
            .option("database", database)\
            .option("collection", collection)\
            .save()
