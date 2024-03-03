import serial

port = 'COM3'
baud_rate = 9600

try:
    ser = serial.Serial(port, baudrate=baud_rate)
    print(f"Conectat la portul {port} cu rata de {baud_rate} baud")


except serial.SerialException as e:
    print(f"Eroare la conectarea la portul {port}: {e}")

except KeyboardInterrupt:
    print("Închidere program...")

finally:
    # Închiderea conexiunii seriale
    ser.close()
    print("Conexiune serială închisă.")
