  #include <iostream>
  #include <fstream>
  #include <cmath>


  using namespace std;

  int main(){
    //Ecuacion de calor
    double C,p,k,nu;
    C=820;
    p=2.71;
    k=1.62*10000//cm2  s-1;
    nu=k/(C*p);

    double xmax,ymax,tmax,dx,dt,temperatura_inicial;
    int maxt,maxx,maxy;
    xmax=50;//cm
    ymax=50;//cm
    tmax=10;
    //Asumiendo dx=dy;
    dx=1;
    dt=1;
    maxx=ceil(xmax/dx);
    maxy=ceil(ymax/dx);
    maxt=ceil(tmax/dt);
    temperatura_inicial=10;

    cout<<maxx<<" "<<maxy<<maxt<<endl;

    //T es oara caso 1 fronteras fijas 10 grados
    //TT es para caso 2 condiciones abiertas
    //TTT es para caso 3 periodicas.

    double*** T=new double** [maxx];
    for (int i = 0; i < maxx; i++) {
      T[i]=new double* [maxy];
      for (int j = 0; j < maxy; j++) {
        T[i][j]=new double [maxt];
      }
    }
    double*** TT=new double** [maxx];
    for (int i = 0; i < maxx; i++) {
      TT[i]=new double* [maxy];
      for (int j = 0; j < maxy; j++) {
        TT[i][j]=new double [maxt];
      }
    }
    double*** TTT=new double** [maxx];
    for (int i = 0; i < maxx; i++) {
      TTT[i]=new double* [maxy];
      for (int j = 0; j < maxy; j++) {
        TTT[i][j]=new double [maxt];
      }
    }




    
    int centrox=ceil(maxx/2); 
    int centroy=ceil(maxy/2);
    double radio=10/2;
    int radioi=ceil(radio/dx);
    //Inicializando T;

    for (int i = 0; i <maxx; i++) {
      for (int j = 0; j < maxy; j++) {


	
        if(pow((j-centroy),2)+pow((i-centrox),2)<=pow(radioi,2)){
	    T[i][j][0]=100;
            TT[i][j][0]=100;
            TTT[i][j][0]=100;
	}
        else {
          if (i==0||j==0){
            TT[i][j][0]=temperatura_inicial;
            TTT[i][j][0]=temperatura_inicial;
          }
          else{
          T[i][j][0]=temperatura_inicial;
          TT[i][j][0]=temperatura_inicial;
          TTT[i][j][0]=temperatura_inicial;}
        }
        if(i==0 ||i==maxx-1 ||j==0||j==maxx-1){
          T[i][j][0]=10;
        }





      }
    }

    ofstream file;
    file.open("Eccalor.txt");
    for (int j = 0; j < maxt-1; j++) {


      for (int m = 0; m < maxx; m++) {
        for (int n = 0; n < maxy; n++) {

        //Condicion metal:
        if(pow((m-centroy),2)+pow((n-centrox),2)>pow(radioi,2)){
	//Condicion 1
	if(m==0||n==0||m==maxx-1||n==maxy-1){
	T[m][n][j+1]=10;
	}
	else{
	T[m][n][j+1]=T[m][n][j]+nu*(dt/pow(dx,2))*(T[m+1][n][j]-T[m-1][n][j]+T[m][n+1][j]-T[m][n-1][j]-4*T[m][n][j]);
	}
	//Condicion 2
	if(m==0||n==0||m==maxx-1||n==maxy-1){
	if(n==0||m==maxx-1||n==maxy-1){
	if(m==maxx-1||n==maxy-1){
	if(n==maxy-1){
	TT[m][n][j+1]=TT[m][n][j]+nu*(dt/pow(dx,2))*(TT[m+1][n][j]-TT[m][n][j]+TT[m][n][j]-TT[m][n-1][j]-4*TT[m][n][j]);
	}
	else{TT[m][n][j+1]=TT[m][n][j]+nu*(dt/pow(dx,2))*(TT[m][n][j]-TT[m-1][n][j]+TT[m][n+1][j]-TT[m][n-1][j]-4*TT[m][n][j])}
	}
	else{TT[m][n][j+1]=TT[m][n][j]+nu*(dt/pow(dx,2))*(TT[m+1][n][j]-TT[m][n][j]+TT[m][n+1][j]-TT[m][n][j]-4*TT[m][n][j])}
	}
	else{TT[m][n][j+1]=TT[m][n][j]+nu*(dt/pow(dx,2))*(TT[m+1][n][j]-TT[m][n][j]+TT[m][n+1][j]-TT[m][n-1][j]-4*TT[m][n][j]);}
	
	}
	else{
	TT[m][n][j+1]=TT[m][n][j]+nu*(dt/pow(dx,2))*(TT[m+1][n][j]-TT[m-1][n][j]+TT[m][n+1][j]-TT[m][n-1][j]-4*TT[m][n][j]);
	}
       
        file<<T[m][n][(j+1)]<<" "<<TT[m][n][(j+1)]<<" "<<TTT[m][n][(j+1)]<<" ";

        }
	//Condicion 3
	TTT[m][n][j+1]=TTT[m][n][j]+nu*(dt/pow(dx,2))*(TTT[m+1][n][j]-TTT[m-1][n][j]+TTT[m][n+1][j]-TTT[m][n-1][j]-4*TTT[m][n][j])
	
        file<<endl;

      }



    }
    file.close();

    return 0;
  }
