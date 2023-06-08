import java.util.Scanner;

public class MetricConverter {
    public static void main(String[] args) {

        // a. The unit you want to convert from

        // b. The unit you want to convert to

        // c. Quantity to be convert

        Scanner input = new Scanner(System.in);

        System.out.println("enter unit you wanna convert from");
        String ConvertUnitFrom = input.nextLine();

        // System.out.println("enter unit you wanna convert to");
        // String ConvertUnitTo = input.nextLine();

        System.out.println("enter quantity");
        double Quantity = input.nextDouble();

        // a. From Feet to Meters

        // b. From Pounds to Kgs

        // c. From Fahrenheit to Celsius (32°F − 32) × 5/9 = 0°C

        double total = 0;
        final double METERS = 3.281;
        // final double KGS = 2.205;

        if (ConvertUnitFrom.equals("feet")) {
            total = Quantity / METERS;
            System.out.println(total);

        } else {
            System.out.println("FAILURE");
        }

    }

}
