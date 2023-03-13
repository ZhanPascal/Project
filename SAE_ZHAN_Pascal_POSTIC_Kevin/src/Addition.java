public class Addition extends Operation{

  public Addition(int a, int b){
    super(a,b);
  }

  public Addition(Nombre a, Nombre b){
    super(a,b);
  }
  
  public Addition(Expression a, Expression b){
	    super(a,b);
	  }
  
  public Addition(Addition a){
	    super(a);
	  }


  public int valeur(){
    return this.getOperande1().valeur()+this.getOperande2().valeur();
  }

  public String toString(){
    return "(" +this.getOperande1() +" + "+this.getOperande2()+")";
  }
}
