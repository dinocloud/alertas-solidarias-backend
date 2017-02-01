from werkzeug.exceptions import BadRequest
import re

TYPE_VALIDATOR = 1
MAX_VALIDATOR = 2
MIN_VALIDATOR = 3
REGEX_VALIDATOR = 4

# Regex
# EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


def validate_type(param_name, param, param_type):
    if isinstance(param, param_type):
        return param
    else:
        raise BadRequest("The param {} is not type {}".format(param_name, param_type))


def validate_max(param_name, param, max_value):
    if param <= max_value:
        return param
    else:
        raise BadRequest("The param {} can't higher than {}".format(param_name, max_value))


def validate_min(param_name, param, min_value):
    if param >= min_value:
        return param
    else:
        raise BadRequest("The param {} can't less than {}".format(param_name, min_value))


def validate_regex(param_name, param, regex):
    if re.match(regex, param):
        return param
    else:
        raise BadRequest("The param {} has an incorrect format".format(param_name))


def validate_param(param_name, param, validations, required=False):
    if not param:
        if not required:
            return None
        else:
            raise BadRequest("The param {} can't be empty".format(param_name))

    for validator in validations:
        if validator[0] == TYPE_VALIDATOR:
            param = validate_type(param_name, param, validator[1])
        elif validator[0] == MAX_VALIDATOR:
            param = validate_max(param_name, param, validator[1])
        elif validator[0] == MIN_VALIDATOR:
            param = validate_min(param_name, param, validator[1])
        elif validator[0] == REGEX_VALIDATOR:
            param = validate_regex(param_name, param, validator[1])
    return param
