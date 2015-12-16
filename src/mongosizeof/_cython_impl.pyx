#cython: embedsignature=True, always_allow_keywords=False
from logging import getLogger

logger = getLogger(__name__)

import sys
from datetime import date
from datetime import datetime

cpdef int naive_sizeof(object obj):
    cdef int total = sys.getsizeof(obj)

    if isinstance(obj, dict):
        for key, value in obj.iteritems():
            total += sys.getsizeof(key) + naive_sizeof(value)

    elif isinstance(obj, (list, tuple, set, frozenset)):
        for item in obj:
            total += naive_sizeof(item)

    return total

cpdef int col_sizeof(list obj_list):
    # item + type(8byte) + "_id" + \00 + ObjectID(12byte)
    cdef int total = 0
    for item in obj_list:
        total += col_sizeof_row(item)
    return total

cpdef int col_sizeof_row(dict row):
    return 17 + bson_sizeof(row)

cpdef int bson_sizeof(object obj):
    # Note: this is a very rough estimate
    # see: http://bsonspec.org/#/specification
    cdef int total = 0

    try:
        if isinstance(obj, dict):
            # int32 + list + \00
            #          ^: type(8bit) + keystr + \00 + value
            total = 5
            for key, value in obj.iteritems():
                total += 2 + len(str(key)) + bson_sizeof(value)
        elif isinstance(obj, (list, tuple, set, frozenset)):
            total = 5
            for value in obj:
                total += 2 + bson_sizeof(value)
        elif isinstance(obj, int):
            total = 4
        elif isinstance(obj, (float, long)):
            total = 8
        elif isinstance(obj, basestring):
            total = 4 + len(obj) + 1
        elif obj is None:
            total = 0
        elif isinstance(obj, bool):
            total = 1
        elif isinstance(obj, (datetime, date)):
            total = 8
        else:
            logger.critical("Failed to compute size (unknown type %r) for:\n\t%r", type(obj), obj)
    except Exception as exc:
        logger.critical("Failed to compute size (%s) for:\n\t%r", exc, obj)

    return total
