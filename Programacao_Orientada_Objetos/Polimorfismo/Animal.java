package Programacao_Orientada_Objetos.Polimorfismo;

public class Animal {
    private String tipo;
    private String nome;
    private int idade;

    public void emitir_som(String som){
        System.out.println(som);
    }

    public void setnome(String nome){
        this.nome = nome;
    }
    public String getnome(){
        return nome;
    }

    public void settipo(String tipo){
        this.tipo = tipo;
    }
    public String gettipo(){
        return tipo;
    }
    public void settidade(int idade){
        this.idade = idade;
    }
    public int getidade(){
        return idade;
    }

}
