from sqlalchemy import create_engine
import pandas as pd
from app.config import BOSTON_HOUSING_DATA_PATH, BOSTON_COLUMNS, DB_CONNECTION_STRING


def populate_database():
    data = pd.read_csv(
        BOSTON_HOUSING_DATA_PATH, names=BOSTON_COLUMNS, delim_whitespace=True
    )
    engine = create_engine(DB_CONNECTION_STRING)
    data.to_sql("boston_housing", engine, index=False, if_exists="replace")
    print("Data loaded to DB")


if __name__ == "__main__":
    populate_database()
