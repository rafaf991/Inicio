#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
using namespace std;

#define PI 3.14159265

double g[2]={10,0};
double c=0.2;
double m=0.2;
//Condiciones iniciales:

double v0=300;

double tmax=10;
double h=0.00001;
int n=tmax/h;


double func1(double x,double y1,double y2,int i);

double func2(double x,double y1,double y2,int i);

void resolv(double **v,double ** x,double angulo,double* t,int n);

int main(){
//Vamos a resolver la ecuacion ddx/ddt = -g -c|v|v/m
  
  double** x=new double* [n];
  for (int i = 0; i < n; i++) x[i]=new double[2];

  double** v=new double *[n];
  for (int i = 0; i < n; i++) v[i]=new double[2];

  double* t=new double [n] ;
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
  ofstream file3;
  file3.open("graf3.txt");
	file3.close();
  for (int p =0; p<8;p++) resolv(v,x,angulos[p],t, n);


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


void resolv(double **v,double ** x,double angulo,double* t,int n){

	v[0][0]=v0*cos(angulo*PI/180);
  v[0][1]=v0*sin(angulo*PI/180);
	
  x[0][0]=0;
  x[0][1]=0;
  ofstream file3;
  int name=angulo;
  std::string s = std::to_string(name);
  file3.open(s);
  double k1,k2,k3,k4,l1,l2,l3,l4,k11,k22,k33,k44,l11,l22,l33,l44;
 //runge-kutta 4
  for (int i = 0; i < n-1 &&x[i][0]>=0 &&x[i][1]>=0 ; i++) {
    //Velocidad coordenada x e y.
		
//Posicion coordenada x e y.
   k1=func1(t[i],v[i][0],v[i][1],0);
   l1=func1(t[i],v[i][0],v[i][1],1);

	 k11=func2(t[i],v[i][0],v[i][1],0);
   l11=func2(t[i],v[i][0],v[i][1],1);

   k2=func1(t[i]+h/2,v[i][0]+k1*h/2,v[i][1]+l1*h/2,0);
   l2=func1(t[i]+h/2,v[i][0]+k1*h/2,v[i][1]+l1*h/2,1);
	
		k22=func2(t[i]+h/2,v[i][0]+k1*h/2,v[i][1]+l1*h/2,0);
   l22=func2(t[i]+h/2,v[i][0]+k1*h/2,v[i][1]+l1*h/2,1);

   k3=func1(t[i]+h/2,v[i][0]+k2*h/2,v[i][1]+l2*h/2,0);
   l3=func1(t[i]+h/2,v[i][0]+k2*h/2,v[i][1]+l2*h/2,1);

	 k33=func2(t[i]+h/2,v[i][0]+k2*h/2,v[i][1]+l2*h/2,0);
   l33=func2(t[i]+h/2,v[i][0]+k2*h/2,v[i][1]+l2*h/2,1);

   k4=func1(t[i]+h,v[i][0]+k3*h,v[i][1]+l3*h,0);
   l4=func1(t[i]+h,v[i][0]+k3*h,v[i][1]+l3*h,1);

	 k44=func2(t[i]+h,v[i][0]+k3*h,v[i][1]+l3*h,0);
   l44=func2(t[i]+h,v[i][0]+k3*h,v[i][1]+l3*h,1);
  

   x[i+1][0]=x[i][0]+(k44+2*(k22+k33)+k11)*h/6;
   x[i+1][1]=x[i][1]+(l44+2*(l22+l33)+l11)*h/6;

   v[i+1][0]=v[i][0]+(k4+2*(k2+k3)+k1)*h/6;
   v[i+1][1]=v[i][1]+(l4+2*(l2+l3)+l1)*h/6;



   file3<<x[i][0]<<"  "<<x[i][1]<<v[i][0]<<" "<<v[i][1]<<endl;

	

  }
	
  

file3.close();

}



