from flask import Flask, render_template, request, redirect, url_for
from routes.icms import icms_route
from routes.calcular import calcular_route
from routes.resultado import resultado_route

app = Flask(__name__)

app.register_blueprint(icms_route)
app.register_blueprint(calcular_route)
app.register_blueprint(resultado_route)

if __name__ == "__main__":
    app.run(debug=True)
