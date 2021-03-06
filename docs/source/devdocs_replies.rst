.. _devdocs_replies:

microspec.replies
=================

Connection to microspeclib
--------------------------

Commands receive a low-level response, then instantiate a
high-level response using the classes defined in
:mod:`~microspec.replies`.

The command populates the high-level response with the attributes
of the low-level response. This is the seam where integer codes
are replaced with strings and additional attributes are provided
as conveniences to applications.

Simple Command Responses
------------------------

Command responses are auto-generated classes defined in
``microspeclib``. These responses are too *low-level* for direct
use in applications:

- the command response includes **serial communication**
  attributes that applications do *not* need to access
- all attribute values are **integers**
    - requires users to look up the meaning of the integer

Module :mod:`~microspec.replies` defines *high-level* versions of
each command response. This creates a seam to:

- hide the serial communication attributes from the application
- add attributes as conveniences for applications:

    - getExposure returns with attributes for milliseconds and
      cycles
    - captureFrame returns with a dict attribute that
      packages the pixel data with its pixel number

- replace integer values with strings matching the names of the
  constants defined in :mod:`~microspec.constants`
- add a ``__repr__`` to eliminate the need to wrap responses in a
  ``print()`` when working at the REPL

    - the ``__repr__`` comes for free with namedtuples
      (it's the ``collections.namedtuple.__repr__()``)

- add custom docstrings for each response

For developers working on :mod:`~microspec.replies`
---------------------------------------------------

For every command defined in ``microspec.Devkit``, there is a
namedtuple in ``replies`` with the same name. There is no
name conflict because the commands are methods of ``Devkit`` and
the replies are members of the ``replies`` module.

For example, :func:`microspec.Devkit.getBridgeLED` is a command
which has the response :class:`microspec.replies.getBridgeLED`.

It is important that the *name* of a namedtuple is the **same**
as its *type name*. This has to do with how the Sphinx
**autodoc** extension handles namedtuples.

The preferred (and usual) approach with autodoc is to use the
``:members:`` option and recursively document everything in the
module. But this generates an ``alias`` in the documentation.

The alias is generated for:

- the **class** if the names are **different**
- the **class attributes** if the names are the **same**

Either way, some ``alias`` is generated and it shows up as noise
in the documentation.

The alternative to using the ``:members:`` option is to
explicitly invoke the ``autoclass::`` directive for the module's
classes.

When using the autodoc directive ``autoclass::``, if the names of
the namedtuple and its type are different, Sphinx generates an
``alias`` for the class created by the namedtuple.

My solution, therefore, to autodoc a module containing
namedtuples is to:

- use the same name for the namedtuple and its type name
- list each namedtuple with the ``autoclass::`` directive
- do not use option ``:members:`` with the ``automodule::`` and
  ``autoclass::`` directives

    - the ``automodule::`` directive picks up the module
      docstring without picking up anything else in the module
    - the ``autoclass::`` directive picks up the namedtuple
      docstring without picking up class members
    - the documentation looks like class members were picked up
      because they are documented in the namedtuple docstring
      (just as you would do for a class that was *not* generated
      by a namedtuple)

Docstrings use text substitution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Module :mod:`~microspec.replies` uses a dictionary to define
snippets of reusable documentation and a shorthand name for each
snippet. These docstring snippets are a single source of truth
for information that is repeated.

How the substitution works
^^^^^^^^^^^^^^^^^^^^^^^^^^
The docstrings in module :mod:`~microspec.replies` use dictionary
``_common`` for reusable docstring snippets.

Here is a simplified example to demonstrate docstring
substitution:

.. code-block:: python

    >>> _common = {"status": "STATUS", "notes": "NOTES"}
    >>> replace_me = '''Docstring with {status} and {notes}.'''
    >>> replace_me.format(**_common)
    'Docstring with STATUS and NOTES.'

How to handle newlines
^^^^^^^^^^^^^^^^^^^^^^
Trailing ``\`` at the end of a line eliminates the newline
introduced by the multiline string:

.. code-block:: python

    >>> one_line = '''This is \
    ... one line'''
    >>> print(one_line)
    This is one line

Otherwise the multiline string includes all newlines:

.. code-block:: python

    >>> two_lines = '''This is
    ... two lines'''
    >>> print(two_lines)
    This is
    two lines

Newlines are included even when they are the only character:

.. code-block:: python

    >>> three_lines = '''This is
    ... three lines
    ... '''
    >>> print(three_lines)
    This is
    three lines
