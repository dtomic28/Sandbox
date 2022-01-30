class avto{
    //Definicija atributov avta
    String znamka, model, barva;
    int letnik, kilometri, cena;

    //Prvi konstruktor, kjer nima default znamke
    public avto(String znamka, String model, int letnik, String barva, int kilometri, int cena){
        this.znamka = znamka;
        this.model = model;
        this.letnik = letnik;
        this.barva = barva;
        this.kilometri = kilometri;
        this.cena = cena;
    }
    //Drugi konstrukor, kjer ima default znamko
    public avto(String model, int letnik, String barva, int kilometri, int cena){
        this.znamka = "Renault";
        this.model = model;
        this.letnik = letnik;
        this.barva = barva;
        this.kilometri = kilometri;
        this.cena = cena;
    }
    
    //Izpis avta
    public void izpisAvta(){
        System.out.printf("%s %s (%d) %s km: %d cena: %d \n", this.znamka, this.model, this.letnik, this.barva, this.kilometri, this.cena);
    }
}