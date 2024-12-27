from flask import Blueprint, render_template, request, url_for

icms_route = Blueprint("icms",__name__)

# Função para calcular o imposto
def calcular_imposto(valor_nf, aliquota):
    return valor_nf * (aliquota / 100)

@icms_route.route('/', methods=["GET"])
def index():
    # Página inicial com o formulário
    return render_template("index.html")

