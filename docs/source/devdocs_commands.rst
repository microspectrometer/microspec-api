.. _devdocs_commands:

microspec.commands
==================

Connection to microspeclib
--------------------------

:class:`~microspec.commands.Devkit` inherits from
:class:`microspeclib.simple.MicroSpecSimpleInterface` to
customize its auto-generated methods. The customizations simplify
application programming:

- add default parameter values
- format responses to use strings instead of numbers
- add a timeout handler via a mix-in
- add custom docstrings with examples

The auto-generated methods of
:class:`~microspeclib.simple.MicroSpecSimpleInterface` are generated
from the dev-kit command definitions in the ``protocol.command``
**object** of the :ref:`JSON API config file <dev-kit-API-JSON>`:

- the **keys** are the **byte values** sent over serial to
  represent the command
- the **values** are **objects** that:

  - **name** the command
  - describe the command **parameters**
  - define the **byte format** of the complete message

- **command names** in ``protocol.command`` are identical to the
  **method names** in ``Devkit`` except that the first letter of the
  command is capitalized

