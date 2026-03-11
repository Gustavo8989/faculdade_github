package POO2;

import javax.swing.JFrame;

public class interface_grafica {
    public static void main(String[] args){
        JFrame tela = new JFrame();
        tela.setTitle("Minha primeira tela GUI");
        tela.setSize(300,300);
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        tela.setLocationRelativeTo(null);
        tela.setResizable(true);
        tela.setVisible(true);

    }
}
