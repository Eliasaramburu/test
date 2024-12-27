from flask import Blueprint, render_template, request

resultado_route = Blueprint("resultado", __name__)

@resultado_route.route("/resultado", methods=["GET"])
def resultado():
    # Obter o imposto da query string via GET
    imposto = request.args.get("imposto", "Valor não disponível")  # Se não houver parâmetro, mostra mensagem

    print(f"Imposto recebido: {imposto}")  # Exibir valor no terminal

    return render_template("resultado.html", imposto=imposto)
