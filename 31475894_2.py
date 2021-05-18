from urllib2 import *
from bs4 import BeautifulSoup
import re

#pattern = re.compile(r'([A-Z])([A-Z]))

txtfile = open("PythonTextFile.txt", "a+")

lt = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in range(len(lt)):
	for j in range(len(lt)):
		print(lt[i] + lt[j])
		url = "https://en.wikipedia.org/wiki/" + lt[i] + lt[j]
		file = urlopen(url)
		str_html = file.read()
		obj_html = BeautifulSoup(str_html, "html.parser")
		for element in obj_html(["script", "style"]):
    			element.extract()
		str_text = obj_html.get_text()
		txtfile.write(str_text)
txtfile.close()
regex = ""


