try:
    BaseException.with_traceback
    from raise_.raise_3 import raise_
except (NameError, AttributeError):
    try:
        from raise_.raise_2 import raise_
    except SyntaxError:
        from raise_.raise_no_traceback import raise_
