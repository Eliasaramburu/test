from flask import Blueprint, render_template, redirect, url_for, request

calcular_route = Blueprint("calcular", __name__)

def calcular_imposto(valor_nf, aliquota):
    imposto = valor_nf * aliquota / 100
    return imposto

@calcular_route.route("/calcular", methods=["POST"])
def calcular():
    try:
        # Obter dados do formulário via POST
        aliquota = float(request.form["aliquota"])
        valor_nf = float(request.form["valor_nf"])

        # Calcular o imposto
        imposto = calcular_imposto(valor_nf, aliquota)

        print(f"Imposto calculado: {imposto}")  # Verificar o valor calculado

        # Verifique a URL gerada antes de redirecionar
        redirect_url = url_for("resultado.resultado", imposto=imposto)
        print(f"Redirecionando para: {redirect_url}")  # Verificando a URL gerada

        # Redireciona para a página de resultados
        return redirect(redirect_url)

    except Exception as e:
        print(f"Erro ao calcular imposto: {e}")
        # Em caso de erro, redireciona de volta para a página de resultados com uma mensagem
        return redirect(url_for("resultado.resultado"))
