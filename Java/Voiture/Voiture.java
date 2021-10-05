public class Voiture {
    private String nom;

    Roue G = new Roue(50);
    Roue D = new Roue(50);
    public void rouler(int vitesse){
        System.out.println("La voiture avance à "+vitesse);
        G.tourner(vitesse, "gauche");
        D.tourner(vitesse, "droite");

    }
    public void stop(int vitesse){
        System.out.println("La voiture avance à "+vitesse);
        G.tourner(vitesse, "gauche");
        D.tourner(vitesse, "droite");

    }
    public void tournerl(boolean gauche){
        System.out.println("La voiture tourne");
        G.tourner(10, "gauche");
        D.tourner(50, "droite");

    }
    public void tournerd(boolean droite){
        System.out.println("La voiture tourne");
        G.tourner(50, "gauche");
        D.tourner(10, "droite");

    }
    public void getNom(){

    }
    public Voiture(String nom){
        System.out.println("La voiture est une "+nom);
    }
    public void setNom(String nom){

    }
}
