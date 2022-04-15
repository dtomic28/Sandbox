import java.util.Scanner;

public class App {
	/*
	public static Pocitnice[] tockaTri() {
		Scanner vhod = new Scanner(System.in);
		System.out.println("Vnesite stevilo pocitnic, ki želite: ");
		int stVnosov = vhod.nextInt();
		Pocitnice[] vnosi = new Pocitnice[stVnosov];
		String destinacija;
		String drzava;
		String paket;
		int mesec;
		int stProstih;
		double cena;
		for(int i = 0; i<vnosi.length; i++) {
			
			System.out.println("Vnesite destinacijo: ");
			destinacija = vhod.next();
			System.out.println("Vnesite drzavo");
			drzava = vhod.next();
			paket = "polpenzion";
			System.out.println("Vnesite mesec (ST): ");
			mesec = vhod.nextInt();
			System.out.println("Vnesite st prostih pojstl");
			stProstih = vhod.nextInt();
			System.out.println("Vnesite ceno");
			cena = vhod.nextDouble();
			
			vnosi[i] = new Pocitnice(destinacija, drzava, paket,mesec, stProstih, cena); 
		}
		vhod.close();
		return vnosi;
	}
	
	public static String tockaStiri() {
		String[] paketi = {"penzion", "polpenzion", "polni penzion", "Ostalo"};
		int rand = (int) (Math.random()*4);
		return paketi[rand];
	}
	
	public static void tockaSest(Pocitnice[] vnosi) {
		for(int i = 0; i<vnosi.length; i++) {
			vnosi[i].izpis();
		}
	}
	
	public static double izracunPovprecja(Pocitnice[] vnosi) {
		double c = 0;
		for(int i = 0; i<vnosi.length; i++) {
			c += vnosi[i].cena;
		}
		return(c/vnosi.length);
		
	}
	
	public static void tockaSedem(Pocitnice[] vnosi) {
		double povprecje = izracunPovprecja(vnosi);
		for(int i = 0; i<vnosi.length; i++) {
			if(vnosi[i].cena>povprecje) {
				vnosi[i].izpis();
			}
		}
	}
	
	public static void tockaOsem(Pocitnice[] vnosi) {
		for(int i = 0; i<vnosi.length; i++) {
			if(vnosi[i].paket.equals("polpenzion") && (vnosi[i].drzava.charAt(0)+"").equals("g")){
				vnosi[i].izpis();
			}
		}
	}
	
	*/
	/*
	public static void naloga1(int p, String pon){
        if(p==0){
            return;
        }else{
            System.out.println(pon);
            naloga1(p-1, pon);
        }
    }

    public static int naloga2(int x, int y){        
        if(x==0){
            return(1);
        }else{
            return(naloga2(x-1, y) * y);
        }
    }

    public static void naloga3(String niz, int c, int x){
        if(x-(c*2)==1 || x-(c*2)==2){
            System.out.println(niz);
            return;
        }else{
            System.out.println(niz);
            try{
                naloga3(" " + niz.substring(0, niz.length()-2), c++, x);
            } catch (Exception e){
                ;
            }
        }
    }
    
    public static String naloga3Fill(int x) {
    	if(x == 0) {
    		return("");
    	}else {
    		return(naloga3Fill(x-1) + "*");
    	}
    }

    public static void naloga3input(){
        Scanner vhod = new Scanner(System.in);
        System.out.println("Vnesite sirino: ");
        int sirina = vhod.nextInt();
        naloga3(naloga3Fill(sirina), 0, sirina);
    }
	
	*/

	public static String naloga1(String str, int c){
		if(c==str.length()){
			return("");
		}else{
			//System.out.println(str.charAt(c));
			return(naloga1(str,c+=1) + str.charAt(c-1));
		}
	}

	public static int naloga2(int[] stevila, int c){
		if(c==stevila.length){
			return(0);
		}else{
			return(stevila[c] + naloga2(stevila, c+=1));
		}
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] stevila = {3,5,7,3}; 	
		System.out.println(naloga2(stevila, 0));
		
	}
}
