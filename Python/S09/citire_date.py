import time
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Inițializează listele pentru a stoca datele de plotat
x_data, y_data = [], []

# Crează figura și axa pentru plotare
fig, ax = plt.subplots()
ax.set_xlim(0, 1000)  # Ajustează aceste limite după necesități
ax.set_ylim(20, 30)  # Presupunând că temperaturile sunt între 20 și 30 grade Celsius

# Inițializează o linie de plotare
line, = ax.plot([], [], lw=2)

# Funcția care simulează citirea în timp real a datelor din fișierul CSV
def citeste_date_in_timp_real(csv_path, frecventa_per_secunda):
    # Citirea datelor din CSV
    df = pd.read_csv(csv_path)
    
    # Calcularea pauzei între citiri pentru a simula frecvența de 10 date pe secundă
    pauza = 1 / frecventa_per_secunda
    
    for index in range(len(df)):
        # Returnează o înregistrare ca și cum ar fi o citire
        yield index, df.iloc[index]['Temperatura']
        
        # Pauză pentru a simula frecvența de citire
        time.sleep(pauza)

def update(frame):
    try:
        x, y = next(citiri)
        x_data.append(x)
        y_data.append(y)
        
        line.set_data(x_data, y_data)
    except StopIteration:
        pass  # Dacă generatorul nu are mai multe valori, nu face nimic
    return line,


csv_path='date_senzor_temperatura.csv'
frecventa_per_secunda = 10
# Apelarea funcției pentru a simula citirea datelor
citiri = citeste_date_in_timp_real(csv_path, frecventa_per_secunda)

# Crează animația
ani = FuncAnimation(fig, update, blit=True, interval=100)

plt.show()
