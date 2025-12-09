from flask import Flask, request

app = Flask(__name__)

def konversi_ke_tahun_jepang(tahun):
    tahun = int(tahun)
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

    tahun_jepang_str = "Gannen" if tahun_jepang == 1 else str(tahun_jepang)
    return f"{era} {tahun_jepang_str}"

@app.route("/")
def home():
    tahun = request.args.get("year")

    if tahun:
        result = konversi_ke_tahun_jepang(tahun)
        return f"Hasil: {result}"

    return """
    <h2>Konversi tahun Masehi ke tahun Jepang</h2>
    <form>
        <input type='number' name='year' placeholder='Masukkan tahun Masehi'>
        <button type='submit'>Konversi</button>
    </form>
    """
return "Python ini berjalan di Render, ditulis oleh H Gunarto! \n Thanks."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

# yang lama untuk check:
# @app.route("/")
# def home():
  #  return "Python ini berjalan di Render, ditulis oleh H Gunarto! \n Thanks."
