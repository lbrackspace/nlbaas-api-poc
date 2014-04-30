import json
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
db = SQLAlchemy()


class BaseModel(object):
    def to_json(self):
        if not hasattr(self, 'TAG'):
            raise NotImplementedError
        return json.dumps({self.TAG: self.to_dict()}, indent=2)

    def to_dict(self):
        return self.get_pub_vars()

    def get_pub_vars(self):
        pub_vars = {}
        # attrs = dir(self)
        attrs = vars(self)
        for attr_name in attrs:
            if getattr(self, attr_name) is None:
                continue
            if attr_name[0] != '_':
                if isinstance(getattr(self, attr_name), BaseModel):
                    pub_vars[attr_name] = getattr(self, attr_name).to_dict()
                else:
                    pub_vars[attr_name] = getattr(self, attr_name)
        return pub_vars