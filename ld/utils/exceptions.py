import json

except_dict = {
    'AccountExist': {
        'code': 'AccountExist',
        'status': 403,
        'message': 'Account is exist.'
    },
    'LoginFail':{
        'code':'LoginFail',
        'status':403,
        'message':'用户或秘密错误'
    },
    'AccountNotFound':{
        'code':'AccountNotFound',
        'status':403,
        'message':'找不到该用户'
    }
}





def __init__(self, **kwargs):
    ''' make returned error message'''
    # the replace for json format
    self.message = self.message.format(**kwargs)


def __str__(self):
    return self.message


def __repr__(self):
    return self.message


class HttpException(Exception):
    pass


exceptions_list = []
bases = (HttpException,)
attrs = {
    '__init__': __init__,
    '__str__': __str__,
    '__repr__': __repr__
}

# generate error classes,
# add them to exception_list
# and then convert to exceptions tuple

for  item in except_dict:
    attrs.update(except_dict[item])
    ex = type(item, bases, attrs)
    exceptions_list.append(ex)
    globals().update({item: ex})

