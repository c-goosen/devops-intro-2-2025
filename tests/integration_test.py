# integration_test.py
def ingest_data():
    # Simulate data ingestion
    return spark.createDataFrame([(1, "A"), (2, "B")], ["id", "value"])

def transform_data(df):
    # Simulate data transformation
    return df.withColumn("value", df["value"].cast("string"))

def store_data(df):
    # Simulate storing data
    df.write.mode("overwrite").parquet("/tmp/test_data")

def test_integration():
    # Ingest
    raw_data = ingest_data()
    # Transform
    transformed_data = transform_data(raw_data)
    # Store
    store_data(transformed_data)
    # Validate
    stored_data = spark.read.parquet("/tmp/test_data")
    assert stored_data.count() == 2
    assert stored_data.schema == transformed_data.schema
