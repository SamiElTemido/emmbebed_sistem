import RPi.GPIO as GPIO
import time

# Configuración
TRIG = 23
ECHO = 24
ARCHIVO = "distancias.txt"  # Archivo de salida

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(2)

def medir_distancia():
    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == GPIO.LOW:
        pulse_start = time.time()
    while GPIO.input(ECHO) == GPIO.HIGH:
        pulse_end = time.time()

    return round((pulse_end - pulse_start) * 17150, 2)  # Distancia en cm con 2 decimales

if __name__ == "__main__":
    try:
        setup()
        with open(ARCHIVO, "a") as file:
            while True:
                    distancia = medir_distancia()
                    if distancia<500:
                        file.write(f"{distancia}\n")  # Solo guarda el número
                        file.flush()
                        print(f"Registrado: {distancia} cm")  # Feedback en consola
                    else:
                        print(f"Dato no registrado: {distancia} cm")  # Feedback en consola

                    time.sleep(1)  # Intervalo entre mediciones

    except KeyboardInterrupt:
        print("\nMedición detenida")
    finally:
        GPIO.cleanup()
