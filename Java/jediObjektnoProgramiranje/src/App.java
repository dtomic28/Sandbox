//Importamo scanner za vhod
import java.util.Scanner;

public class App {

    //Ustvarimo metodo za vnos jedijev
    public static jedi[] vnosJedi(){
        //Ustvarimo dva scannerja, kjer bo eden za ukaz .nextLine drugi pa za vse ostale. To naredimo, saj imamo problem z ne-shranjevanjem vrednosti/crash programa
        Scanner vnos = new Scanner(System.in);
        Scanner vnos2 = new Scanner(System.in);
        //Vprašamo koliko jedijov želimo ustvariti nato ustvarimo seznam jedijov ter ustvarimo vse spremenljivke, da jih ne dupliciramo v zanki
        System.out.println("Napisite koliko jedijov želite ustvariti: ");
        int kolikokrat = vnos.nextInt(), hp=0, mocMeca = 0, c=0;
        String ime = "", barvaMeca = "";
        boolean sila = false;
        jedi[] jediji = new jedi[kolikokrat];
        jedi novJedi;
        //Ustvarimo while zanko, ki bo delovala dokler se ne ustvari vneseno n število jedijov
        while(c!=kolikokrat){
            //Vprašamo in shranimo vse podatke
            System.out.println("Vpisite ime");
            ime = vnos2.nextLine();
            System.out.println("Vpisite Stran silo");
            sila = vnos.nextBoolean();
            System.out.println("Vpisite hp");
            hp = vnos.nextInt();
            System.out.println("Vpisite barvo meca");
            barvaMeca = vnos.next();
            System.out.println("Vpisite moc meca");
            mocMeca = vnos.nextInt(); 
            //Ustvarimo novega jedija in prevermo če je barva meča veljavna
            novJedi = new jedi(ime, sila, hp, barvaMeca, mocMeca);
            if(novJedi.preveriVeljavnostBarve() == true){
                //Če je veljavna program gre naprej 
                jediji[c] = novJedi;
                novJedi.izpisJedija();
                c++;
            }else{
                //Drugače poskupsimo ponovno
                System.out.println("Jedi ni bil pravilno vnešen poskusite znova");
            }
        }
        //Zapremo scannerje ter vrnemo seznam
        vnos2.close();
        vnos.close();
        return(jediji);
    }

    //Metoda, kjer sortiramo izpis po barvi meča
    public static void izpisJediGledeMec(jedi[] jediji){
        //Ustvarimo seznam z barvami
        String[] barve = {"moder", "zelen", "rdeč", "rumen", "vijoličen"};
        //Gremo skozi vse barve z eno zanko
        for(int i = 0; i<barve.length; i++){
            //Ter vse jedije z drugo zanko
            for(int j = 0; i<jediji.length; j++){
                //Pogledamo če jedi ustreza trenutno izbrani zanki, ter izpišemo.
                if(jediji[j].barva.equals(barve[i])==true){
                    jediji[j].izpisJedija();
                }
            }
        }
    }

    public static void najboljsiSvetlobniMeci(jedi[] jediji){
        int najvecji;
        String[] barve = {"moder", "zelen", "rdeč", "rumen", "vijoličen"};
        for(int i = 0; i<barve.length; i++){
            najvecji=0;
            for(int j = 0; i<jediji.length; j++){
                if(jediji[j].barva.equals(barve[i])==true && jediji[j].moc > jediji[najvecji].moc){
                    najvecji = j;
                }
            }
            jediji[najvecji].izpisJedija();
        }
    }

    public static void tehnicaJedijev(jedi[] jediji){
        int j=0,s=0;
        for(int i = 0; i<jediji.length; i++){
            if(jediji[i].stranSile==true){
                j += jediji[i].moc;
            }else{
                s += jediji[i].moc;
            }
        }
        if(j>s){
            System.out.println("Svetla stran sile je mocnejsa.");
        }else{
            System.out.println("Temna stran sile je mocnejsa");
        }
    }



    public static void main(String[] args){
        jedi[] jediji = vnosJedi();
        izpisJediGledeMec(jediji);
    }   
}
