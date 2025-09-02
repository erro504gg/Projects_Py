# pip install flask
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Calculadora</title>
<h2>Calculadora Simples</h2>
<form method="post">
  Número 1: <input type="number" step="any" name="n1" required><br>
  Operação:
  <select name="opcao">
    <option value="1">Somar</option>
    <option value="2">Dividir</option>
    <option value="3">Multiplicar</option>
    <option value="4">Diminuir</option>
  </select><br>
  Número 2: <input type="number" step="any" name="n2" required><br>
  <input type="submit" value="Calcular">
</form>
{% if resultado is not none %}
  <h3>Resultado: {{ resultado }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def calculadora():
    resultado = None
    if request.method == "POST":
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        opcao = request.form["opcao"]
        if opcao == "1":
            resultado = n1 + n2
        elif opcao == "2":
            if n2 == 0:
                resultado = "Não é possível dividir por zero."
            else:
                resultado = n1 / n2
        elif opcao == "3":
            resultado = n1 * n2
        elif opcao == "4":
            resultado = n1 - n2
    return render_template_string(HTML, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)   