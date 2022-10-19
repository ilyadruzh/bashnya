# import default libraries that are used in this example
import time

# import the library
from raspberry_i2c_tb6612fng import MotorDriverTB6612FNG, TB6612FNGMotors

# create an instance of the driver, connected to i2c
driver = MotorDriverTB6612FNG()

# drive both motors forward
driver.dc_motor_run(TB6612FNGMotors.MOTOR_CHA, 200)
driver.dc_motor_run(TB6612FNGMotors.MOTOR_CHB, 200)

# pause for a second
time.sleep(1)

# stop the motors
driver.dc_motor_break(TB6612FNGMotors.MOTOR_CHA)
driver.dc_motor_break(TB6612FNGMotors.MOTOR_CHB)