import RPi.GPIO as GPIO
import time

# Configuración de pines (BCM)
TRIG = 23
ECHO = 24

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(2)  # Estabilizar sensor

def medir_distancia():
    # Enviar pulso de disparo
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)  # 10 µs
    GPIO.output(TRIG, GPIO.LOW)

    # Medir tiempo de eco con alta precisión
    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()  # time.time() ya usa alta resolución

    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()

    # Cálculo con más decimales
    pulse_duration = pulse_end - pulse_start
    distancia = (pulse_duration * 34300) / 2  # 34300 cm/s
    return distancia

if __name__ == "__main__":
    try:
        setup()
        while True:
            dist = medir_distancia()
            print(f"Distancia: {dist:.3f} cm")  # Ahora muestra 3 decimales
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nPrograma detenido")
    finally:
        GPIO.cleanup()
