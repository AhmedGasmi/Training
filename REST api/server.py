from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

# Simple authentication decorator
def requires_authentication(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_credentials(auth.username, auth.password):
            return jsonify({'error': 'Authentication required'}), 401
        return f(*args, **kwargs)
    return decorated

# Dummy function to check credentials (replace with your own logic)
def check_credentials(username, password):
    return username == 'admin' and password == 'password'

# Protected endpoint that requires authentication
@app.route('/protected', methods=['GET'])
@requires_authentication
def protected():
    return jsonify({'message': 'Access granted to protected endpoint'})

if __name__ == '__main__':
    app.run()
