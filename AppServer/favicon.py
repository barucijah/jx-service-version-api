from flask import Blueprint
from flask import send_from_directory
import os
import logging

bp = Blueprint('favicon',__name__,url_prefix='/favicon.ico')

@bp.route('/') 
def favicon():
    logging.info('GET /favicon.ico') 
    return send_from_directory(os.path.join(bp.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')