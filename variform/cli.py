import defopt

def subcommand():
    pass

def main(argv=None):
    defopt.run({
        "sub-command": subcommand}, argv=argv)
    
