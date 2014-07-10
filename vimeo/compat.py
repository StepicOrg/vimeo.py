import sys

__all__ = ['urlencode', 'b2s', 's2b']

PY2 = sys.version_info[0] < 3

if PY2:
    # noinspection PyCompatibility
    from urllib import urlencode

    def b2s(s):
        return s

    def s2b(s):
        # noinspection PyUnresolvedReferences
        if isinstance(s, str):
            return s
        elif isinstance(s, unicode):
            return s.encode('utf-8')
        else:
            raise TypeError("Expected unicode or bytes, got %r" % s)

else:
    # noinspection PyCompatibility
    from urllib.parse import urlencode

    def b2s(s):
        return s.decode() if isinstance(s, bytes) else s

    def s2b(s):
        if isinstance(s, bytes):
            return s
        elif isinstance(s, str):
            return s.encode()
        else:
            raise TypeError("Expected string or bytes, got %r" % s)
