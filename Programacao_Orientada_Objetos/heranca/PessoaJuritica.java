package Programacao_Orientada_Objetos.heranca;

public class PessoaJuritica extends Pessoas{
    private String cnpj;

    private String getCNPJ(){
        return cnpj;
    }
    private void setCNPJ(String cnpj){
        this.cnpj = cnpj;
    }
}
