import java.util.Random;

public class App {
    public static void main(String[] args) throws Exception {
        Random randomGenerator = new Random();
        int randomInt = randomGenerator.nextInt(14);
        System.out.print(randomInt);
    }
}
