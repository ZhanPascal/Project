public class Nombre extends Expression{
  private int valeurNombre;

  public Nombre(int nb){
    this.valeurNombre = nb;
  }
  
  public Nombre(Nombre nb){
	    this.valeurNombre = nb.getValeurNombre();
	  }

  public int getValeurNombre(){
    return this.valeurNombre;
  }

  public void setValeurNombre(int n){
    this.valeurNombre = n;
  }

  public int valeur(){
    return this.valeurNombre;
  }

  public String toString(){
    return this.valeurNombre+"";
  }

}
