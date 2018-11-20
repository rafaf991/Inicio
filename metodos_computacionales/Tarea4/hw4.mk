Resultados_hw4.pdf: Resultados_hw4.tex condicionesfinales.pdf condicionesiniciales.pdf condicionesmitad.pdf ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png
	pdftex ./Resultados_hw4.tex

condicionesfinales.pdf condicionesiniciales.pdf condicionesmitad.pdf ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png ('Trayectoria', 45, ' grados').png: Plots_hw4.py 10 20 30 40 45 50 60 70 Eccalor.txt
	python Plots_hw4.py
10 20 30 40 45 50 60 70 Eccalor.txt: PDE.cpp ODE.cpp
	g++ PDE.cpp
	./a.out
	g++ ODE.cpp
	./a.out
