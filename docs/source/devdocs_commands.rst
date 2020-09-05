.. _devdocs_commands:

microspec.commands
==================

Connection to microspeclib
--------------------------

:class:`~microspec.commands.Devkit` inherits from
:class:`microspeclib.simple.MicroSpecSimpleInterface` to
customize its auto-generated methods. The customizations simplify
application programming:

- improve commands:
    - provide default parameter values where it makes sense
    - setExposure has option to specify time in milliseconds or
      cycles
    - recognize serial timeouts:
        - add status value 'TIMEOUT'
        - issue a warning when a timeout occurs
- improve documentation:
    - add custom docstrings with examples
    - show type hints and default values in command function
      signatures 

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

