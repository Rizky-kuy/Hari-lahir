from datetime import datetime

def get_birth_day(date_string):
    # Konversi input string ke format tanggal
    date_format = "%d-%m-%Y"  # Format: DD-MM-YYYY
    birth_date = datetime.strptime(date_string, date_format)
    
    # List nama hari dalam bahasa Indo
    days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    
    # Mengambil indeks hari dari tanggal lahir
    birth_day = days[birth_date.weekday()]
    
    return birth_day

# Contoh menggunakannya
tanggal_lahir = input("Masukkan tanggal lahir (DD-MM-YYYY): ")
hari_lahir = get_birth_day(tanggal_lahir)
print(f"Kamu lahir pada hari {hari_lahir}.")
