from Raspi_MotorHAT import Raspi_MotorHAT
mh = Raspi_MotorHAT(addr=0x6f)
motor = mh.getMotor(1)

motor.setSpeed(150)

motor.run(Raspi_MotorHAT.FORWARD)
