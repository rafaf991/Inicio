wget https://raw.githubusercontent.com/daniel-lozano/CLASES_PYTHON/master/CLASE1/HERRAMIENTAS/notas.txt
touch contador.txt
touch contador2.txt
touch RES1.txt

awk '{if($4 >4) print 2 }' notas.txt > contador.txt
wc contador.txt> contador2.txt
awk '{print "hay",$1,"estudiantes con nota superior a 4" }' contador2.txt > RES1.txt
rm -rf contador.txt
rm -rf contador2.txt
touch contador.txt
touch contador2.txt
awk '{if($4 > 4) print $0}' notas.txt | awk '{if($6 > 15) print $0}' notas.txt > contador.txt

wc contador.txt > contador2.txt
awk '{print "hay",$1,"estudiantes con nota superior a 15 en el final" }' contador2.txt >>RES1.txt 

