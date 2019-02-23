# Copyright 2018 Alexander Kozhevnikov <mentalisttraceur@gmail.com>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.


"""Raise exceptions with a function instead of a statement.

Provides a minimal, clean and portable interface for raising exceptions
with all the advantages of functions over syntax.

Note:
    This is the "no traceback" variant, for Python implementations that
    do not support using a custom traceback when raising. It exists to
    allow code using the ``raise_`` interface to gracefully degrade in
    the absence of full traceback support.
"""


__all__ = ('raise_',)
__version__ = '1.1.0'


def raise_(exception, traceback=None):
    """Raise an exception, optionally with a custom traceback.

    Arguments:
        exception (Union[BaseException, type]): The exception to raise.
            Can be an exception instance, which is raised directly,
            or an exception type, which is constructed when needed.
        traceback (Optional[TracebackType]): Traceback to raise with.

    Note:
        This "no traceback" variant, meant for Python implementations
        that do not support using a custom traceback when raising,
        silently ignores the ``traceback`` argument.
    """
    raise exception