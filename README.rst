Python ``raise`` as a Function
==============================

Raise exceptions with a function instead of a statement.

Provides a minimal, clean, and portable interface for raising
exceptions with all the advantages of functions over syntax.


Versioning
----------

This library's version numbers follow the `SemVer 2.0.0 specification
<https://semver.org/spec/v2.0.0.html>`_.

The current version number is available in the variable ``__version__``
as is normal for Python modules.


Installation
------------

::

    pip install raise

If you need to get it manually, or you need the "no traceback"
variant, see the `Manual Installation`_ section for tips.


Usage
-----

Import the ``raise_`` function from the ``raise_`` module:

.. code:: python

    from raise_ import raise_

Raise an exception:

.. code:: python

    raise_(Exception('foo'))

(You can also pass an exception type instead of an
instance as the first argument to ``raise_``.)

Raise an exception with a traceback:

.. code:: python

    raise_(Exception('foo'), my_traceback_object)

Raise in a ``lambda``:

.. code:: python

    lambda x: x if x > 0 else raise_(ValueError('x is too small!')) 

And you can combine ``raise_`` with ``functools.partial`` and other
functional programming libraries and techniques for many more uses.


Portability
-----------

Portable to all releases of both Python 3 and Python 2.

(The oldest tested is 2.5, but it will likely work on all
Python 2 versions and probably on even earlier versions.)

For implementations of Python that do not support raising with a custom
traceback, a "no traceback" variant can be installed manually.


Manual Installation
-------------------

Depending on your needs, either:

* Take one of these files and save it as ``raise_.py``:

  * ``raise_3.py`` is for Python 3.
  * ``raise_2.py`` is for Python 2.
  * ``raise_no_traceback.py`` is for Python implementations which
    do not support raising exceptions with a custom traceback.

* Take all of the above files and the ``__init__.py``
  file and save them in a folder called ``raise_``.

That way you can always do ``from raise_ import raise_``
in all of your other code and it'll just work.

You are of course welcome to just copy-paste the tiny ``raise_`` function
definition into your code, just keep in mind the compatibility issues
involved: your code will only work without modification on Python
versions compatible with the version you chose, and Python 2's version
causes a SyntaxError in Python 3, which is uncatchable unless you import
it from another file or wrap that function definition in an ``exec``.
