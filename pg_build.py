import csv
import os
import psycopg2
from dotenv import load_dotenv

# Load .env file
load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

def table_exists(table_name, cur):
    cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = %s);", (table_name,))
    return cur.fetchone()[0]

def create_table_from_csv(filename, cur):
    table_name = os.path.splitext(os.path.basename(filename))[0]  # Extract table name from filename

    # Check if the table already exists
    if table_exists(table_name, cur):
        print(f"Table {table_name} already exists. Skipping...")
        return

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        columns = next(reader)  # Get the column names from the first row
        
        # Create a table creation query
        query = f"CREATE TABLE {table_name} ("
        for col in columns:
            query += f"{col} TEXT, "
        query = query.rstrip(", ") + ");"
        
        cur.execute(query)  # Execute the table creation query

        # Insert data into the table
        for row in reader:
            cur.execute(f"INSERT INTO {table_name} ({','.join(columns)}) VALUES ({','.join(['%s' for _ in row])});", row)

def main():
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    cur = connection.cursor()

    # Iterate over all CSV files in the "data" folder
    for filename in os.listdir('data'):
        if filename.endswith('.csv'):
            filepath = os.path.join('data', filename)
            create_table_from_csv(filepath, cur)

    connection.commit()  # Commit the transactions
    cur.close()
    connection.close()

if __name__ == '__main__':
    main()
