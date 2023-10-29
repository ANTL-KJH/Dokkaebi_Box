"""
* Project : 2023 Seoul AIOT Hackathon
* Program Purpose and Features :
* - class ServoMotor
* Author : JH KIM
* First Write Date : 2023.11.03
* ==========================================================================
* Program history
* ==========================================================================
* Author    		Date		    Version		History
* JH KIM            2023.11.03		v1.00		First Write
"""
import RPi.GPIO as GPIO
import time
from ServoConstant import *
GPIO.setwarnings(False)

SERVO_MAX_DUTY    = 12   # 서보의 최대(180도) 위치의 주기
SERVO_MIN_DUTY    = 3    # 서보의 최소(0도) 위치의 주기

class ServoMotor:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BOARD)  # 핀의 번호를 보드 기준으로 설정, BCM은 GPIO 번호로 호출함
        GPIO.setup(pin, GPIO.OUT)  # GPIO 통신할 핀 설정
        self.pwm = GPIO.PWM(self.pin, SERVO_DEFAULT_FREQ)  # 서보모터는 PWM을 이용해야됨. 16번핀을 50Hz 주기로 설정
        self.pwm.start(5)  # 초기 시작값, 반드시 입력해야됨
        time.sleep(1)  # 초기 시작값으로 이동하고 싶지 않으면 이 라인을 삭제하면 된다.

    def setAngle(self, degree, t):   # 각도와 움직일 시간 입력
        duty = SERVO_MIN_DUTY + (degree * (SERVO_MAX_DUTY - SERVO_MIN_DUTY) / 180.0)
        self.pwm.ChangeDutyCycle(duty)  # 보통 2~12 사이의 값을 입력하면됨
        time.sleep(t)  # 서보모터가 이동할만큼의 충분한 시간을 입력. 너무 작은 값을 입력하면 이동하다가 멈춤



def main():
    servo = ServoMotor(SERVO_DEFAULT_PIN)
    while True:
        servo.setAngle(0, 2) # 0도
        servo.setAngle(100, 2)  # 90도
if __name__ == "__main__":
    main()
