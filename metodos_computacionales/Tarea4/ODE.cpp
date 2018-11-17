#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

double g[2];

double c=0.2;
double m=0.2;
double angulo=45;



double func2(double x,double* y,int i);

double func1(double x,double* y,int i );

int main(){
//Vamos a resolver la ecuacion ddx/ddt = -g -c|v|v/m
  //Condiciones iniciales:
  double v0,h,tmax;
  int n;
  v0=300;
  g[0]=10;
  g[1]=0;
  tmax=10;
  h=0.01;
  n=tmax/h;

  double** x=new double* [n];
  for (int i = 0; i < 2; i++) x[i]=new double[2];

  double** v=new double *[n];
  for (int i = 0; i < 2; i++) v[i]=new double[2];

  double t[n];
  for (int i = 0; i < n; i++) t[i]=h*i;


  v[0][0]=v0*cos(angulo);
  v[0][1]=v0*sin(angulo);
  x[0][0]=0;
  x[0][1]=0;



  return 0;
}

double func1(double x,double* y,int i ){
  double res;
  double valory;
  valory=sqrt(pow(y[0],2)+pow(y[1],2));
  res=-g[i]-c*valory*y[i]/m;

  return res;
}
double func2(double x,double* y,int i){

  return y[i];

}
