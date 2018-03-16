Python ``raise`` as a Function
==============================

Raise exceptions with a function instead of a statement.

Provides a minimal, clean and portable interface for raising exceptions
with all the advantages of functions over syntax.


Versioning
----------

This library's version numbers follow the `SemVer 2.0.0 specification
<https://semver.org/spec/v2.0.0.html>`_.

The current version number is available in the variable ``__version__``
as is normal for Python modules.


Installation
------------

::

    pip install raise_

**If** you need or want to get it *manually* (for example if you're
using Brython or Skulpt or just cannot use ``pip``), see the
`<Advanced/Manual Installation>`_ section for suggestions/tips.


Usage
-----

.. code:: python

    from raise_ import raise_


Portability
-----------

Portable to all releases of both Python 3 and Python 2 back to 2.5,
when ``BaseException`` was first added.


Advanced/Manual Installation
----------------------------

There are two recommended ways of installing this manually, depending
on your needs:

1. If you're installing it into the library path for your Python system
   as a whole or adding it into the source tree of a project that is
   not meant to be compatible to both Python 3 and Python 2 or older,
   you can just take either ``raise3.py`` or ``raise2.py`` and save it
   *as* ``raise_.py``.

2. If you're adding it into the source tree of a project that should
   work with both Python 3 and Python 2 and older, copy the files
   ``raise_.py``, ``raise3.py``, and ``raise2.py``.

Both of these methods have the advantage that your code can just do
``from raise_ import raise_`` and it'll just work consistently,
without version-detecting boilerplate or hardcoding the version number
in the module name (which is an implementation detail).
