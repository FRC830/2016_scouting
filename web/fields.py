import flask_wtf
from wtforms.fields import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    match_id = IntegerField('Match ID')
    team_id = IntegerField('Team ID')
    #Auton Section
    auton_start = RadioField('Robot Starting Location',choices=['Neutral Zone', 'Courtyard'])
    auton_breach = RadioField('Defense Crossed in Auton', choices=['None',
                                                                    'Low bar',
                                                                    'Portcullis',
                                                                    'Cheval de Frise',
                                                                    'Moat',
                                                                    'Ramparts',
                                                                    'Drawbridge',
                                                                    'Sally Port',
                                                                    'Rock Wall',
                                                                    'Rough Terrain',
                                                                    'Touched a defense, did not cross'])
    auton_score = RadioField('Ball Scored', choices=['None', 'Low Goal', 'High Goal'])
    #Teleop Section
    teleop_breach = BooleanField('Defenses Breached At Some Point')
    breach_count = IntegerField('# of defenses breached')
    high_scores = IntegerField('High Goals Scored')
    high_misses = IntegerField('High Shots Missed')
    low_scores = IntegerField('Low Goals Scored')
    fouls = IntegerField('Fouls')
    tech_fouls = IntegerField('Tech Fouls')
    defense = RadioField('Robot Defense', choices=['Did not play defense',
                                                   'Bad', 'Good'])
    #EndGame Section
    hang = BooleanField('Robot Scaled Tower')
    comments = TextAreaField('Put comments here')
    
