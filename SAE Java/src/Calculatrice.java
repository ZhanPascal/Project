public class Calculatrice{
	
	public static void main(String[] args) {
		
	    Expression two = new Nombre(2) ;
	    Expression trois = new Nombre(3) ;
	    Expression dixSept = new Nombre(17) ;
	    Expression s1 = new Soustraction(dixSept, two) ;
	    Expression a1 = new Addition(two, trois) ;
	    Expression d1 = new Division(s1, a1) ;
	    System.out.println(d1 + " = " + d1.valeur()) ; // affiche ((17 - 2) / (2 + 3)) = 3 
	    
	    Expression m1 = new Multiplication(two,dixSept);
	    Expression un = new Nombre(1);
	    Expression s2 = new Soustraction(m1,un);
	    Expression d2 = new Division(s2,trois);
	    System.out.println(d2 + " = " + d2.valeur()) ; // affiche (((2 * 17)-1)/3) = 11

	    Expression quatre = new Nombre(4);
	    Expression dixHuit = new Nombre(18);
	    Expression s3 = new Soustraction(12,6);
	    Expression s4 = new Soustraction(dixHuit,quatre);
	    Expression s5 = new Soustraction(56,43);
	    Expression s6 = new Soustraction(s4,s5);
	    Expression s7 = new Soustraction(s5,s4);
	    System.out.println(s3 + " = " + s3.valeur()); //affiche (12 - 6) = 6
	    System.out.println(s4 + " = " + s4.valeur()); //affiche (18 - 4) = 14
	    System.out.println(s5 + " = " + s5.valeur()); //affiche (56 - 43) = 13
	    System.out.println(s6 + " = " + s6.valeur()); //affiche ((18 - 4) - (56 - 43)) = 1
	    System.out.println(s7 + " = " + s7.valeur()); //affiche ((56 - 43) - (18 - 4)) = -1
	    
	     	
	    Expression m2 = new Multiplication(3,12);
	    Expression m3 = new Multiplication(quatre,dixHuit);
	    Expression m4 = new Multiplication(m2,m3);
	    Expression m5 = new Multiplication(m3,m2);
	    System.out.println(m2 + " = " + m2.valeur()); //affiche (3 * 12) = 36
	    System.out.println(m3 + " = " + m3.valeur()); //affiche (4 * 18) = 72
	    System.out.println(m4 + " = " + m4.valeur()); //affiche ((3 * 12) * (4 * 18)) = 2592
	    System.out.println(m5 + " = " + m5.valeur()); //affiche ((4 * 18) * (3 * 12)) = 2592
	    
	    Expression six = new Nombre(6);
	    Expression zero = new Nombre(0);
	    Expression d3 = new Division(15,3);
	    Expression d4 = new Division(zero,d3);
	    Expression d5 = new Division(d3,zero);
	    System.out.println(d3 + " = " + d3.valeur()); //affiche (15 / 3) = 5
	    System.out.println(d4 + " = " + d4.valeur()); //affiche (0 / (15 / 3)) = 0
	    try {
	    	System.out.println(d5 + " = " + d5.valeur()) ; // Affiche une erreur
	    }catch(ArithmeticException e) {
	    	System.out.println(e.getMessage() + " Impossible!!!");
	    }
	    
	    Expression a2 = new Addition(45,5);
	    Expression a3 = new Addition(a2,a1);
	    Expression a4 = new Addition(six,quatre);
	    Expression a5 = new Addition(a4,a3);
	    System.out.println(a2 + " = " + a2.valeur()); //affiche (45 + 5) = 50
	    System.out.println(a3 + " = " + a3.valeur()); //affiche ((45 + 5) + (2 + 3)) = 55
	    System.out.println(a4 + " = " + a4.valeur()); //affiche (6 + 4) = 10
	    System.out.println(a5 + " = " + a5.valeur()); //affiche ((6 + 4) + ((45 + 5) + (2 + 3))) = 65
	}
	
}