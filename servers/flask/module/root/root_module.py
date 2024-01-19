from flask import Blueprint


class RootModule:
  blueprint = Blueprint('root', __name__, url_prefix='/')
