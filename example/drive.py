import wpilib
import wpilib.drive


class Drive:
    l_motor: wpilib.Spark
    r_motor: wpilib.Spark

    def setup(self):
        self.drive_train = wpilib.drive.DifferentialDrive(self.l_motor, self.r_motor)

        self.y = self.rotation = 0
        self.squared = True

    def drive(self, y, rot, squared=True):
        self.y = y
        self.rotation = rot
        self.squared = squared

    def execute(self):
        self.drive_train.arcadeDrive(self.y, self.rotation, self.squared)

        self.y = 0
        self.rotation = 0
