import sqlalchemy as db


# For Creating, as well as pushing the data into table
def create_insert_table(action='insert', d_values=None):
    engine = db.create_engine('sqlite:///debDB.sqlite')  # Create debDB.sqlite automatically in same path
    connection = engine.connect()
    metadata = db.MetaData()

    poll = db.Table('poll', metadata,
                    db.Column('name', db.String(255), nullable=False),
                    db.Column('vote1', db.String(255), nullable=False),
                    db.Column('vote2', db.String(255), nullable=False)
                    )
    if action.lower() == 'create':
        metadata.create_all(engine)
        return 'CREATED DB debDB, table name poll'
    else:
        # will insert into the db values from parameter
        # will receive a dictionary 'values'
        print('push_db called.......')
        print(d_values)
        # Inserting record one by one
        query = db.insert(poll).values(name=f"{d_values['username']}", vote1=f"{d_values['vote1']}", vote2=f"{d_values['vote2']}")
        ResultProxy = connection.execute(query)
        print(ResultProxy)
        return 'inserted into the table name poll'


if __name__ == '__main__':
    # For creating the DB use this approach.....
    res = create_insert_table(action='create')
    print(res)

