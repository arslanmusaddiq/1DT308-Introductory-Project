from machine import PWM

pwm = PWM(0, frequency=100)  # use PWM timer 0, with a frequency of 100Hz

# create pwm channel on pin P12 with a duty cycle of 50%

pwm_c = pwm.channel(0, pin='P12', duty_cycle=1)

#pwm_c.duty_cycle(0.5) # change the duty cycle to 30%
