package Programacao_Orientada_Objetos.heranca;

public class Pessoas {
    private int codigo;
    private String nome;
    private String endereco;

    public void gravar(){
        System.out.println("Gravando informações: ");
    }

    public int getCodigo(){
        return codigo;
    }

    public void setCodigo(int codigo){
        this.codigo = codigo;
    }  

}