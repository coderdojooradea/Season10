import time
import pandas as pd

# Funcția care simulează citirea în timp real a datelor din fișierul CSV
def citeste_date_in_timp_real(csv_path, frecventa_per_secunda):
    # Citirea datelor din CSV
    df = pd.read_csv(csv_path)
    
    # Calcularea pauzei între citiri pentru a simula frecvența de 10 date pe secundă
    pauza = 1 / frecventa_per_secunda
    
    for index, row in df.iterrows():
        # Returnează o înregistrare ca și cum ar fi o citire
        yield f"Timestamp: {row['Timestamp']}, Temperatura: {row['Temperatura']:.2f}°C"
        
        # Pauză pentru a simula frecvența de citire
        time.sleep(pauza)


csv_path='date_senzor_temperatura.csv'
frecventa_per_secunda = 10
# Apelarea funcției pentru a simula citirea datelor
citiri = citeste_date_in_timp_real(csv_path, frecventa_per_secunda)

for _ in range(20):
    print(next(citiri))
