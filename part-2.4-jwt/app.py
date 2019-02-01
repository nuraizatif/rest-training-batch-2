from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from datetime import timedelta
import json, logging
from logging.handlers import RotatingFileHandler
from flask_jwt_extended import JWTManager

app = Flask(__name__)

#################################### 
# JWT
####################################

app.config['JWT_SECRET_KEY'] = 'SFsieaaBsLEpecP675r243faM8oSB2hV'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)

jwt = JWTManager(app)

@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    return {
        'hello': identity,
        'foo': ['bar', 'baz']
    }
	
#################################### 
# Flask-RESTFul define custom error
####################################

## catch 404 default error with catch_all_404s=True
api = Api(app, catch_all_404s=True)

#################################### 
# Middlewares 
######################################

@app.after_request
def after_request(response):
	if request.method=='GET':
		app.logger.warning("REQUEST_LOG\t%s", json.dumps({ 'request': request.args.to_dict(), 'response': json.loads(response.data.decode('utf-8')) }))
	else:
		app.logger.warning("REQUEST_LOG\t%s", json.dumps({ 'request': request.get_json(), 'response': json.loads(response.data.decode('utf-8')) }))
	return response

#################################### 
# Import blueprints
####################################

from blueprints.person.resources import bp_person
from blueprints.auth import bp_auth

app.register_blueprint(bp_person, url_prefix='/person')
app.register_blueprint(bp_auth, url_prefix='/token')

if __name__ == '__main__':

	## define log format and create a rotating log with max size of 10MB and max backup up to 10 files
	formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
	log_handler = RotatingFileHandler("%s/%s" % (app.root_path, 'storage/log/app.log'), maxBytes=10000, backupCount=10)
	log_handler.setLevel(logging.INFO)
	log_handler.setFormatter(formatter)
	app.logger.addHandler(log_handler)

	## if you want to jsonify 500 error, you cannot. But you can set debug=False
	app.run(debug=True, host='0.0.0.0', port=5000)