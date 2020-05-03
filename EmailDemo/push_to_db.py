import datetime

import sqlalchemy as db
import uuid
from sqlalchemy import ForeignKey
from dbmodel_conf import db
from dbmodel_conf import Surveyparams, Poll


# for creating the table
def create_insert_table(action='insert', d_values=None):
    engine = db.create_engine('sqlite:///debDB.sqlite')  # Create test.sqlite automatically
    connection = engine.connect()
    metadata = db.MetaData()

    surveyParams = db.Table('Survey_Params', metadata,
                            db.Column('Survey_ID', db.Integer, primary_key=True, nullable=False),
                            db.Column('Initiator', db.String(255), nullable=False),
                            db.Column('Reason', db.String(255), nullable=False),
                            db.Column('Survey_Date', db.DateTime, nullable=False, default=datetime.datetime.now())
                            )

    poll = db.Table('poll', metadata,
                    db.Column('Poll ID', db.Integer, primary_key=True, nullable=False),
                    db.Column('SurveyParams_ID', db.Integer, ForeignKey('Survey_Params.Survey_ID')),
                    db.Column('Name', db.String(255), nullable=False),
                    db.Column('Answer1', db.String(255), nullable=False),
                    db.Column('Answer2', db.String(255), nullable=False)
                    )
    if action.lower() == 'create':
        metadata.create_all(engine)
        return 'CREATED table name poll & Suervey_Params'
    else:
        # will insert into the db values from parameter
        # will receive a dictionary 'values'
        print('psuhd_db called....')
        print(d_values)
        # Inserting record one by one
        now = datetime.datetime.now()
        print('current date & time--'+now)
        # query1 = db.insert(surveyParams).values(Initiator=f"{d_values['username']}", Reason="Feedback survey",
        #                                         Survey_Date=now)
        # ResultProxy1 = connection.execute(query1)
        # print(ResultProxy1)
        print("first one executed, now next query...")
        # query2 = db.insert(poll).values(Name=f"{d_values['username']}", Answer1=f"{d_values['vote1']}", Answer2=f"{
        # d_values['vote2']}")
        query2 = db.insert(poll).values(Name=f"{d_values['username']}", Answer1=f"{d_values['vote1']}",
                                        Answer2=f"{d_values['vote2']}")
        ResultProxy2 = connection.execute(query2)
        print(ResultProxy2)
        return 'inserted into the table name poll'


if __name__ == '__main__':
    res = create_insert_table(action='create')
    print(res)
    pass
