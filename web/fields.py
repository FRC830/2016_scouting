import flask_wtf
from widgets import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    match_id = IntegerField('Match ID')
    team_id = IntegerField('Team ID')
    #Auton Section
    auton_start = RadioField('Robot Starting Location',choices=[('Neutral Zone','Neutral Zone'), ('Courtyard','Courtyard')],
                             default='Neutral Zone')
    auton_breach = RadioField('Defense Crossed in Auton', choices=[('0','None'),
                                                                   ('1','Touched'),
                                                                   ('2','Crossed (Mark the defense in the Teleop section)')],
                                                                   default='0')
    auton_score = RadioField('Ball Scored', choices=[('0','None'), ('1','Low Goal'), ('2','High Goal')],
                             default='0')
    #Teleop Section

        #Breaching checkboxes
    lb_breach = BooleanField('Low Bar')
    pc_breach = BooleanField('Portcullis')
    cf_breach = BooleanField('Cheval de Frise')
    mo_breach = BooleanField('Moat')
    rp_breach = BooleanField('Ramparts')
    db_breach = BooleanField('Drawbridge')
    sp_breach = BooleanField('Sally Port')
    rw_breach = BooleanField('Rock Wall')
    rt_breach = BooleanField('Rough Terrain')

        #Other
    breach_count = IntegerField('Number of defenses crossed', default=0)
    high_scores = IntegerField('High Goals Scored', default=0)
    high_misses = IntegerField('High Shots Missed', default=0)
    low_scores = IntegerField('Low Goals Scored', default=0)
    fouls = IntegerField('Fouls', default=0)
    tech_fouls = IntegerField('Tech Fouls', default=0)

    defense_rating = RadioField('How well did they play defense?', choices=[('0','Did not Defend'), ('1', 'Bad Defense'), ('2', 'Moderate Defense'), ('3', 'Best Defense')], default="0")
    defense_time = RadioField('How much time did they spend on defense?', choices=[('0', 'No Time'), ('1', 'Less than Half'), ('2', 'Most of the Time'), ('3', 'All Match')], default="0")

    hang = BooleanField('Robot Scaled Tower')
    comments = TextAreaField('Put comments here')
