Python ``raise`` as a Function
==============================

Raise exceptions with a function instead of a statement.

Provides a minimal and portable interface for raising exceptions
with all the advantages of functions over syntax.


Versioning
----------

This library's version numbers follow the `SemVer 2.0.0
specification <https://semver.org/spec/v2.0.0.html>`_.


Installation
------------

::

    pip install raise


Usage
-----

Import ``raise_``:

.. code:: python

    from raise_ import raise_

Raise an exception:

.. code:: python

    raise_(Exception('foo'))

Raise an exception with a traceback:

.. code:: python

    raise_(Exception('foo'), traceback)

Raise in a ``lambda``:

.. code:: python

    lambda x: x if x > 0 else raise_(ValueError('x is too small!')) 

And of course because ``raise_`` is a function, you can combine
it with ``functools.partial`` and other functional programming
libraries and techniques for many more uses.


Surprises
---------

``raise_`` clears ``__traceback__`` if you don't pass in a traceback,
same as if you passed in ``None``. If you want the Python 3 behavior
of reusing the ``__traceback__``, you should explicitly pass it in:

.. code:: python

    raise_(exception, exception.__traceback__)

Or, if you want to gracefully degrade on Python implementations
which do not have ``__traceback__`` on their exceptions:

.. code:: python

    raise_(exception, getattr(exception, '__traceback__', None))


Portability
-----------

Portable to all releases of both Python 3 and Python 2.

(The oldest tested is 2.5, but it will likely work on all
Python 2 versions and probably on even earlier versions.)

For implementations of Python that do not support raising
with a custom traceback, a "no traceback" variant is
included in the source that can be installed manually.
