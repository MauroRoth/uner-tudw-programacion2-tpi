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
        descripciones = [
            'Primer Recurso: Obtiene una bodega determinada por su id, sabemos de ella su nombre, las cepas y los vinos que contiene.',
            'Segundo Recurso: Obtiene una cepa determinada por su id, sabemos de ella su nombre, y los vinos que la contienen con sus respectivas bodegas.',
            'Tercer Recurso: Obtiene un vino determinado por su id, sabemos de él su nombre, la bodega a la que pertenece, las cepas y partidas en las que se ofrece.',
            'Cuarto Recurso: Obtiene los vinos, sus id, sus nombres, las cepas y partidas de los mismos. Si entre las partidas se encuentra el año 2020 y ordenándolos según su nombre de manera directa.',
            'Cuarto Recurso: Obtiene los vinos, sus id, sus nombres, las cepas y partidas de los mismos. Si entre las partidas se encuentra el año 2020 y ordenándolos según su nombre de manera indirecta.'
        ]
        recursos_solicitados = zip(descripciones,urls)
        otras_urls = [
            'http://127.0.0.1:5000/api/bodegas',
            'http://127.0.0.1:5000/api/cepas',
            'http://127.0.0.1:5000/api/vinos',
            'http://127.0.0.1:5000/api'
            ]
        otras_descripciones = [
            'Primer Recurso: Obtiene todas las bodegas, sus id, sus nombres, sus cepas y la cantidad de vinos que posee. ',
            'Segundo Recurso: Obtiene todas las cepas, sus id, sus nombres y la cantidad de vinos en los que está presente. ',
            'Tercer Recurso: Obtiene todos los vinos, sus id, sus nombres, la bodega a la que pertenece, las cepas y las partidas que tiene. ',
            'Cuarto Recurso: Obtiene todos los datos del JSON.'
        ]
        otros_recursos = zip(otras_descripciones,otras_urls)
        bodegas_titulo = (list(Vinoteca.obtenerTodos().keys()))[0]
        cepas_titulo = (list(Vinoteca.obtenerTodos().keys()))[1]
        vinos_titulo = (list(Vinoteca.obtenerTodos().keys()))[2]

        bodegas = Vinoteca.obtenerBodegas()
        cepas = Vinoteca.obtenerCepas()
        vinos = Vinoteca.obtenerVinos()

        return render_template(
            'index.html', 
            titulo = 'VINOTECA', 
            subtitulo1 =' Recursos Solicitados', 
            recursos_solicitados = recursos_solicitados,
            subtitulo2 = 'Otros Recursos',
            otros_recursos = otros_recursos,
            subtitulo3 = 'Algunos Datos Tabulados',
            bodegas_titulo = bodegas_titulo,
            cepas_titulo = cepas_titulo,
            vinos_titulo = vinos_titulo,
            bodegas = bodegas,
            cepas = cepas,
            vinos = vinos)
    
    # API RESTful
    api = Api(app)
    api.add_resource(RecursoTodos, '/api/')
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')

    app.run(debug=True)

    