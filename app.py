from flask import Flask, request, send_file, jsonify, render_template
import json
from gerar_word import gerar

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.post("/gerar-word")
def gerar_word():
    try:
        file = request.files.get("planejamento")
        data = json.loads(file.read().decode("utf-8"))

        if "semana_inicio" not in data:
            data["semana_inicio"] = ""
        if "semana_fim" not in data:
            data["semana_fim"] = ""

        output = gerar(data)

        return send_file(output, as_attachment=True, download_name="Planejamento.docx")

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
