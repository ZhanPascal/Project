public abstract class Operation extends Expression{
  private Expression operande1;
  private Expression operande2;

  public Operation(Nombre a, Nombre b){
    this.operande1 = a;
    this.operande2 = b;
  }
  public Operation(Expression a, Expression b){
	    this.operande1 = a;
	    this.operande2 = b;
	  }
  
  public Operation(Operation o) {
	  	this.operande1 = o.getOperande1();
	    this.operande2 = o.getOperande2();
  }

  public Operation(int a, int b){
    this.operande1 = new Nombre(a);
    this.operande2 = new Nombre(b);
  }

  public abstract int valeur();

  public Expression getOperande1(){
    return this.operande1;
  }

  public Expression getOperande2(){
    return this.operande2;
  }

  public void setOperande1(Nombre n){
    this.operande1 = n;
  }

  public void setOperande2(Nombre n){
    this.operande2 = n;
  }

}
