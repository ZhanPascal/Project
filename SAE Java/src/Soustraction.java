public class Soustraction extends Operation{

  public Soustraction(int a,int b){
    super(a,b);
  }

  public Soustraction(Nombre a, Nombre b){
    super(a,b);
  }
  
  public Soustraction(Expression a, Expression b){
	    super(a,b);
	  }

  public Soustraction(Soustraction s){
	    super(s);
	  }
  
  public int valeur(){
    return this.getOperande1().valeur()-this.getOperande2().valeur();
  }

  public String toString(){
    return "("+this.getOperande1()+" - "+this.getOperande2()+")";
  }
}
