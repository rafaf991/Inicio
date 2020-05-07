#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;
int main(){

  //Constantes
  double dx,dt,k,c,rho,tfin,a;
  int maxx,maxt;
  dx=0.03;
  k=210;
  c=900;
  rho=2700;
  maxx=101;
  tfin=3000;


  //Sacar dt
  a=2.1;
  dt=dx*dx*c*rho/(k*a);
  maxt=ceil(tfin/dt);
  cout<<maxt<<endl;
  double p[maxx][maxt];

  //Inicializo la matriz
  for (int i = 0; i < maxt; i++) {
    p[0][i]=50;
    p[maxx-1][i]=0;
  }

  for (int i = 0; i < maxt; i++) {

    for (int j = 0; j < maxx; j++) {
      if(j==0) {

      }
      else if(j==maxx-1) {

      }
      else{p[j][i]=100;}
      //cout<<p[j][i]<<" ";
    }
  //cout<<endl;
  }


ofstream file;
file.open("eccalor.txt");

  //Asigno cada P
  double eta;
  eta=k*dt/(c*rho*dx*dx);
  for (int i = 0; i < maxt; i++) {
    for (int j = 0; j < maxx; j++) {
      if(j!=0 && j!=maxx-1){
      p[j][i+1]=p[j][i]+eta*(p[j+1][i]+p[j-1][i]-2*p[j][i]);}
      file<<p[j][i]<<" ";
    }
    file<<endl;
  }
file.close();




  return 0;
}
