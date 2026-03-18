

import javax.swing.JFrame;
import javax.swing.JButton;
import javax.awt.BorderLayout;

public class tela03{
    public static void main(String[] args){
        // Criando uma tela com JFrame
        JFrame tela = new JFrame();
        tela.setSize(500,500);
        tela.setTitle("BorderLayout");
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Incluindo componentes na tela 
        
        tela.getContentPane().add(new JButton("Centro"),BorderLayout.CENTER);
        tela.getContentPane().add(new JButton("Norte"),BorderLayout.NORTH);
        tela.getContentPane().add(new JButton("Sul"),BorderLayout.SOUTH);
        tela.getContentPane().add(new JButton("Oeste"),BorderLayout.WEST);
        tela.getContentPane().add(new JButton("Leste"),BorderLayout.EAST);


        tela.setLocationRelative(null);
        tela.setVisible(true);

    }
}
