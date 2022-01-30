public class jedi{

    //Definiramo atribute razreda jedi. Nastavimo ime, stran sile, zivljenske točke, barvo meča ter moč meča
    String ime = "";
    boolean stranSile;
    int zivljenskeTocke = 0;
    String barva = "";
    int moc = 0;

    //Ustvarimo konstruktor, da lahko ob ustvarjanju razreda lahko nastavimo vrednosti
    public jedi(String ime, boolean stranSile, int HP, String barvaMeca, int mocMeca){
        this.ime = ime;
        this.stranSile = stranSile;
        this.zivljenskeTocke = HP;
        this.barva = barvaMeca;
        this.moc = mocMeca;
    }

    //Metoda za ispis jedija
    public void izpisJedija(){
        //Ustvarimo spremenljivko niza
        String stran = "";
        //Pogledamo na kateri strani sile je ter dodamo na spremenljivko
        if(this.stranSile == true){
            stran = "Jedi";
        }else{
            stran = "Sith";
        }
        //Z pomočjo formatiranja stringov izpišemo
        System.out.printf("%s (%s) %s-%d \n", this.ime, stran, this.barva, this.moc);
    }

    //Metoda, kjer preverimo veljavnost barve meča ter vrnemo true ali false
    public boolean preveriVeljavnostBarve(){
        if(this.barva.equals("moder")==true || this.barva.equals("zelen")==true || this.barva.equals("rdec")==true || this.barva.equals("rumen")==true || this.barva.equals("vijolicen")==true){
            return(true);
        }else{
            return(false);
        }
    }

    public static void main(String[] args){
        jedi nov = new jedi("Darth Vader", false, 100, "zelena", 40);
    }
    
}
