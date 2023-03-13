public class Division extends Operation {

  public Division(Nombre a, Nombre b){
    super(a,b);
  }

  public Division(int a, int b){
    super(a,b);
  }
  
  public Division(Expression a, Expression b){
	    super(a,b);
	  }
  
  public Division(Division d){
	    super(d);
	  }

  public int valeur(){
      return this.getOperande1().valeur() / this.getOperande2().valeur();
  }

  public String toString(){
    return "(" +this.getOperande1() +" / "+this.getOperande2() +")";
  }
}
