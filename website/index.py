from flask import Blueprint, request, render_template, url_for
from flask_login import login_required, current_user
from .SMART import SMART

index_blueprint = Blueprint('index', __name__)

@index_blueprint.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.values.get('deviceName')
        id = request.form.get('deviceId')
        phone = request.form.get('phone')
        highPh = request.form.get('highPH')
        lowPh = request.form.get('lowPH')
        highTemp = request.form.get('highTemp')
        lowTemp = request.form.get('lowTemp')
        highMoisture = request.form.get('highMoisture')
        lowMoisture = request.form.get('lowMoisture')
        #SMARTObj = SMART(name, id, highMoisture, lowMoisture, highTemp, lowTemp, highPh, lowPh)
        print(name, id, phone, highPh, lowPh, highTemp, lowTemp, highMoisture, lowMoisture)
    return render_template('index.html', user = current_user)

