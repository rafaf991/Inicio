#include <iostream>
#include <fstream>
#include <cmath>


using namespace std;

int main(){
  //Ecuacion de calor
  double C,p,k,nu;
  C=820;
  p=2.71;
  k=1.62;
  nu=k/(C*p);

  double xmax,ymax,tmax,dx,dt,temperatura_inicial;
  int maxt,maxx,maxy;
  xmax=50;//cm
  ymax=50;//cm
  tmax=1000;
  //Asumiendo dx=dy;
  dx=0.01;
  dt=0.01;
  maxx=ceil(xmax/dx);
  maxy=ceil(ymax/dx);
  maxt=ceil(tmax/dt);
  temperatura_inicial=0;


  double*** T=new double** [maxx];
  for (int i = 0; i < maxx; i++) {
    T[i]=new double* [maxy];
    for (int j = 0; j < maxy; j++) {
      T[i][j]=new double [maxt];
    }
  }
  int liminf,limsup;
  liminf=20/dx;
  limsup=30/dx;
  //Inicializando T;

  for (int i = 0; i <maxx; i++) {
    for (int j = 0; j < maxy; j++) {
      if(j<=limsup && j>=limsup){
        T[i][j][0]=100;
      }
      else T[i][j][0]=temperatura_inicial;
    }
  }

  for (int j = 0; j < maxt; j++) {


    for (int m = 0; m < maxx; m++) {
      int n=m;
      //Condicion:
      T[m][n][j+1]=T[m][n][j]+nu*(dt/pow(dx,2))*(T[m+1][n][j]-T[m-1][n][j]+T[m][n+1][j]-T[m][n-1][j]-4*T[m][n][j]);

    }


  }



  return 0;
}
