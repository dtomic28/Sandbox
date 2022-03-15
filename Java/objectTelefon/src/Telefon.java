import java.util.Random;

public class Telefon {
    String znamka;
    String model;
    String imei;
    int letoIzdaje;
    String barva;
    int kapaciteta;
    boolean PetG;
    int cena;
    
    public Telefon(String znamka, String model, String imei, int letoIzdaje, String barva, int kapaciteta, boolean PetG){
        this.znamka = znamka;
        this.model = model;
        this.imei = imei;
        this.letoIzdaje = letoIzdaje;
        this.barva = barva;
        this.kapaciteta = kapaciteta;
        this.PetG = PetG;
    }

}
