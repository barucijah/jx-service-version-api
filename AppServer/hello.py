from flask import Blueprint
import logging

bp = Blueprint('hello',__name__,url_prefix='/')

@bp.route("/", methods=['GET'])
def hello():
    logging.info('GET /')
    return '' 