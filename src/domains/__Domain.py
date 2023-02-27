import json
import re
from pydoc import locate
from datetime import datetime, date
from enum import Flag
from inspect import signature

from soupsieve.util import lower


class Domain:
    @classmethod
    def create(cls, **args):
        pass

    @classmethod
    def from_json(cls, json_str):
        _dict = json.loads(json_str)
        return cls.__json_object_hook(_dict)

    def to_json(self):
        return json.dumps(self, default=self.__json_default,
                          sort_keys=False, indent=4)

    @classmethod
    def __json_object_hook(cls, obj):
        try:
            _obj = cls()
            sig = signature(cls.create)
            for _key in sig.parameters.keys():
                _parameter = sig.parameters.get(_key)
                _type = _parameter.annotation
                if _key not in obj:
                    _key = cls.snake_to_camel(_key)
                if _key in obj:
                    _val = obj[_key]
                else:
                    _val = None
                # print(f'{_type} {_key} = {_val}')
                _val = cls.__convert_val(_type, _val)
                _obj.__setattr__(_key, _val)

            return _obj
        except Exception as e:
            print(e)

    # noinspection PyTypeChecker
    @classmethod
    def __convert_val(cls, _type, _val):
        if _val is None:
            return _val
        if _type in (datetime, date):
            return datetime.strptime(_val, '%Y-%m-%dT%H:%M:%S.%fZ')
        elif issubclass(_type, Flag):
            return next(element for element in _type if element.name == _val or lower(element.name) == lower(_val) or cls.snake_to_camel(element.name) == cls.snake_to_camel(_val))
        elif issubclass(_type, Domain):
            return _type.__json_object_hook(_val)
        elif re.match(r'^list\[.*]$', str(_type)) is not None:

            sub_type = re.sub(r'^list\[(.*)]$', r'\1', str(_type))
            if sub_type != '':
                sub_type = locate(sub_type)
                if not isinstance(_val, list):
                    return [cls.__convert_val(sub_type, _val)]
                _val2 = []
                for v in _val:
                    _val2.append(cls.__convert_val(sub_type, v))
                return _val2
            else:
                if not isinstance(_val, list):
                    return [_val]
        return _val

    @classmethod
    def __json_default(cls, val):
        if isinstance(val, (datetime, date)):
            return val.strftime('%Y-%m-%dT%H:%M:%S.%fZ').replace('000Z', 'Z')
        if isinstance(val, Flag):
            return val.name
        elif val.__class__.__name__ in ['mappingproxy']:
            return None
        else:
            return val.__dict__

    @staticmethod
    def snake_to_camel(word):
        words = word.split('_')
        if len(words) > 1:
            return f"{words[0]}{''.join(x.capitalize() or '_' for x in words[1:])}"
        else:
            return word
