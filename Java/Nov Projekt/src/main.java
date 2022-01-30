import java.util.Scanner;

public class main {

    //Vnos avta
    public static avto[] vnosAvtov(){
        //Ustvarimo dva scannerja, zaradi tega, ker če po nextLine izberemo nextInt program crashne ali se pa ne shrani vrednost
        Scanner vnos = new Scanner(System.in);
        Scanner vnosLine = new Scanner(System.in);
        //Vnesemo koliko avtov želimo ustvariti
        System.out.println("Vnesite kolikov avtov želite kreirati: ");
        //Ustvarimo vse spremenljivke za vse vrednosti avta
        int k = vnos.nextInt(), c = 0, let, km, cn;
        String zn,md,barva;
        //Ustvarimo seznam, ki ga bomo vrnili z avti
        avto[] avti = new avto[k];
        //Usvtarimo avte dokler ni toliko, kolikor jih želimo
        while(c!=k){
            System.out.println("Vnesite znamko: ");
            zn = vnosLine.nextLine();
            System.out.println("Vnesite model: ");
            md = vnosLine.nextLine();
            System.out.println("Vnesite letnik: ");
            let = vnos.nextInt();
            System.out.println("Vnesite barvo: ");
            barva = vnosLine.nextLine();
            System.out.println("Vnesite kilometre: ");
            km = vnos.nextInt();
            System.out.println("Vnesite ceno: ");
            cn = vnos.nextInt();
            //Vse podatke vnesemo ter ustvarimo nov avto, ki ga damo na seznam
            avti[c] = new avto(zn,md,let,barva,km,cn);
            c++;
        }
        //Zapremo scannerje ter returnamo seznam
        vnos.close();
        vnosLine.close();
        return(avti);
    }

    //Izpis avtov z forzanko, ki gre po vnesenem seznamu
    public static void izpisAvtov(avto[] avti){
        for(int i = 0; i<avti.length; i++){
            avti[i].izpisAvta();
        }
    }

    public static void Naloga1(avto[] avti){
        int n = 0;
        for(int i = 0; i<avti.length; i++){
            if(avti[i].kilometri > avti[n].kilometri){
                n = i;
            }
        }
        avti[n].izpisAvta();

    }

    public static void naloga2(avto[] avti){
        for(int i = 0; i<avti.length; i++){
            if(avti[i].znamka.equals("Renault")){
                avti[i].izpisAvta();
            }
        }
    }

    public static void naloga3(avto[] avti){
        int n = 0;
        for(int i = 0; i<avti.length; i++){
            if(avti[i].cena > avti[n].cena){
                n = i;
            }
        }
        avti[n].izpisAvta();
    }

    public static void naloga4(avto[] avti){
        int n = 0;
        for(int i = 0; i<avti.length; i++){
            if(avti[i].cena<avti[i].cena){
                n = i;
            }
        }
        avti[n].izpisAvta();
    }

    public static void naloga5(avto[] avti){
        int c = 0;
        for(int i = 0; i<avti.length; i++){
            if(avti[i].kilometri==0 || avti[i].letnik==2022){
                c++;
            }
        }
        System.out.println(c);
    }

    

    public static void main(String[] args){
        avto[] avti = new avto[5];
        avti[0] = new avto("Clio", 2002, "rumen", 1000000, 10);
        avti[1] = new avto("Volkswagen","Passat", 2022, "Sivi", 100, 45000);
        avti[2] = new avto("Lamborghini","Aventador", 2012, "Verede mantis", 50000, 250000);
        avti[3] = new avto("Megane RS", 2019, "črn", 90000, 20000);
        avti[4] = new avto("Clio", 2022, "rumen", 1000, 10000);
        
        //Naloga1(avti);
        
        //naloga2(avti);
        
        //naloga3(avti);
        
        izpisAvtov(avti);
        //naloga5(avti);
        
    } 
}
