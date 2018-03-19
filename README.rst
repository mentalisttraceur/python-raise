Python ``raise`` as a Function
==============================

Raise exceptions with a function instead of a statement.

Provides a minimal, clean and portable interface for raising exceptions
with all the advantages of functions over syntax.


Why
---

I want to be able to work with exceptions in a way that is:

1. *Intuitive* to use and see in code.
2. *Generic* and *flexible*, empowering *reuse*.
3. *Portable* to all versions of Python I might want to use.

Python is a great language, and modern Python in particular takes a
nice approach to exceptions.

In my code, I've often found myself writing interaces that combine
the intuitive nature of Python 3's ``raise`` and ``with_traceback``,
the generic and flexible pattern of raising exceptions in other
coroutines or threads of control as exemplified by the ``throw``
method on Python generators, in the inherently portable and powerfully
reusable and composable form of a basic function.

The interface provided by this module, the function signature taking
an ``exception`` (either an instance *or* type) and an optional
``traceback`` instance, is what I found myself arriving at that met all
of these criteria. It has served us well in code that I've worked on,
and I'm submitting it to the world in the hope that others will either
find it useful and build upon it or point out flaws in my approach.


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

Import the ``raise_`` function from the ``raise_`` module:

.. code:: python

    from raise_ import raise_

Then you can raise things in a fairly intuitive manner:

1. Raising an exception:

    .. code:: python

        raise_(Exception('foo'))

    You can of course also pass an exception type instead of an
    exception instance as the first argument to ``except``.

2. Raising an exception with a traceback:

    .. code:: python

        raise_(Exception('foo'), traceback=my_traceback_object)

   ``traceback`` does not have to be passed as a keyword argument, but
   one advantage of doing so, is that this form (an exception as a
   positional argument and ``traceback`` as a keyword argument) fits the
   signature of Python's generator ``throw`` method too.


Portability
-----------

Portable to all releases of both Python 3 and Python 2 back to 2.5,
when ``BaseException`` was first added.

(If you polyfill ``BaseException`` globally and/or make it fallback to
using ``Exception`` when ``BaseException`` doesn't exist, it will likely
work on all Python 2 versions and probably on even earlier versions.)


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
   work with both Python 3 and Python 2 and older, copy the whole
   ``raise_`` directory.

Both of these methods have the advantage that your code can just do
``from raise_ import raise_`` and it'll just work consistently,
without version-detecting boilerplate or hardcoding the version number
in the module name (which is an implementation detail).
