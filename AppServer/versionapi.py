import os.path
import os
import yaml
import logging
 
from flask import Blueprint
from middleware import github_read_file
bp = Blueprint('versionapi',__name__,url_prefix='/<string:envID>')


@bp.route("/", methods=['GET'])
def getEnv(envID):
    logging.info('GET /<string:envID>')
    github_token = os.environ['GITHUB_TOKEN']
    username = os.environ['GITHUB_USER']
    repository_name = envID
    file_path = 'env/requirements.yaml'
    file_content = github_read_file(username, repository_name, file_path, github_token=github_token)
    data = yaml.safe_load(file_content)
    return data
