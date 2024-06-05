from django.core.exceptions import ObjectDoesNotExist

def search_if_exist(function):
    try:
        data = function()
        return data
    except ObjectDoesNotExist:
        return None