package Programacao_Orientada_Objetos;


import java.util.Date;

public class Funcionario {
    private int matricula;
    private String nome;
    private Date dataNecimento;
    private String cpf;
    private String endereco;
    private String cidade;

    public void setNome(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return this.nome;
    }

    public void calcSalario(double salario){
        System.out.println("Salario do " + this.nome + " é de " + salario);
    }
}