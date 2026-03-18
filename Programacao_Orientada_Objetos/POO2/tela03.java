

import javax.swing.JFrame;
import javax.swing.JButton;
import javax.awt.BorderLayout;
import javax.awt.FlowLayout;

public class tela03{
    public static void main(String[] args){
        // Criando uma tela com JFrame
        JFrame tela = new JFrame();
        tela.setSize(500,500);
        tela.setTitle("Layout");
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        // Incluindo componentes na tela 
        // BorderLayout
        tela.getContentPane().add(new JButton("Centro"),BorderLayout.CENTER);
        tela.getContentPane().add(new JButton("Norte"),BorderLayout.NORTH);
        tela.getContentPane().add(new JButton("Sul"),BorderLayout.SOUTH);
        tela.getContentPane().add(new JButton("Oeste"),BorderLayout.WEST);
        tela.getContentPane().add(new JButton("Leste"),BorderLayout.EAST);
        
         // Flow Layout 
        tela.getContentPane.setLayout(new FlowLayout(FlowLayout.CENTER)); // Onde vai começar nosso Layout(Left,right)
        tela.getContentPane.add(new JButton("Botao 1"));
        tela.getContentPane.add(new JButton("Botao 2"));
        tela.getContentPane.add(new JButton("Botao 3"));
        tela.getContentPane.add(new JButton("Botao 4"));
        tela.getContentPane.add(new JButton("Botao 5"));
        tela.getContentPane.add(new JButton("Botao 6"));
 
        // Grid Layout 

        tela.getContentPane().setLayout(new GridLayout(3,3));
        tela.getContentPane().add(new JButton("botao 1"));
        tela.getContentPane().add(new JButton("botao 2"));
        tela.getContentPane().add(new JButton("botao 3"));
        tela.getContentPane().add(new JButton("botao 4"));
        tela.getContentPane().add(new JButton("botao 5"));
        tela.getContentPane().add(new JButton("botao 6"));
        tela.getContentPane().add(new JButton("botao 7"));
        tela.getContentPane().add(new JButton("botao 8"));
        tela.getContentPane().add(new JButton("botao 9"));

        tela.setLocationRelative(null);
        tela.setVisible(true);

    }
}
