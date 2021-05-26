from pyspark.sql import SparkSession


class CommonFunction :

    @staticmethod
    def get_spark_instance(uris) :
        spark = SparkSession \
            .builder \
            .appName("processing historical load") \
            .config("spark.mongodb.input.uri", uris[0]) \
            .config("spark.mongodb.output.uri", uris[1]) \
            .getOrCreate()
        return spark
