import java.util.Random;
import java.util.Scanner;

public class test {
    public static void main(String[] args) {

        Random random = new Random();

        Scanner scanner = new Scanner(System.in);

        System.out.println("what is the heightest range: ");
        int num = scanner.nextInt();

        int rannum = random.nextInt(num) + 1;
        System.out.println(num);
        System.out.println(rannum);
        String name = "";

        while (name.isBlank()) {
            System.out.print("enter your name: ");
            name = scanner.nextLine();

        }
        System.out.println("hello: " + name);

    }
}
