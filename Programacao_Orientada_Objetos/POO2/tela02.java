package POO2

import javax.swing.JFrame;
import java.swing.JLabel;

public class tela02 {
    public staci void main(String[] args){
        JFrame tela = new Frame();
		tela.setTitle("Primeira aplicação GUI");
		tela.setSize(300,300);
		tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		tela.setLocationRelativeTo(null);


        tela.getContentPane.setLayout(null);
        JLabel label = new JLabel("Aula 01");
        label.setBounds(5,5,100,20) ;
        label.setToolTipText("ToolTip - Aula01");
        tela.getContentPane.add(label);
        tela.setResizable(true);
        tela.setsetVisible(true);


    }
}


