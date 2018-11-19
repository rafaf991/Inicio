#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

#define PI 3.14159265

double g[2];

double c=0.2;
double m=20;


double func1(double x,double y1,double y2,int i);

double func2(double x,double y1,double y2,int i);

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
  for (int i = 0; i < n; i++) x[i]=new double[2];

  double** v=new double *[n];
  for (int i = 0; i < n; i++) v[i]=new double[2];

  double t[n];
  for (int i = 0; i < n; i++) t[i]=h*i;

  double angulos[8];
  angulos[0]=45;
  angulos[1]=10;
  angulos[2]=20;
  angulos[3]=30;
  angulos[4]=40;
  angulos[5]=50;
  angulos[6]=60;
  angulos[7]=70;
  for (int l = 0; l < 8; l++) {
  double angulo=angulos[l];
  v[0][0]=v0*cos(angulo*PI/180);
  v[0][1]=v0*sin(angulo*PI/180);
  x[0][0]=0;
  x[0][1]=0;
  ofstream file3;
  file3.open("graf3.txt",std::fstream::app);
  double k1,k2,k3,k4,l1,l2,l3,l4;
 //runge-kutta 4
  for (int i = 0; i < n-1; i++) {
    //Velocidad coordenada x e y.

   k1=h*func1(t[i],v[i][0],v[i][1],0);
   l1=h*func1(t[i],v[i][0],v[i][1],1);

   k2=h*func1(t[i]+h/2,v[i][0]+k1/2,v[i][1]+l1/2,0);
   l2=h*func1(t[i]+h/2,v[i][0]+k1/2,v[i][1]+l1/2,1);

   k3=h*func1(t[i]+h/2,v[i][0]+k2/2,v[i][1]+l2/2,0);
   l3=h*func1(t[i]+h/2,v[i][0]+k2/2,v[i][1]+l2/2,1);

   k4=h*func1(t[i]+h,v[i][0]+l3,v[i][1]+k3,0);
   l4=h*func1(t[i]+h,v[i][0]+l3,v[i][1]+k3,1);

   v[i+1][0]=v[i][0]+(k4+2*(k2+k3)+k1)/6;
   v[i+1][1]=v[i][1]+(l4+2*(l2+l3)+l1)/6;




  }
  for (int i = 0; i < n-1; i++) {
    //Posicion coordenada x e y.

   k1=h*func2(t[i],x[i][0],x[i][1],0);
   l1=h*func2(t[i],x[i][0],x[i][1],1);

   k2=h*func2(t[i]+h/2,x[i][0]+k1/2,x[i][1]+l1/2,0);
   l2=h*func2(t[i]+h/2,v[i][0]+k1/2,v[i][1]+l1/2,1);

   k3=h*func2(t[i]+h/2,x[i][0]+k2/2,x[i][1]+l2/2,0);
   l3=h*func2(t[i]+h/2,x[i][0]+k2/2,x[i][1]+l2/2,1);

   k4=h*func2(t[i]+h,x[i][0]+l3,x[i][1]+k3,0);
   l4=h*func2(t[i]+h,x[i][0]+l3,x[i][1]+k3,1);

   x[i+1][0]=x[i][0]+(k4+2*(k2+k3)+k1)/6;
   x[i+1][1]=x[i][1]+(l4+2*(l2+l3)+l1)/6;



   file3<<t[i]<<"  "<<x[i][0]<<"  "<<x[i][1]<<"  "<<v[i][0]<<"  "<<v[i][1]<<endl;
  }
  file3.close();
}



  return 0;
}

double func1(double x,double y1,double y2,int i ){
  double res;
  double valory;
  valory=sqrt(pow(y1,2)+pow(y2,2));
  if (i==0){
    res=-g[i]-c*valory*y1/m;
  }
  else res=-g[i]-c*valory*y2/m;

  return res;
}
double func2(double x,double y1,double y2,int i){
  if (i==0){
    return y1;
  }
  else return y2;

}
