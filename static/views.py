from static import app

from flask import render_template, redirect, request, flash

import os


ALLOWED_EXTENSIONS = set(['pdf'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title='Home')

@app.route('/add-a-meter', methods=['POST', 'GET'])
def add_a_meter():
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('add_a_meter.html')






# @app.route('/handle-meter-request', methods=['POST'])
# def handleMeterRequest():
#     jobID = int(time()*sin(3))
#     if request.method == 'POST':
#         meterRequest = request.form.to_dict(flat=False)
#         db = dataset.connect('sqlite:///database.db')
#         table = db['requestTable']
#         #db['meterInventory']
#         meterRequestDict = {}
#
#         for key, values in meterRequest.items():
#             x = ';'.join(values)
#             meterRequestDict.update({key: x})
#
#         futureAppointments = table.find(
#             installationDate={'<=':datetime.datetime.strptime(meterRequestDict['installationDate'], "%Y-%m-%d") - datetime.timedelta(days=1)},
#             removalDate={'>=':datetime.datetime.strptime(meterRequestDict['removalDate'], "%Y-%m-%d")  + datetime.timedelta(days=1)})
#         table.insert(meterRequestDict)
#
#         x = 0
#         for row in futureAppointments:
#             x = x + int(row['qntDentElietPro'])
#             if x >= len(db['meterInventory']):
#                 print("failed attempt")
#     return redirect('/')
#
# @app.route('/meter-inventory')
# def meterInventory():
#     db = dataset.connect('sqlite:///database.db')
#     table = db['meterInventory']
#     return render_template('meterInventory.html',meters=table)
#
# @app.route('/handle-meter-inventory' , methods=['POST'])
# def handleMeterInventory():
#     if request.method == 'POST':
#         db = dataset.connect('sqlite:///database.db')
#         table = db['meterInventory']
#         meterInventoryDict= request.form.to_dict(flat=False)
#         meterRequestDictB={}
#         list = []
#         for j in meterInventoryDict['serialNumber'][0].split(';'):
#             meterRequestDictB.update({'serialNumber': j})
#             for key, values in meterInventoryDict.items():
#                 if key != 'serialNumber':
#                     meterRequestDictB.update({key: values[0]})
#                     list.append(meterRequestDictB)
#                     print(meterRequestDictB)
#         table.insert_many(list)
#     return redirect('/')

