from flask import jsonify


class ResponseDto:
  def __init__(self, ok: bool, status: int, data: any):
    self.ok = ok
    self.status = status
    self.data = data

  def __json__(self):
    return {
      "ok": self.ok,
      "status": self.status,
      "data": self.data
    }

  @staticmethod
  def ok(status: int, data: any):
    return jsonify(ResponseDto(True, status, data).__json__())

  @staticmethod
  def fail(status: int, data: any):
    return jsonify(ResponseDto(False, status, data).__json__())