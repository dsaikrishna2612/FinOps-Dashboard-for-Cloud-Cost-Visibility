import boto3
import sqlite3
from datetime import datetime, timedelta

client = boto3.client('ce', region_name='us-east-1')

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
        'End': datetime.now().strftime('%Y-%m-%d')
    },
    Granularity='DAILY',
    Metrics=['UnblendedCost'],
    GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'}]
)

conn = sqlite3.connect('database/finops.db')
cursor = conn.cursor()

for group in response['ResultsByTime'][0]['Groups']:
    service = group['Keys'][0]
    cost = float(group['Metrics']['UnblendedCost']['Amount'])
    date = datetime.now().strftime('%Y-%m-%d')
    cursor.execute("INSERT INTO usage (date, service, cost) VALUES (?, ?, ?)", (date, service, cost))

conn.commit()
conn.close()

