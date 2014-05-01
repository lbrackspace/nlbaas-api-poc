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
        ignore_vars = ['TAG']
        attrs = dir(self)
        for attr_name in attrs:
            attr = getattr(self, attr_name)
            if attr is None or attr_name in ignore_vars or \
                    hasattr(attr, '__call__'):
                continue
            if attr_name[0] != '_':
                attr_value = self._attribute_to_dict(attr_name)
                if attr_value is not None:
                    pub_vars[attr_name] = attr_value
        return pub_vars

    def _attribute_to_dict(self, attr_name):
        ret = None
        accepted_types = (int, long, float, str, unicode, bool, dict, list,
                          BaseModel)
        if hasattr(self, '_child_classes'):
            recurse_classes = self._child_classes
        else:
            recurse_classes = ()

        attr = getattr(self, attr_name)

        if isinstance(attr, accepted_types):
            if isinstance(attr, list):
                dict_list = []
                for item in attr:
                    if isinstance(item, accepted_types):
                        if isinstance(item, recurse_classes):
                            dict_list.append(item.to_dict())
                        else:
                            dict_list.append(item)
                ret = dict_list

            elif isinstance(attr, recurse_classes):
                ret = attr.to_dict()
            else:
                ret = attr
        return ret