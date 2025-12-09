from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Python ini berjalan di Render, ditulis oleh H Gunarto! <br> Thanks."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
# ------------------------

def konversi_ke_tahun_jepang(tahun):
    if tahun >= 2019:
        era = "Reiwa"
        tahun_jepang = tahun - 2018
    elif tahun >= 1989:
        era = "Heisei"
        tahun_jepang = tahun - 1988
    elif tahun >= 1926:
        era = "Shōwa"
        tahun_jepang = tahun - 1925
    elif tahun >= 1912:
        era = "Taishō"
        tahun_jepang = tahun - 1911
    elif tahun >= 1868:
        era = "Meiji"
        tahun_jepang = tahun - 1867
    else:
        return "Tahun sebelum 1868 belum didukung."

    # Tahun 1 disebut "Gannen" dalam budaya Jepang
    tahun_jepang_str = "Gannen" if tahun_jepang == 1 else str(tahun_jepang)
    return f"{era} {tahun_jepang_str}"


# ===============================
# Contoh penggunaan
# ===============================

while True:
    try:
        tahun = int(input("Masukkan tahun Masehi: "))
        print("→", konversi_ke_tahun_jepang(tahun))
    except:
        print("Input tidak valid.")



# print("Hello from Render!")
