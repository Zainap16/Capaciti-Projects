import java.util.Scanner;

public class MetricConverter {

    public static void main(String[] args) {

        // a. The unit you want to convert from

        // b. The unit you want to convert to

        // c. Quantity to be convert

        Scanner input = new Scanner(System.in);

        // a. From Feet to Meters

        // b. From Pounds to Kgs

        // c. From Fahrenheit to Celsius (32°F − 32) × 5/9 = 0°C

        double total = 0;
        final double METERS = 3.281;
        final double KGS = 2.205;

        System.out.println("enter unit you wanna convert from feet-f,pounds-p,F : ");
        String ConvertUnitFrom = input.nextLine();

        System.out.println("enter quantity");
        double Quantity = input.nextDouble();
        // input.nextLine();

        System.out.println("enter unit you wanna convert to inches-i,kilograms-kg,, C");
        String ConvertUnitTo = input.nextLine();

        if (ConvertUnitFrom.equals("f") && ConvertUnitTo.equals("i")) {
            total = Quantity / METERS;
            System.out.println(Math.ceil(total));

        } else if (ConvertUnitFrom.equals("p") && ConvertUnitTo.equals("kg")) {
            total = Quantity / KGS;
            System.out.println(Math.ceil(total));

        } else if (ConvertUnitFrom.equals("F") && ConvertUnitTo.equals("C")) {
            total = (Quantity - 32) * (5 / 9);
            System.out.println(Math.ceil(total));
        }

        else {
            System.out.println("FAILURE");
        }

    }

}
