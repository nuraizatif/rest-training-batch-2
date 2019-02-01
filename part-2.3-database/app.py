import json, logging, sys
from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from time import strftime
from logging.handlers import RotatingFileHandler

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['APP_DEBUG'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:masukaja@127.0.0.1/rest_training'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
	
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

from blueprints.person import bp_person

app.register_blueprint(bp_person, url_prefix='/person')

if __name__ == '__main__':
	## define log format and create a rotating log with max size of 10MB and max backup up to 10 files
	formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
	log_handler = RotatingFileHandler("%s/%s" % (app.root_path, 'storage/log/app.log'), maxBytes=10000, backupCount=10)
	log_handler.setLevel(logging.INFO)
	log_handler.setFormatter(formatter)
	app.logger.addHandler(log_handler)

	try:
		if sys.argv[1] == 'db':
			manager.run()
		else:
			## if you want to jsonify 500 error, you cannot. But you can set debug=False
			app.run(debug=app.config['APP_DEBUG'], host='0.0.0.0', port=5000)
	except IndexError as e:
		app.run(debug=app.config['APP_DEBUG'], host='0.0.0.0', port=5000)