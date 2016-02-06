import flask_wtf
from wtforms.fields import * #http://wtforms.readthedocs.org/en/latest/fields.html

class Form(flask_wtf.Form):
    match_id = IntegerField('Match ID')
    team_id = IntegerField('Team ID')
    #Auton Section
    auton_start = RadioField('Robot Starting Location',choices=[('Neutral Zone','Neutral Zone'), ('Courtyard','Courtyard')],
                             default='Neutral Zone')
    auton_breach = RadioField('Defense Crossed in Auton', choices=[('None','None'),
                                                                   ('Touched a defense, did not cross','Touched a defense, did not cross'),
                                                                   ('Low bar','Low bar'),
                                                                   ('Portcullis','Portcullis'),
                                                                   ('Cheval de Frise','Cheval de Frise'),
                                                                   ('Moat','Moat'),
                                                                   ('Ramparts','Ramparts'),
                                                                   ('Drawbridge','Drawbridge'),
                                                                   ('Sally Port','Sally Port'),
                                                                   ('Rock Wall','Rock Wall'),
                                                                   ('Rough Terrain','Rough Terrain')])
    auton_score = RadioField('Ball Scored', choices=[('None','None'), ('Low Goal','Low Goal'), ('High Goal','High Goal')],
                             default='None')
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
    breach_count = IntegerField('Number of defenses breached')
    high_scores = IntegerField('High Goals Scored')
    high_misses = IntegerField('High Shots Missed')
    low_scores = IntegerField('Low Goals Scored')
    fouls = IntegerField('Fouls')
    tech_fouls = IntegerField('Tech Fouls')
    defense = RadioField('Robot Defense', choices=[('No Defense','Did not play defense'),
                                                   ('Bad','Bad'), ('Good','Good')])
    #EndGame Section
    hang = BooleanField('Robot Scaled Tower')
    comments = TextAreaField('Put comments here')
    
