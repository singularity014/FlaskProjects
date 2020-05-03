import datetime
import sqlalchemy as db
from dbmodel_conf import *
import random
from sqlalchemy import *


# for creating the table
def create_insert_relationship_table(action, d_user_response, d_initiator_data):

    if action.lower() == 'create':
        db.create_all()
        return 'CREATED table name poll & Suervey_Params'
    else:
        # will insert into the db values from parameter
        # will receive a dictionary 'values'

        reasons_list = ['some reason', 'some other reason', 'more reason', 'abc reason', 'xyz reason', '123 reason']
        reason = random.choice(reasons_list)
        print('psuhd_db called....')


        print("STEP 1 - Populating First table Survey...")
        # INSERT -------------- TABLE - SurveyParams ------------------------------------
        initiator_mail = d_initiator_data['initiator_email']
        initiator_name = d_initiator_data['initiator_name']
        initator_date = d_initiator_data['initiator_date']
        condition_check = db.session.query(Surveyparams).filter(and_(Surveyparams.initiator_email == initiator_mail, Surveyparams.survey_date == initator_date)).first()
        if condition_check is None:
            query1 = Surveyparams(initiator=initiator_name,initiator_email=initiator_mail , survey_reason=reason, survey_date=initator_date)
            db.session.add(query1)
            db.session.commit()

        # -------------------------------------------------------------------------------

        print("STEP 2 - Populating Second table Poll...")
        filter_query = Surveyparams.query.filter_by(initiator_email=d_initiator_data['initiator_email']).first()
        query2 = Poll(username=f"{d_user_response['username']}", answer_1=f"{d_user_response['vote1']}", answer_2=f"{ d_user_response['vote2']}",
                      surveyparams=filter_query)
        db.session.add(query2)
        db.session.commit()
        return 'inserted into the table name poll & survey'


if __name__ == '__main__':


    res = create_insert_relationship_table('create', [], [])
    print(res)
    pass
