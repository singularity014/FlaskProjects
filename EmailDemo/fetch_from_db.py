import sqlalchemy as db


# fetching data from db
def fetch_from_table(action='select'):
    engine = db.create_engine('sqlite:///debDB.sqlite')  # Create test.sqlite automatically
    connection = engine.connect()
    # metadata = db.MetaData()
    recipientsquery = "SELECT Email from recipientTable"
    results = connection.execute(recipientsquery)
    names = [row[0] for row in results]
    print(names)
    return names


if __name__ == '__main__':
    res = fetch_from_table(action='select')
    # print(res)
    pass
