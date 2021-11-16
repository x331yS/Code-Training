public class Main {
    public static void main(String[] args) {
        System.out.println("Want to turn Celsius in Fahrenheit?\n Yes - 1\n No - 2");
        Scanner menu = new Scanner(System.in);
        int choice = menu.nextInt();
        if (choice == 1) {
            System.out.println("Converting Celsius to Fahrenheit ! ");
            System.out.println("Please enter temperature in Celsius : ");
            Scanner scan = new Scanner(System.in);
            float celsius = scan.nextFloat();
            double fahrenheit = 9.0 / 5.0 * celsius + 32;
            System.out.println("Temperature in Fahrenheit is : " + fahrenheit);
        } else {
            System.out.println("Converting Fahrenheit to Celsius ! ");
            System.out.println("Please enter temperature in Fahrenheit : ");
            Scanner scan = new Scanner(System.in);
            float fahrenheit = scan.nextFloat();
            float celsius = (fahrenheit - 32) * 5 / 9;
            System.out.println("Temperature in Celsius is : " + celsius);
        }
    }
}
