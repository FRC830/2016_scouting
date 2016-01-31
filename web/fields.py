import flask_wtf
from wtforms.fields import *

class Form(flask_wtf.Form):
    match_id = IntegerField('Match ID')
    team_id = IntegerField('Team ID')
