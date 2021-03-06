from logging import getLogger

from datetime import date
from datetime import datetime

from six import PY3
from six import iteritems
from six import string_types

logger = getLogger(__name__)


def col_sizeof(obj_list):
    # item + type(8byte) + "_id" + \00 + ObjectID(12byte)
    if not isinstance(obj_list, list):
        raise TypeError("Expected list, got %r" % type(obj_list))
    return sum(col_sizeof_row(item) for item in obj_list)


def col_sizeof_row(row):
    return 17 + bson_sizeof(row)


def bson_sizeof(obj):
    # Note: this is a very rough estimate
    # see: http://bsonspec.org/#/specification
    try:
        if isinstance(obj, dict):
            # int32 + list + \00
            #          ^: type(8bit) + keystr + \00 + value
            return 5 + sum(2 + len(str(key)) + bson_sizeof(value) for key, value in iteritems(obj))
        elif isinstance(obj, (list, tuple, set, frozenset)):
            return 5 + sum(2 + bson_sizeof(value) for value in obj)
        elif isinstance(obj, int):
            return 4
        elif isinstance(obj, float if PY3 else (float, long)):  # NOQA
            return 8
        elif isinstance(obj, string_types):
            return 4 + len(obj) + 1
        elif obj is None:
            return 0
        elif isinstance(obj, bool):
            return 1
        elif isinstance(obj, (datetime, date)):
            return 8
        else:
            raise RuntimeError("Can't estimate size for %r" % obj)

    except Exception as exc:
        logger.critical("Failed to compute size (%s) for:\n\t%r", exc, obj)

    return 0
