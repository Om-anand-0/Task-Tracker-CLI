import argparse  # library

# parser obj
parser = argparse.ArgumentParser(description="Task Tracker CLI")

# use object and add arguments

parser.add_argument(
    "action",
    choices=[
        "add",
        "show",
        "delete",
        "mark",
        "done",
        "undone",
        "inprogress",
        "list",
        "clear",
        "exit",
    ],
)
parser.add_argument("value", nargs="?", help="Task id or task text")
parser.add_argument("--file", default="tasks.json", help="File name to use (default: tasks.json)")


# use parser to parse arguments and store them in args
args = parser.parse_args()

