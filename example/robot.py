import magicbot
import wpilib
from wpilib.interfaces.generichid import GenericHID

import marsutils
from marsutils.decorator import *

import drive


class JoystickControl(marsutils.ControlInterface):
    """
        Implements control via a joystick
    """

    _DISPLAY_NAME: str = "Joystick Control"

    stick: wpilib.Joystick

    drive: drive.Drive

    def teleopPeriodic(self):
        self.drive.drive(-self.stick.getY(), self.stick.getZ())


@with_ctrl_manager
@provide_setup
class MyRobot(magicbot.MagicRobot):
    drive: drive.Drive
    stick_control: JoystickControl

    def createObjects(self):
        self.stick = wpilib.Joystick(0)

        self.l_motor = wpilib.Spark(1)
        self.r_motor = wpilib.Spark(2)

    def setup(self):
        print("Setup called")


if __name__ == "__main__":
    wpilib.run(MyRobot)
