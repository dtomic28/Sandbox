public class Pokemon{
    //Nastavimo atribute za pokemona
    int id, zivljenje,napad; 
    String ime;

    //Ustvairmo konstruktor, kjer z vhodno spremenljivko nastavimo vrednosti na atribute objekta
    public Pokemon(int id, int zivljenje, int napad, String ime){
        this.id = id;
        this.zivljenje = zivljenje;
        this.napad = napad;
        this.ime = ime;
    }

    //Okrajšamo oz. formatiramo obliko prikaza pokemona, tako da vzamemo prve 3 črke iz niza this.ime ter dodamo še id v []
    public String okrajsaj(){
        return("" + this.ime.charAt(0) + this.ime.charAt(1) + this.ime.charAt(2) + "[" + this.id + "]");
    }

    //Izpišemo vse skupaj 
    public void izpis(){
        System.out.printf("%s - HP:%d PW:%d\n", this.okrajsaj(), this.zivljenje, this.napad);
    }

    //Metoda bitka, ki preprosto odšteje moč udarca
    public void bitka(int Mocnapada){
        this.zivljenje -= Mocnapada;
    }

}