#include <iostream>
#include <string>
#include<fstream>
using namespace std;
int main(){
  ofstream file;
  file.open("graf.txt");
  float tmax,t0,x0,y0,km,temp1,temp2;
  tmax=5;
  t0=0;
  x0=0;
  y0=1;
  km=3;
  float h=0.01;
  int N= (int) (tmax-t0)/h;
  float v[N],x[N],t[N];

  x[0]=x0;
  v[0]=y0;
  t[0]=t0;

  for(int i =0;i<N; i++){
    t[i]=t0+h*(i);
    float v_nn,x_nn,k2;

    k2=h*(v[i]+(-3)*x[i]*h/2);
    x_nn=x[i]+k2;

    k2=h*(-3)*(x[i]+v[i]*h/2);
    v_nn=v[i]+k2;

    temp1=x_nn;
    temp2=v_nn;

    x[i+1]=temp1;
    v[i+1]=temp2;

  file<<  t[i]<<"  "<<x[i]<<"  "<<v[i]<<endl;
  }
  file.close();



return 0;

}
