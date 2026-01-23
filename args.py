import argparse #library

# parser obj
parser = argparse.ArgumentParser()

# use object and add arguments

# parser.add_argument("echo",help="echoes the string you use here")
parser.add_argument("square",type=int,help="display a square of a given number")

# use parser to parse arguments and store them in args
args = parser.parse_args()

# print(args.echo)
print(args.square**2)

