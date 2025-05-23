import boto3
import json
import pymysql

region = 'us-east-1'
parameter_store = '/dev/petclinic/rds_endpoint'
secret_name_tag = 'dev-rds-db'
file_path = "/opt/application.properties"


ssm = boto3.client('ssm', region_name=region)

rds_endpoint = ssm.get_parameter(Name=parameter_store)['Parameter']['Value']

secrets_client = boto3.client('secretsmanager', region_name=region)

secrets_list = secrets_client.list_secrets()
secret_arn = None
for secret in secrets_list['SecretList']:
    if 'Tags' in secret:
        for tag in secret['Tags']:
            if tag['Key'] == 'Name' and tag['Value'] == secret_name_tag:
                secret_arn = secret['ARN']
                break

if secret_arn is None:
    print(f"Secret with name tag '{secret_name_tag}' not found.")
    exit(1)

response = secrets_client.get_secret_value(SecretId=secret_arn)
secret_value = response['SecretString']

secret_data = json.loads(secret_value)

with open(file_path, 'r') as f:
    file_contents = f.read()

file_contents = file_contents.replace("spring.datasource.url=jdbc:mysql://localhost:3306/todoapp", f"spring.datasource.url=jdbc:mysql://{rds_endpoint}/todoapp")
file_contents = file_contents.replace("spring.datasource.username=root", f"spring.datasource.username={secret_data['username']}")
file_contents = file_contents.replace("spring.datasource.password=tirthraj07", f"spring.datasource.password={secret_data['password']}")


with open(file_path, 'w') as f:
        f.write(file_contents)

try:
    if ':' in rds_endpoint:
        rds_endpoint = rds_endpoint.split(':')[0]
    connection = pymysql.connect(
        host=rds_endpoint,
        user=secret_data['username'],
        password=secret_data['password'],
        port=3306
    )
    with connection.cursor() as cursor:
        cursor.execute("SHOW DATABASES LIKE 'todoapp';")
        result = cursor.fetchone()
        if not result:
            print("Creating 'todoapp' database...")
            cursor.execute("CREATE DATABASE todoapp;")
        else:
            print("'todoapp' database already exists.")
    connection.commit()
finally:
    connection.close()  