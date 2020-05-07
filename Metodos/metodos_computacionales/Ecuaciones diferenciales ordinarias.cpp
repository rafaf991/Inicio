#include<iostream>
#include <fstream>
using namespace std;
float f(float x,float y);
int main(){
  float x0,y0,h,xmax;
  int n;
  x0=0;
  y0=1;
  h=0.1;
  xmax=5.1;
  n=(int)(xmax-x0)/h;
  float x[n],y[n];
  x[0]=x0;
  y[0]=y0;
  ofstream file;
  file.open("graf.txt");



  //euler
  for (int i = 0; i < n; i++) {
    float temp;
    temp=y[i];

    y[i+1]=temp+h*f(x[i],y[i]);
    x[i+1]=x0+h*i;
    file<<x[i]<<"  "<<y[i]<<endl;
}

file.close();
ofstream file2;
file2.open("graf2.txt");
float k1,k2;
  //ruge-kutta 2
  for (int i = 0; i < n; i++) {

    k1=h*f(x[i],y[i]);
    k2=h*f(x[i]+h/2,y[i]+k1/2);
    y[i+1]=y[i]+k2;
  file2<<x[i]<<"  "<<y[i]<<endl;
  }
file2.close();


ofstream file3;
file3.open("graf3.txt");
float k3,k4;
  //ruge-kutta 4
  for (int i = 0; i < n; i++) {

    k1=h*f(x[i],y[i]);
    k2=h*f(x[i]+h/2,y[i]+k1/2);
    k3=h*f(x[i]+h/2,y[i]+k2/2);
    k4=h*f(x[i]+h,y[i]+k3);
    y[i+1]=y[i]+(k4+2*(k2+k3)+k1)/6;
  file3<<x[i]<<"  "<<y[i]<<endl;
  }
file3.close();



return 0;




}

float f(float x,float y){
  return x*y;
}
