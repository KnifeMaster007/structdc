from . import inttypes
from functools import reduce

type_mapping = dict(
    reduce(lambda acc, m: [*acc, *(getattr(m, '_type_mapping', {}).items())], [
        # Type definition modules
        inttypes
    ], [])
)
