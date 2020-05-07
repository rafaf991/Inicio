wget https://raw.githubusercontent.com/daniel-lozano/CLASES_PYTHON/master/CLASE1/HERRAMIENTAS/notas.txt

touch RES1.txt

awk '{if($3 > 4) print $0}' notas.txt| wc |awk '{print "hay ",$1-1, "estudiantes con nota superior a 4"}' > RES1.txt
awk '{if($3 > 4) print $0}' notas.txt|awk '{if ($6 > 15) print $1-1}' |wc |awk '{print "entre ellos,"$1, "tuvieron mas de 15 en el final"}' >> RES1.txt
echo "Los estudiantes con un cero y que perdieron la materia son:"
grep -w "0" notas.txt | awk '{if ($7<6) print $1 ,$2}'

touch RES2.txt
echo "Los estudiantes con nota final mayor a 8 son:" > RES2.txt

awk '{if($7> 8 && $7 != "Puntos" && $7 != "Laboratorios") print $1,$2}' notas.txt >> RES2.txt

cat RES2.txt
