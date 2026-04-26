import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;

import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.Dimension;

import javax.swing.JButton;
import javax.swing.JCheckBox;
import javax.swing.JComboBox;

public class projeto1 {
    public static void main(String[] args){
        JFrame tela = new JFrame();
        tela.setTitle("Projeto 1");
        tela.setSize(400,200);
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        tela.setLocationRelativeTo(tela);

        JPanel painel = new JPanel();
        painel.setLayout(new FlowLayout());

        String[] options = {"Eletronicos","Roupas","Alimentos"};
        JComboBox<String> combox = new JComboBox<>(options);
        combox.setFont(new Font("Arial",Font.PLAIN,10));
        combox.setEnabled(true);
        
        JCheckBox checkBox = new JCheckBox(null,null,false);
        checkBox.setEnabled(true);

        JTextField texto = new JTextField();
        texto.setPreferredSize(new Dimension(50, 25));
        texto.setEnabled(true);

        JButton button_salvar = new JButton();
        button_salvar.setText("Salvar");
        button_salvar.setEnabled(true);

        JButton button_sair = new JButton();
        button_sair.setText("Sair");
        button_sair.setEnabled(true);

        painel.add(combox);
        painel.add(checkBox);
        painel.add(texto);
        painel.add(button_salvar);
        painel.add(button_sair);
        tela.add(painel);
        tela.setResizable(true);
        tela.setVisible(true);
        
    }
}
