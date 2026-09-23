import pandas as pd
from sqlalchemy import create_engine
import os
from urllib.parse import quote_plus

# CSV folder
folder_path = os.path.join(os.path.dirname(__file__), "music store data", "music store data")

# MySQL details
username = "root"

import os
from getpass import getpass
password = os.environ.get("MYSQL_PASSWORD") or getpass("Enter MySQL password: ")

# Special characters in password ko safely handle karega
password = quote_plus(password)

# MySQL connection
engine = create_engine(
    f"mysql+pymysql://{username}:{password}@localhost:3306/music_database"
)

# Upload all CSV files
for file in os.listdir(folder_path):

    if file.lower().endswith(".csv"):

        file_path = os.path.join(folder_path, file)

        df = pd.read_csv(file_path)

        table_name = os.path.splitext(file)[0]

        df.to_sql(
            table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        print(f"{file} uploaded successfully!")

print("All CSV files uploaded successfully!")