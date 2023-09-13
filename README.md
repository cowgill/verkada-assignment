# PostgreSQL CSV Importer

For a Marketing Ops role interview at [Verkada](https://www.verkada.com/), I was given a quantitative assignment along with data in .csv files. No `.sql` create tables or import data scripts were provided so I decided to create my own since I'm all about automation.

This script is used to import `.csv` files into a PostgreSQL database. The script reads `.csv` files from a directory named `data`, and for each file, creates a new table (based off the `.csv` file name) in the database and populates it with the contents of the `.csv` file. It does not setup any primary/foreign keys, relationships, or indexes and the column data types are all `text`.

## Dependencies

Before you can use this script, you need to ensure the following are set up:

- **Python 3+**
- **PostgreSQL**


I prefer using a GUI tool like [Postico](https://eggerapps.at/postico2/) or [PSequel](https://psequel.com/) for creating the db and working with data.

## Setup
   - Start the PostgreSQL service
   - Create a new database

## Installation

#### Clone the repo
```bash
git clone verkada-assignment
```


#### Navigate to project directory
```bash
cd verkada-assignment
```

#### Install Python dependencies
```bash
pip install -r requirements.txt
```

## Usage

#### Prepare CSV files
Place the CSV files you want to import into the data directory. Ensure the first row of each CSV file contains column names. For example, `data/account.csv` will create a table called, "account".

#### Set Environment Vars
Copy and rename the `.env.example` file in the root of the project to `.env` and fill in the values.

#### Run the script:
```bash
python pg_build.py 
```

## Notes
If a table with the same name as a CSV file already exists in the database, the script will skip that file.

Always ensure your PostgreSQL service is running before executing the script and you have the necessary permissions.