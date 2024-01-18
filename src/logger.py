import sys


class Logger:
  def verbose(self, message, transport=sys.stdout):
    print(f"[VERBOSE] {message}", file=transport)

  def warn(self, message, transport=sys.stderr):
    print(f"[WARNING] {message}", file=transport)

  def error(self, message, transport=sys.stderr):
    print(f"[ERROR] {message}", file=transport)
