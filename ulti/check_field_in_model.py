def is_field(obj, field_name):
    for field in obj.model._meta.get_fields(include_hidden=True):
        if field.name == field_name:
            return True
    return False
