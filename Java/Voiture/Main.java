import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        System.out.println("Welcome to Tesla Motors");
        Voiture A = new Voiture("Tesla");
        boolean exit = false;
        do {
            System.out.println("What do you want to do ?\n 1-Drive \n 2-Turn to left \n 3-Turn to right \n 4-Stop");
            Scanner menu = new Scanner(System.in);
            int choice = menu.nextInt();
            if (choice == 1) {
                A.rouler(50);
            }
            if (choice == 2) {
                A.tournerl(true);
            }
            if (choice == 3) {
                A.tournerd(true);
            }
            if (choice == 4) {
                A.stop(0);
                exit = true;

            }
        } while (!exit);
    }
}

