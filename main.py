# Flask
from flask import Flask, render_template
from flask_restful import Api

from vinoteca import Vinoteca

# API
from recursos import *

if __name__ == "__main__":
    
    Vinoteca.inicializar()

    app = Flask(__name__)

    @app.route("/")
    def home():
        urls = [
            'http://127.0.0.1:5000/api/bodegas/a0900e61-0f72-67ae-7e9d-4218da29b7d8',
            'http://127.0.0.1:5000/api/cepas/33ccaa9d-4710-9942-002d-1b5cb9912e5d',
            'http://127.0.0.1:5000/api/vinos/4823ad54-0a3a-38b8-adf6-795512994a4f',
            'http://127.0.0.1:5000/api/vinos?anio=2020&orden=nombre&reverso=no',
            'http://127.0.0.1:5000/api/vinos?anio=2020&orden=nombre&reverso=si',
            ]
        return render_template('index.html', title='VINOTECA', urls=urls)
    
    # API RESTful
    api = Api(app)
    api.add_resource(RecursoTodos, '/api/')
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')
#
    app.run(debug=True)

    