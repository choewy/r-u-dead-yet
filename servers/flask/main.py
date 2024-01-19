from app import Application
from module import RootModule


if __name__ == "__main__":
  Application(3000, '::').register_blueprints(
    RootModule.blueprint
  ).listen()
