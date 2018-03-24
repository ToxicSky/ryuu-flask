def typecast(value=None, type_v='str'):
    if (value == None):
        return

    if type_v == 'str':
        return str(value)
    if type_v == 'int':
        return int(value)
    if type_v == 'float':
        return float(value)
    if type_v == 'bool':
        return bool(value)


from sqlalchemy.orm.exc import NoResultFound


def get_one_or_create(model, data):
    try:
        result = model().query.filter_by(**data).first()
        if result is None:
            raise NoResultFound
        return model().query.filter_by(**data).first()
    except NoResultFound:
        return model(**data)
