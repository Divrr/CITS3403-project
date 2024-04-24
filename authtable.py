from flask import Flask, request, jsonify

app = Flask(__name__)

# JSON table to store authentication details
auth_table = []

@app.route('/auth', methods=['POST'])
def add_auth():
    data = request.get_json()
    auth_table.append(data)
    return jsonify({'message': 'Authentication details added successfully'})

if __name__ == '__main__':
    app.run(debug=True)