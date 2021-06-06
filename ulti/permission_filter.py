from django.core.exceptions import FieldDoesNotExist

from permission.models import Group, Role
from ulti.check_field_in_model import is_field


def permission_filter(user, obj):
    group = Group.objects.filter(user=user)
    role = Role.objects.filter(group__in=group).order_by('permission_on')
    for i in role:
        '''Filter province'''
        if is_field(obj, 'province'):
            if i.permission_on == 'province':
                if i.permission_data != 'ALL':
                    obj = obj.filter(province=i.permission_data)

        '''Filter od'''
        if is_field(obj, 'operating_district'):
            if i.permission_on == 'operating_district':
                if i.permission_data != 'ALL':
                    obj = obj.filter(operating_district=i.permission_data)

        '''Filter facility'''
        if is_field(obj, 'facility'):
            if i.permission_on == 'facility':
                if i.permission_data != 'ALL':
                    obj = obj.filter(facility=i.permission_data)

    return obj
