#!/usr/bin/env python3
'''''''''''''''''''''''''''''
COPYRIGHT LESTERRRY,
2022

'''''''''''''''''''''''''''''
import sys
from PIL import Image
from tqdm import tqdm
import os

RED = "\033[31m"
GRN = "\033[32m"
ORG = "\033[33m"
CYN = "\033[36m"
BLD = "\033[1m"
RES = "\033[0m"

def my_except_hook(exctype, value, traceback):
	print(f'{RED + BLD}ERROR:{RES} {value}')
	exit(1)
sys.excepthook = my_except_hook

argv = sys.argv
if len(argv) != 5:
	raise ValueError("erroneous arguments: expected <PATH> <R> <G> <B>")
path = argv[1]
r, g, b = [int(i) for i in argv[2:]]

def handle_image(path_to_image, r, g, b, strict):
	image = Image.open(path_to_image)
	if image.mode != "RGBA":
		raise ValueError("image lacks alpha") if strict else None
	else:
		bg = Image.new("RGBA", image.size, (r, g, b, 255))
		alpha_composite = Image.alpha_composite(bg, image)
		alpha_composite.save(path_to_image)

def has_hidden_attribute(filepath):
	try:
		assert attrs != -1
		result = bool(attrs & 2)
	except (AttributeError, AssertionError):
		result = False
	return result

if os.path.isfile(path):
	handle_image(path, r, g, b, True)
	print(f"{GRN + BLD}SUCCESSFULLY{RES} replaced alpha channel")
elif os.path.isdir(path):
	files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and not f.startswith('.')]
	for i in tqdm(range(len(files))):
		handle_image(files[i], r, g, b, False)
else:
	raise ValueError("neither a file nor a directory")
