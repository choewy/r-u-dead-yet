from rudy import Command, Args, Rudy


if __name__ == "__main__":
  try:
    cli = Command()
    args = Args(cli.parse_args())
    rudy = Rudy(args).run()
  except KeyboardInterrupt:
    pass
