from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/api/login', methods=['POST'])
def login():
    status_code = 0
    message = 'Berhasil'
    data = {
        'no_anggota': 'USR0510-01',
        'nama_lengkap': 'Raden Muh. Saleh Idris',
        'nama_inisial': 'Rd Saleh',
        'tempat_lahir': 'Cirebon',
        'tgl_lahir': '13 Juli 1998',
        'tgl_gabung': '20-04-2020 12:11',
        'unit_kerja': 'Dosen Teknik Mesin',
        'alamat': 'Jl. Pangeran Cakra Buana RT 04 RW 01 No 8 Kecamatan Talun, Kabupaten Cirebon, Indonesia',
        'no_hp': '089677482931',
        'email': 'radensaleh@student.polindra.ac.id',
        'role': 1
    }

    json = {
        'status_code': status_code,
        'message': message,
        'data': [data]
    }
    return jsonify(json)


@app.route('/api/data-transaksi', methods=['POST'])
def data_transaksi():
    status_code = 0
    message = 'Berhasil'

    ar = []

    for i in range(1, 10):
        data = {
            'id_transaksi': 'TRX000'+str(i),
            'tgl_transaksi': str(i)+'-03-2020 08:00',
            'nominal_transaksi': '15000'+str(i)
        }
        ar.append(data)

    json = {
        'status_code': status_code,
        'message': message,
        'data': ar
    }
    return jsonify(json)


@app.route('/data-simpanan', methods=['POST'])
def data_simpanan():
    status_code = 0
    message = 'Berhasil'

    id_jenis = ''

    if id_jenis == '1':
        ar = []

        for i in range(1, 17):
            data = {
                'jenis_simpanan': 'SIMPANAN POKOK',
                'tgl_simpanan': str(i)+'-03-2020 08:00',
                'nominal_simpanan': '15000'+str(i)
            }
            ar.append(data)

        json = {
            'status_code': status_code,
            'message': message,
            'data': ar
        }
        return jsonify(json)
    elif id_jenis == '2':
        ar = []

        for i in range(1, 12):
            data = {
                'jenis_simpanan': 'SIMPANAN SUKARELA',
                'tgl_simpanan': str(i)+'-03-2020 08:00',
                'nominal_simpanan': '15000'+str(i)
            }
            ar.append(data)

        json = {
            'status_code': status_code,
            'message': message,
            'data': ar
        }
        return jsonify(json)
    elif id_jenis == '3':
        ar = []

        for i in range(1, 15):
            data = {
                'jenis_simpanan': 'SIMPANAN WAJIB',
                'tgl_simpanan': str(i)+'-03-2020 08:00',
                'nominal_simpanan': '15000'+str(i)
            }
            ar.append(data)

        json = {
            'status_code': status_code,
            'message': message,
            'data': ar
        }
        return jsonify(json)
    else:
        ar = []
        for i in range(1, 13):
            data = {
                'jenis_simpanan': 'SIMPANAN SHU',
                'tgl_simpanan': str(i)+'-03-2020 08:00',
                'nominal_simpanan': '15000'+str(i)
            }
            ar.append(data)

        json = {
            'status_code': status_code,
            'message': message,
            'data': ar
        }
        return jsonify(json)

    


if __name__ == '__main__':
    app.run(debug=True, host='192.168.43.197', port=8000)

    # var no_anggota: String? = null,
    # var nama_lengkap: String? = null,
    # var nama_inisial: String? = null,
    # var tempat_lahir: String? = null,
    # var tgl_lahir: String? = null,
    # var tgl_gabung: String? = null,
    # var unit_kerja: String? = null,
    # var alamat: String? = null,
    # var no_hp: String? = null,
    # var email: String? = null,
    # var role: Int? = null
