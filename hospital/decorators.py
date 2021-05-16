from django.core.exceptions import PermissionDenied


def user_is_hospital(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'hospital':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap


def user_is_bloodbank(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'bloodbank':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap



def user_is_supplier(function):
    def wrap(request, *args, **kwargs):
        user = request.user
        if user.role == 'supplier':
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied

    return wrap
