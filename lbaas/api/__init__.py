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
from lbaas.api.pub.resources import load_balancer_resource, \
    health_monitor_resource, pool_resource, member_resource

##Add resources and routes here...
api.add_resource(load_balancer_resource.LoadbalancerResource, '/<int:tenant_id>/loadbalancers/<int:lb_id>')
api.add_resource(load_balancer_resource.LoadbalancersResource, '/<int:tenant_id>/loadbalancers')

api.add_resource(pool_resource.PoolsResource, '/<int:tenant_id>/pools')
api.add_resource(pool_resource.PoolResource, '/<int:tenant_id>/pools/<int:pool_id>')

api.add_resource(health_monitor_resource.HealthMonitorResource, '/<int:tenant_id>/pools/<int:pool_id>/healthmonitor')

api.add_resource(member_resource.MembersResource, '/<int:tenant_id>/pools/<int:pool_id>/members')
api.add_resource(member_resource.MemberResource, '/<int:tenant_id>/pools/<int:pool_id>/members/<int:member_id>')

base.db.init_app(app)