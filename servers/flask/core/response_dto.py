import json

from flask import Response


class ResponseDto(Response):
  def __init__(self, ok: bool, status: int, data: any = None):
    Response.__init__(self, json.dumps({
      "ok": ok,
      "status": status,
      "data": data,
    }), status=status, mimetype="application/json")