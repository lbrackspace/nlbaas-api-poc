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
        accepted_types = (int, long, float, str, unicode, bool, dict, list,
                          BaseModel)
        ignore_vars = ['TAG']
        pub_vars = {}
        if hasattr(self, '_child_classes'):
            recurse_classes = self._child_classes
        else:
            recurse_classes = ()
        attrs = dir(self)
        for attr_name in attrs:
            attr = getattr(self, attr_name)
            if attr is None or attr_name in ignore_vars or \
                    hasattr(attr, '__call__'):
                continue
            if attr_name[0] != '_':
                attr = getattr(self, attr_name)
                if isinstance(attr, accepted_types):
                    if isinstance(attr, recurse_classes):
                        pub_vars[attr_name] = attr.to_dict()
                    else:
                        pub_vars[attr_name] = attr
        return pub_vars