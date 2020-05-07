display: xt.png
	display xt.png

xt.png: graf.py graf.txt graf2.txt graf3.txt
	python graf.py
graf.txt graf2.txt graf3.txt: test.cpp
	g++ -o output test.cpp
	./output
clean:
	rm *.png
