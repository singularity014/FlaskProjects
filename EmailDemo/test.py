from dbmodel_conf import db
from dbmodel_conf import Surveyparams, Poll

# # for creating the models
# db.create_all()

# TABLE NAME - Surveyparams
# Survey_ID, name>, survery_reason<hardcode>, survery_date
# survey_reason1 = 'first reason'
# deb = Surveyparams(initiator='Deb', survey_reason=survey_reason1)
#

#survey, poll

# user response
d = {'username', 'answer_1', 'answer_2', 'user_id'}









# TABLE NAME - PoLL
survey_reason4 = 'sdsdsd reason'
deb = Surveyparams(initiator='vvvbbb', survey_reason=survey_reason4)
db.session.add(deb)
db.session.commit()
some_initiator = Surveyparams.query.filter_by(initiator='vvvbbb').first()
panu_sen = Poll(username='mmmmmm', answer_1='ddsdsdsd', answer_2='C++', surveyparams=some_initiator)
#
db.session.add(panu_sen)
db.session.commit()