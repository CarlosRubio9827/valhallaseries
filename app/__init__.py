from flask import Flask
app = Flask(__name__, static_folder='../static')

def create_app():

    app.config['SECRET_KEY'] = 'nauralseries2021'
    

    # Registro de los Blueprints
    # BluePrint Carrera
    from .carrera import carrera
    app.register_blueprint(carrera)
    # BluePrint Entreno
    from .entreno import entreno
    app.register_blueprint(entreno)
    # BluePrint KmVertical
    from .kmvertical import kmvertical
    app.register_blueprint(kmvertical)
    # BluePrint Private
    from .private import private
    app.register_blueprint(private)
    # BluePrint Public
    from .public import public
    app.register_blueprint(public)
    
    
    return app