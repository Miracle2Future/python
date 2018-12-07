# 模仿django orm 设计理念

import numbers

class Field:
    pass
# CharField 和 IntField 为属性描述类
class CharField(Field):
    
    def __init__(self, db_column, max_length=None, *args, **kwargs):
        self._value = None
        self.db_column = db_column
        self.max_length = max_length
        
        if max_length is not None:
            if not isinstance(max_length, numbers.Integral):
                raise ValueError('max_length must be int')
        
    # 获取属性值 
    def __get__(self, instance, owner):
        self._value
    
    # 设置属性值
    def __set__(self, instance, value):
#         if not isinstance(instance, numbers.Intergal):
        if not isinstance(value, str):
            raise ValueError('must str')
        if len(value) > self.max_length:
            raise ValueError('must be less than max_length')
        self._value = value
        
class IntField(Field):
    
    def __init__(self, db_column, min_value=None, max_value=None, *args, **kwargs):
        self._value = None
        self.db_column = db_column
        self.min_value = min_value
        self.max_value = max_value
        
        if min_value is not None:
            if not isinstance(min_value, numbers.Integral):
                raise ValueError('min_value must be int')
            elif min_value < 0:
                raise ValueError('min_value must be > 0')
        if max_value is not None:
            if not isinstance(max_value, numbers.Integral):
                raise ValueError('max_value must be int')
            elif max_value < 0:
                raise ValueError('max_value must be > 0')
        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError('min_value must be smaller than max_value')
    
    def __get__(self, instance, owner):
        return self._value
    
    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('must be int')
        if value < self.min_value or value > self.max_value:
            raise ValueError('must be between min_value and max_value')
        self._value = value


# 元类
class ModelMetaClass(type):
    
    def __new__(cls, name, bases, attrs, **kwargs):
#         print('name:{name},base:{bases}'.format(name=name,bases=bases))
        # 获取字段（name,age）
        if name == 'BaseModel':
            return super().__new__(cls, name, bases, attrs, **kwargs)
        fields = {}
        for key, value in attrs.items():
#             print('key:{key},value:{value}'.format(key=key, value=value))
                if isinstance(value, Field):
                    fields[key] = value
        print(fields)
        # 获取Meta
        attrs_meta = attrs.get('Meta', None)
        print(attrs_meta)
        db_table = name.lower()
        _meta = {}
        if attrs_meta is not None:
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta['db_table'] = db_table
        attrs['_meta'] = _meta
        attrs['fields'] = fields
        print(attrs)
        del attrs['Meta']    
        return super().__new__(cls, name, bases, attrs, **kwargs)
        
class BaseModel(metaclass=ModelMetaClass):
    
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            print('set key:{key} value:{}'.format(key=key, value=value))
            setattr(self, key, value)
        return super().__init__()
    
    def save(self,):
        print(self)
        print(self.fields)
        fields = []
        values = []
        for key, value in self.fields.items():
            print(key,value)
            db_column = value.db_column
            if db_column is None:
                db_column = key.lower()
            fields.append(db_column)
            value = getattr(self, key)
            values.append(value)
        print(fields)
        print(values)
#         sql = "insert into {keys} value={values} ".format(keys=kwargs.keys(), values=kwargs.values())
#         print(sql)

# 实现User
class User(BaseModel):
    
    name = CharField(db_column='name', max_length=10)
    age = IntField(db_column=None, min_value=1, max_value=100)
    
    class Meta:
        pass
