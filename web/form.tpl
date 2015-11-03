% rebase('base.tpl', title='Scouting form')
% from form import render_field
<h2>Scouting form</h2>
<form action="/form/save" method="post" id="scouting-form">
  <div class="row form-group">
    <div class="col-md-4 col-xs-12">
      % render_field('match_id')
    </div>
    <div class="col-md-4 col-xs-12">
      % render_field('team_id')
    </div>
  </div>
  <div class="row">
    <div class="col-md-4"><input type="submit" class="btn btn-primary" value="Save"></div>
  </div>
</form>
