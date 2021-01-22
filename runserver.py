from flask import Flask
from optparse import OptionParser
from digiez_api import app

# def create_app(config_filename):
#     app = Flask(__name__)
#     app.config.from_object(config_filename)
#
#     from app import api_bp
#     app.register_blueprint(api_bp, url_prefix='/api')
#
#     from Model import db
#     db.init_app(app)
#     return app


if __name__ == "__main__":
    # app = create_app("config")
    # app.run(debug=True)
    # Run with docker
    parser = OptionParser()
    parser.add_option("-d", "--debug", dest="debug", default=False,
                      action="store_true", help="Use debug option")
    options, args = parser.parse_args()
    app.run(debug=options.debug, host='0.0.0.0',
            port=5001)
