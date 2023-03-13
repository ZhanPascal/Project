public class Multiplication extends Operation{

  public Multiplication(int a, int b){
    super(a,b);
  }

  public Multiplication(Nombre a, Nombre b){
    super(a,b);
  }
  
  public Multiplication(Expression a, Expression b){
	    super(a,b);
	  }
  
  public Multiplication(Multiplication m){
	    super(m);
	  }
  
  public int valeur(){
      return this.getOperande1().valeur()*this.getOperande2().valeur();
  }

  public String toString(){
    return "("+this.getOperande1()+" * "+this.getOperande2()+")";
  }

}
