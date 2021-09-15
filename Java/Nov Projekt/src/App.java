import java.util.Scanner;

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

        nal4();

    }
}
