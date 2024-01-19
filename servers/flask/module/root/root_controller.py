from flask import request
from core import ResponseDto
from module.root.root_module import RootModule

router = RootModule.blueprint.route


class RootController:
  @staticmethod
  @router("/", methods=["GET"])
  def get():
    return ResponseDto(True, 200, "Root")
  
  @staticmethod
  @router("/", methods=["POST"])
  def post():
    return ResponseDto(True, 201)