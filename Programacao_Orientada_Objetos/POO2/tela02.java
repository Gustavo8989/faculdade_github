package POO2

import javax.swing.JFrame; 
import javax.swing.JLabel; 
import javax.swing.JTextField; 
import javax.swing.JPasswordField;
import javax.swing.JTextArea;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JCheckBox;
import javax.swing.JPanel;

public class tela02 {
    public static void main(String[] args) { 
        
        JFrame tela = new JFrame(); // Cria o objeto da janela
        tela.setTitle("Primeira aplicação GUI"); // Define o título da barra superior
        tela.setSize(300, 300); // Define largura e altura da janela em pixels
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Encerra o programa ao fechar a janela
        tela.setLocationRelativeTo(null); // Centraliza a janela no meio da tela
        tela.setResizable(true); // Permite que o usuário redimensione a janela
        
        tela.getContentPane().setLayout(null); // Desativa o layout automático (permite usar coordenadas X e Y)
        
        // Componente JLabel que cria um rótulo de texto

        JLabel label = new JLabel("Aula 01 POO"); // Cria um rótulo de texto
        label.setBounds(5, 5, 100, 20); // Define posição (x,y) e tamanho (largura, altura) do rótulo
        label.setToolTipText("TopTip - aula"); // Mensagem que aparece ao passar o mouse sobre o texto
        
        // Componente JTextField faz com que aparece um caixa de texto na interface

        JTextField textField = new JTextField(); // Cria uma caixa de entrada de texto
        textField.setColuns(30); // Coluna o tamanho da caixa de texto 
        textField.setBounds(15,60,100,200);
        textField.setEditable(true);

        // Componente JPassowordField utilizados para caixa de texto com senha 

        JPasswordField password = new JPasswordField();
        password.setToolTipText("Digite a sua senha");
        password.setColuns(30);
        password.setBounds(5,30,100,200);
        password.setEnabled(true);

        // Componente JTextArea 

        JTextArea area = new JTextArea();
        area.setColuns(10);
        area.setRows(3);
        area.setBounds(5,30,100,200);
        area.setEnabled(true);

        // Componente JButton 
        
        JButton botao = new JButton();
        botao.setText("Salvar");
        botao.setMnemonic('s');
        botao.setBounds(5,30,100,200);

        // Componente JComboBox cria um botão que apertado mostra diversos opções

        String[] itens = new String[] {"Item1","Item2","Item3","Item4"};
        JcomboBox box =  new JComboBox();
        combo.setBounds(5,10,80,30);
        combo.setEnabled(true);

        // Componente JCheckBox
        JCheckBox checkbox = new CheckBox();
        checkbox.setText("Texto checkbox");
        checkbox.setBounds(10,10,200,30);
        checkbox.setEnabled(true);

        // Componente Panel Criando um Painel 

        JPanel painel = new JPanel();
        panel.setLayout(new FlowLayout);
        JButton button = new JButton();
        button.setText("Botão");
        button.setBounds(5,30,100,200);

        panel.add(button);


        tela.getContentPane().add(textField);
        tela.setVisible(true); // Torna a janela visível (deve ser o último passo)
    }
}
