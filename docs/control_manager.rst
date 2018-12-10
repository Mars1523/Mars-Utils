Control Manager
===============

:class:`.ControlManager` was created to reduce the amount of boiler plate when
creating multiple "control modes" for a robot.  Essentially, each driver wants
their own set of controls.  For ``MagicRobot`` is is very easy, as each
controlmanager mode can be a component that then has variables injected.
However, adding all the control modes to the dashboard with a nice chooser,
detecting and handling changes can lead to a lot of boilerplate.

:class:`.ControlManager` allows us to reduce boilerplate by subclassing
:class:`.ControlInterface` and then initializing :class:`.ControlManager`
with the control interfaces, and it creates the chooser.

For even more code reducing magic, see :func:`.decorator.with_ctrl_manager`
which when used with ``MagicRobot``, completely removes all boilerplate
by managing the creation of a :class:`ControlManager` and dispatching event
calls.

.. autoclass:: marsutils.controlmanager.ControlInterface
    :members:
    :undoc-members:
    :show-inheritance:

.. automodule:: marsutils.controlmanager
    :members:
    :exclude-members: ControlInterface
