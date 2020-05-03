import sqlalchemy as db
import uuid
from sqlalchemy.dialects.postgresql import UUID


# for creating the table
def create_insert_table(action='insert', d_values=None):
    engine = db.create_engine('sqlite:///debDB.sqlite')  # Create test.sqlite automatically
    connection = engine.connect()
    metadata = db.MetaData()

    recipient = db.Table('recipientTable', metadata,
                    db.Column('Recipient ID', db.Integer, primary_key=True, nullable=False),
                    db.Column('Name', db.String(255), nullable=False),
                    db.Column('Email', db.String(255), nullable=False)
                    )

    if action.lower() == 'create':
        metadata.create_all(engine)
        return 'CREATED table name recipientTable'
    else:
        # will insert into the db values from parameter
        # will receive a dictionary 'values'
        print('psuhd_db called....')
        # print(d_values)
        # Inserting record one by one
        query = db.insert(recipient).values(Name="Jennifer", Email="neoanderson8732@gmail.com")
        # query = db.insert(recipient).values(Name="Tom", Email="sidmitra8732@gmail.com")
        ResultProxy = connection.execute(query)
        print(ResultProxy)
        return 'inserted into the table name poll'


if __name__ == '__main__':
    res = create_insert_table(action='create')
    print(res)
    pass
