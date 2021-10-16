import java.util.Scanner;
import java.lang.Math;

public class App {

    static void vrniPetkratnik(int a) {
        System.out.print(a*5);
    }

    static void nal4() {
        Scanner vhod = new Scanner(System.in);
        System.out.println("Vnesite stavek a: ");
        String a = vhod.nextLine().toUpperCase();
        System.out.println("Vnesite st b: ");
        int b = vhod.nextInt();
        System.out.println("Vnesite st c: ");
        int c = vhod.nextInt();
        a = a.replaceAll(" ", "");
        
        vhod.close();

        if(b>c || c>a.length()){
            System.out.println("Naredili ste napako pri vnosu.");
            return;
        }
        
        //ye

        for(int i = b-1; i<c; i++){
            if(a.charAt(i) != ' '){
                System.out.print(a.charAt(i));
            }
        }

    }

    public static String nal5(String s, char a, char b, char c, char d, char e) { // ustvarimo metodo 
		int ca = 0, cb = 0, cc = 0, cd = 0, ce = 0;
        String n = ""; // ustvarimo spremenljivko za nov niz 
		for(int i = 0; i<s.length(); i++) { // gremo skozi orginalen niz
			if(n.contains(s.charAt(i) + "") == false) { // pogledamo, da se ni ponovila črka
				n += s.charAt(i); // če se ni dodamo na niz
			}
            if(s.charAt(i) == a){
                ca += 1;
            }else if(s.charAt(i) == b){
                cb += 1;
            }else if(s.charAt(i) == c){
                cc += 1;
            }else if(s.charAt(i) == d){
                cd += 1;
            }else if(s.charAt(i) == e){
                ce += 1;
            }
		}
        System.out.printf("%s: %o, %s: %o, %s: %o, %s: %o, %s: %o", a,ca,b,cb,c,cc,d,cd,e,ce);
		return(n); // ter ga vrnemo
	}

    public static double nalogaUstno(){
        Scanner vhod = new Scanner(System.in);
        int c = 0, y = 0;
        int stevila = 0;
        for(int i = 0; i<1000;i++){
            y = vhod.nextInt();
            if(y>9999&&y<100000){
                stevila += y;
                c++;
            }
        }
        vhod.close();
        return((stevila*1.00)/c);
    }

    public static void drugaNaloga(){
            int l = 0;
            int d = 1;
            int n = (int) (Math.random()*10000);
            while(l<d){
                n =(int) (Math.random()*10000);
                if (n<1000){
                    n+=1000;
                }
                d=n%100;
                l=n/100;
                System.out.println(n);
            }
            System.out.println("--------------");
            System.out.println(n);
    }
    
    public static void palindrom(int st){
        String n = "", r = "";
        n = st + "";
        for(int i = n.length()-1; i > -1; i--){
            r += n.charAt(i);
        }
        if(n.equals(r)==true){
            System.out.print("Da");
        }else{
            System.out.print("Ne");
        }

    }

    public static void izSedemVDeset(int st){
        String s = st + "";
        int c = 0;
        int ss = 0;
        for(int i = s.length()-1; i>-1; i--){
            ss += Integer.parseInt(s.charAt(i)+"") * Math.pow(7, c);
            c++;
        }
        System.out.print(ss);
    }

    public static void kvadrat(int st){
        String vrstica = "";
        for(int i=0;i<st;i++){
           vrstica = "";
            for(int j = 0; j<st;j++){
                if(i>=j){
                    if((i+j)%2==0){
                        vrstica += "- ";
                    }else{
                        vrstica += "+ ";
                    }
                }
            }
            System.out.println(vrstica);
       } 
    }

    public static int count(String s){
        int c = 0;
        for(int i = 0; i<s.length(); i++){
            if(s.charAt(i) == '0'){
                c++;
            }
        }
        return(c);
    }

    public static void kvadrat2(int st){
        String vrstica = "";
        int c = 0;
        for(int i=0;i<st;i++){
            vrstica = "";
            for(int j = 0; j<st;j++){
                if(i+j>=st-1 && i<=j || i+j<=st-1 && i>=j ){
                    vrstica += "0 ";
                    c++;
                    System.out.print(c);
                }else{
                    vrstica += "  ";
                    c++;
                    System.out.print(c);
                }
            }
            System.out.println(vrstica);
        }
        System.out.printf("What the %d", c);
    }

    public static void kvadrat3(int st){
        String vrstica = "";
        int c = 0;
        for(int i=0;i<st;i++){
            vrstica = "";
            for(int j = 0; j<st;j++){
                if(i==j){
                    vrstica += "0 ";
                    System.out.println();
                }else{
                    vrstica += "  ";
                }
            }
            System.out.println(vrstica);
        }
        System.out.printf("Ploscina je %o \n", c); 
    }

    public static void izDesetVSedem(int stevilo){
        int st = 0;
        int c = 1;    
        while(stevilo>0){
            st += stevilo%7 * c;
            c = c*10;
            stevilo = stevilo / 7;
        }
        System.out.print(st);
    } 

    public static char vrniCrko(String beseda, int črka){
        return(beseda.charAt(črka));
    }

    public static void izDesetVosem(int st){
        System.out.printf("Stevilo je: %x", st);
    }

    public static void main(String[] args) throws Exception {
        /*
        Scanner vhod = new Scanner(System.in);
        System.out.print("Vnesite število: ");
        int pra = vhod.nextInt();
        vhod.close();
        boolean prastevilo = true;
        for(int i = 2; i<=pra; i++) {
            if(pra%i==0 && i!=pra) {
                prastevilo = false;
            }
        }
        if(prastevilo == true){
            System.out.println("Je praštevilo!!!");
        }else{
            System.out.println("Ni praštevilo");
        }
        */
        
        // System.out.print(vrniCrko("Yes",2));

        izDesetVosem(255);
    }
}
