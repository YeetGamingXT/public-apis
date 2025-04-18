from flask import Flask, request, jsonify

app = Flask(__name__)

# Pravilni odgovori – vrstni red ni pomemben
pravilni_odgovori = {"kit", "netopir"}

@app.route('/preveri-odgovore', methods=['POST'])
def preveri_odgovore():
    podatki = request.get_json()
    poslani_odgovori = set(podatki.get('odgovori', []))

    if poslani_odgovori == pravilni_odgovori:
        rezultat = "Pravilno!"
    else:
        rezultat = f"Napačno. Poskusite znova."

    return jsonify({'rezultat': rezultat})

if __name__ == '__main__':
    app.run(debug=True)
