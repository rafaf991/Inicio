display: graf.py eccalor.txt
	python graf.py
eccalor.txt: eccalor.cpp
	g++ eccalor.cpp
	./a.out
