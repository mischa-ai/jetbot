import smbus

# Define the I2C address of the motor driver board
MOTOR_DRIVER_ADDR = 0x14

# Define the registers for the motor driver board
REG_MODE1 = 0x00
REG_MODE2 = 0x01
REG_PWM_A = 0x02
REG_PWM_B = 0x03
REG_PWM_FREQ = 0xfe

# Initialize the I2C bus
bus = smbus.SMBus(1)

# Set the PWM frequency to 100Hz
bus.write_byte_data(MOTOR_DRIVER_ADDR, REG_PWM_FREQ, 0x64)

# Set the motor speed (0-255) and direction (1 or -1)
def set_motor_speed(motor, speed):
    if speed > 0:
        dir = 0x01
    else:
        dir = 0x02
    if motor == 1:
        reg_pwm = REG_PWM_A
    else:
        reg_pwm = REG_PWM_B
    bus.write_byte_data(MOTOR_DRIVER_ADDR, reg_pwm, abs(speed))
    bus.write_byte_data(MOTOR_DRIVER_ADDR, reg_pwm+1, dir)

# Example usage:
# set_motor_speed(1, 100) # set motor 1 speed to 100 (forward)
# set_motor_speed(2, -50) # set motor 2 speed to -50 (reverse)
