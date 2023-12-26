def handleJsonFile(filepath):
	content=__import__(json).loads(open(filepath).read())
	__import__("os").system(f"del {filepath}")
	return content
print(handleJsonFile(input("Path: ") if len(__import__("sys").argv)==1 else __import__("sys").argv[1]))