from flask import Flask, request,jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Onpe'

mysql = MySQL(app)



@app.route('/departamentos', methods=['GET'])
def get_departamentos():
    cur = mysql.connection.cursor()
    cur.callproc('sp_getDepartamentos', (1, 25))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/provincias', methods=['GET'])
def get_provincias():
    cur = mysql.connection.cursor()
    cur.callproc('sp_getProvincias', (1,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/distritos', methods=['GET'])
def get_distritos():
    cur = mysql.connection.cursor()
    cur.callproc('sp_getDistritos', (1,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/localvotaciones', methods=['GET'])
def get_localvotaciones():
    cur = mysql.connection.cursor()
    cur.callproc('sp_getLocalesVotacion', (1,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/grupovotaciones', methods=['GET'])
def get_grupovotaciones():
    cur = mysql.connection.cursor()
    cur.callproc('sp_getGruposVotacion', (1,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/grupovotacion/<string:grupo_id>', methods=['GET'])
def get_grupovotacion(grupo_id):
    cur = mysql.connection.cursor()
    cur.callproc('sp_getGrupoVotacion', (grupo_id,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

@app.route('/votos', methods=['GET'])
def get_votos():
    cur = mysql.connection.cursor()
    cur.callproc('sp_getVotos', (1, 25))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/votos/departamento/<string:departamento>', methods=['GET'])
def get_votos_departamento(departamento):
    cur = mysql.connection.cursor()
    cur.callproc('sp_getVotosDepartamento', (departamento,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/votos/provincia/<string:provincia>', methods=['GET'])
def get_votos_provincia(provincia):
    cur = mysql.connection.cursor()
    cur.callproc('sp_getVotosProvincia', (provincia,))
    data = cur.fetchall()
    cur.close()
    return jsonify(data)

if __name__=='__main__':
    app.run(debug=True, port=5000)
