package Programacao_Orientada_Objetos;
import java.util.Date;
import java.time.LocalDate;

public class Funcionario {
    private int matricula;
    private String nome;
    private Date dataNecimento;
    private String cpf;
    private String endereco;
    private String cidade; 

    public void setData(String nome, int matricula, String cpf, String endereco, String cidade ){
        this.nome = nome;
        this.matricula = matricula;
        //this.dataNecimento = dataNecimento;
        this.cpf = cpf;
        this.endereco = endereco;
        this.cidade = cidade;
    }

    public String getData(){
        return nome;
    }
    @Override
    public String toString() {
        return "Funcionario{" +
               "nome='" + nome + '\'' +
               ", matricula='" + matricula + '\'' +
               ", Endereço='" + endereco + '\'' +
               ", cpf='" + cpf + '\'' +
               ", cidade='" + cidade + '\'' +
               '}';
    }
}