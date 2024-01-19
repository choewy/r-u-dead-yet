from flask import request
from core import ResponseDto
from module.root.root_module import RootModule

router = RootModule.blueprint.route


class RootController:
  @staticmethod
  @router("/", methods=["GET"])
  def get():
    return ResponseDto.ok(200, "Root")
  
  @staticmethod
  @router('/', methods=["POST"])
  def post():
    return ResponseDto.ok(201, request.form)