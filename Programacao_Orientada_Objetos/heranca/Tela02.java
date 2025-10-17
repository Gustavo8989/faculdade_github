package Programacao_Orientada_Objetos.heranca;

public class Tela02 {
    public static void main(String[] args){
         System.out.println("Aula de POO");
         PessoaFisica pessoa_fisica = new PessoaFisica();
         PessoaJuritica pessoa_juridica = new PessoaJuritica();
         pessoa_fisica.setCodigo(1209);
         pessoa_fisica.setCodigo(0);
         pessoa_juridica.setCodigo(324);
         pessoa_juridica.gravar();
         System.out.printf("Código: " + pessoa_juridica.getCodigo());
    }
}
