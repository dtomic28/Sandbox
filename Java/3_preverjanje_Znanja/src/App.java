public class App {

    public static void bitkaDvehPokemonov(Pokemon p, Pokemon d){
        //Izpis prvih dveh
        p.izpis();
        d.izpis();
        //Izpis napada
        System.out.println("--------NAPAD--------");
        //Napad p
        p.bitka(d.napad);
        p.izpis();
        d.izpis();
    }

    public static void main(String[] args) throws Exception {
        //Definiramo dva nova pokemona
        Pokemon pika = new Pokemon(25, 95, 30, "Pikachu");
        Pokemon charmander = new Pokemon(4, 75, 40, "Charmander");
        //Ter prikličemo bitko
        bitkaDvehPokemonov(pika, charmander);
    }
}
