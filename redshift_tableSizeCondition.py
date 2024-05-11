import psycopg2
import boto3

# Connect to the Redshift database
conn = psycopg2.connect(
    dbname='your_database',
    user='your_username',
    password='your_password',
    host='your_host',
    port='your_port'
)

# Create a cursor object
cur = conn.cursor()

# Execute the query to get the size of the table
cur.execute("""
    SELECT
        "table", 
        size
    FROM 
        SVV_TABLE_INFO
    WHERE 
        "table" = 'your_table_name'
""")

# Fetch the result
result = cur.fetchone()

# Close the cursor and the connection
cur.close()
conn.close()

# Get the size of the table
table_size = result[1]

# Decide whether to run the query using AWS Lambda or AWS Batch
if table_size < 1000:  # Replace with your threshold
    # Run the query using AWS Lambda
    lambda_client = boto3.client('lambda')
    response = lambda_client.invoke(
        FunctionName='your_lambda_function_name',
        InvocationType='RequestResponse',
        Payload='your_query'
    )
else:
    # Run the query using AWS Batch
    batch_client = boto3.client('batch')
    response = batch_client.submit_job(
        jobName='your_job_name',
        jobQueue='your_job_queue',
        jobDefinition='your_job_definition',
        containerOverrides={
            'command': ['python', 'my_script.py', 'Ref::your_query']
        }
    )