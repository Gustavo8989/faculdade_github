package Programacao_Orientada_Objetos;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class tela {
    public static void main(String args){
         Funcionario funcionario = new Funcionario();
         funcionario.setData("Gustavo Henrique",190,LocalDate.of(2005,11,06),"5425505460","Rua não sei","Holambra");
         funcionario .getData(); 
         List<Funcionario> lista_funcionario = new ArrayList<>();
    }    
}
