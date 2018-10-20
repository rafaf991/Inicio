display: xt.png
	display xt.png

xt.png: graf.py graf.txt
	python graf.py
graf.txt : rafS10C2.cpp
	g++ -o output rafS10C2.cpp
	./output
clean:
	rm *.png
