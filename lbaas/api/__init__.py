import ConfigParser

from flask import Flask
from lbaas.models.persistence import base
from flask.ext.restful import Resource, Api

filename = 'config.cfg'
config = ConfigParser.SafeConfigParser()
config.read([filename])

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s/%s' % (
    config.get('api', 'username'), config.get('api', 'password'),
    config.get('api', 'address'), config.get('api', 'dbname'))

api = Api(app)


#from lbaas.api.pub.resources import #resources imported here...


#Lbaas
##Add resources and routes here ex:...
#api.add_resource(lb.LoadbalancersResource, '/<int:account_id>/loadbalancers')

base.db.init_app(app)