public class CalculatriceSimple{

  public static void main(String[] args){
    Nombre six = new Nombre(6) ;
    Nombre dix = new Nombre(10) ;
    Operation s = new Soustraction(dix,six) ;
    System.out.println(s + " = " + s.valeur()) ;// doit afficher : (10 – 6) = 4

    Nombre zero = new Nombre(0);
    Operation div0 = new Division(dix,zero);
    try {
    	System.out.println(div0 + " = " + div0.valeur()) ; // Affiche une erreur
    }catch(ArithmeticException e) {
    	System.out.println(e.getMessage() + " Impossible!!!");
    }

    Nombre deux = new Nombre(2);
    Operation div2 = new Division(dix,deux);
    try {
    	System.out.println(div2 + " = " + div2.valeur()) ; // Affiche une erreur
    }catch(ArithmeticException e) {
    	System.out.println(e.getMessage() + " Impossible!!!");
    }

    Nombre huit = new Nombre(8) ;
    Operation a = new Addition(huit,six) ;
    System.out.println(a + " = " + a.valeur()) ;// doit afficher : (8 + 6) = 14

    Nombre cinq = new Nombre(5);
    Operation m = new Multiplication(huit,cinq);
    System.out.println(m + " = " + m.valeur()) ;// doit afficher : (8 * 5 ) = 40
    Nombre sept = new Nombre(7);
    System.out.println("La valeur de la variable sept est initialisee a : "+sept.getValeurNombre()); //affiche 7;
    sept.setValeurNombre(34);
    System.out.println("La valeur de la variable sept a ete modifiee en : "+sept.getValeurNombre()); //affiche 34;
    
    Nombre dixHuit = new Nombre(18);
    Nombre quatre = new Nombre(4);
    
    Multiplication m2 = new Multiplication(3,12);
    Multiplication m3 = new Multiplication(m2);
    Multiplication m4 = new Multiplication(quatre,dixHuit);
    System.out.println(m2 + " = " + m2.valeur()); //affiche (3 * 12) = 36
    System.out.println(m3 + " = " + m3.valeur()); //affiche (3 * 12) = 36
    System.out.println(m4 + " = " + m4.valeur()); //affiche (4 * 18) = 72
    
    Division d3 = new Division(15,3);
    Division d4 = new Division(d3);
    Division d5 = new Division(dixHuit,six);
    System.out.println(d3 + " = " + d3.valeur()); //affiche (15 / 3) = 5
    System.out.println(d4 + " = " + d4.valeur()); //affiche (15 / 3) = 5
    System.out.println(d5 + " = " + d5.valeur()); //affiche (18 / 6) = 3
    
    Addition a2 = new Addition(45,5);
    Addition a3 = new Addition(a2);
    Addition a4 = new Addition(six,quatre);
    System.out.println(a2 + " = " + a2.valeur()); //affiche (45 + 5) = 50
    System.out.println(a3 + " = " + a3.valeur()); //affiche (45 + 5) = 50
    System.out.println(a4 + " = " + a4.valeur()); //affiche (6 + 4) = 10
    System.out.println("Inversement des Operandes :");
    a4.setOperande1(quatre);
    a4.setOperande2(six);
    System.out.println(a4 + " = " + a4.valeur()); //affiche (4 + 6) = 10

  }
}
