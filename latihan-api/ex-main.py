from flask import Flask,jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['GET'])
def hello():
    data = [{
        'nama': 'Bisma',
        'pekerjaan': 'Pelukis',
        'pesan': 'Jangan makan terus'
    }]
    return make_response({'data':data},200)

@app.route('/data_karyawan',methods=['GET','DELETE','PUT','POST'])
def data_karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama': 'Budi GET',
                'pekerjaan': 'Pembalap',
                'usia': 27
            }]
        elif request.method == 'POST':
            data = [{
                'nama': 'Budi POST',
                'pekerjaan': 'Pembalap',
                'usia': 27
            }]
        elif request.method == 'PUT':
            data = [{
                'nama': 'Budi PUT',
                'pekerjaan': 'Pembalap',
                'usia': 27
            }]
        else:
            data = [{
                'nama': 'Budi DELETE',
                'pekerjaan': 'Pembalap',
                'usia': 27
            }]
    except Exception as e:
        return make_response(jsonify({'error':str(e)}),400)
    return make_response(jsonify({'data':data}),200)

app.run()
