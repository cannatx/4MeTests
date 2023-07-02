import argparse

# """
# (venv) PS C:\Users\ng71cd8\Documents\__Devs\Tests> python .\python_path\parse_args_argparser.py -display "full_color"
# full_color
# """
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--display", required=True, help="Set display")
args = parser.parse_args()

display = args.display
print(display)
