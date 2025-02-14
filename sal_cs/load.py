from os.path import split

_sample = split(__file__)[0] + "/sample.txt"

def load(fileName=_sample):
	try:
		with open(fileName, encoding="UTF-8") as f:
			txt = f.read()
	except Exception as e:
		txt = str(e)
	return txt
