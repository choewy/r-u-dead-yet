from src import Command, Args, Rudy


if __name__ == "__main__":
  cli = Command()
  args = Args(cli.parse_args())
  rudy = Rudy(args).run()
