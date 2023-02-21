from flask import Flask, jsonify, request, abort
from dbase.models import Data, data_json
from dbase.mongodb import Database as db
from forms.Forms import DataForm

from flask_restful import Resource, Api, marshal_with

app = Flask(__name__)
api = Api(app)
app.config['JSON_SORT_KEYS'] = False   # Keep the json data order


class IncidentList(Resource):
    def get(self):
        all_incidents = db.fetch_all_data()
        if not all_incidents:
            abort(404, "Data not found")
        return jsonify(all_incidents)

    def post(self):
        data = request.json
        payload = Data(
            data.get('country'),
            data.get('incident'),
            data.get('location'),
            data.get('casualties'),
            data.get('injured'),
        )
        db.add_data(data_json(payload))
        return data, 201

# @app.route('/incidents/', methods=["GET", "POST"])
# def dashboard():
#     form = DataForm()
#     if form.validate_on_submit():
#         payload = Data(
#             country=form.country.data,
#             incident=form.incident.data,
#             incident_date=form.incident_date.data,
#             location=form.location.data,
#             casualties=form.casualties.data,
#             injured=form.injured.data,
#         )
#         db.add_data(payload.create_json())
#         flash('New data added successfully', 'success')
#         return redirect(url_for('dashboard'))
#     return render_template('dashboard.html', form=form)


api.add_resource(IncidentList, '/api/')

if __name__ == '__main__':
    app.run()
