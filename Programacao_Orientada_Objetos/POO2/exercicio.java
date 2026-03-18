import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JLabel;
import javax.swing.JButton;
import javax.swing.JTextFiled;
import javax.swing.JComboBox;
import javax.swing.JCheckBox;
import javax.swing.JPasswordField;
import java.awt.FlowLayout;
import java.awt.BorderLayout;

public class exercicio{
    public static void main(String[] args){
        JFrame tela = new JFrame();
        tela.setSize(350,250);
        tela.setTitle("Exercicio");
        tela.setDefaultCloseOperatoin(JFrame.EXIT_ON_CLOSE);
        


        JPanel pn1 = new JPanel(new FlowLayout(FlowLayout.CENTER));
        pn1.add(new JLabel("Tela de Cadastro"));
        tela.getContentPane().add(pn1,BorderLayout.NORTH);
        
        JPanel pn2 = new JPanel(new FlowLayout(FlowLayout.LEFT));
        pn2.add(new JLabel("Nome"));
        pn2.add(new JTextFiled(30));
        pn2.add(new JLabel("Senha"));
        pn2.add(new JPasswordField(30));
        pn2.add(new JLabel("Cidade"));
        pn2.add(new JComboBox(new String[] {"Cidade01","Cidade02","Cidade03"}));
        pn2.add(new JCheckBox("Casado"));
        tela.getContentPane().add(pn2,BorderLayout.CENTER);

        JPanel pn3 = new JPanel(new FlowLayout(FlowLayout.CENTER));
        pn3.add(new JButton("Salvar"));
        pn3.add(new JButton("Alterar"));
        pn3.add(new JBUtton("Cancelar"));
        tela.getContentPane().add(pn3,BorderLayout.SOUTH);
        tela.setLocalitionRelative(null);
        tela.setvisible(true);

        
    }
}
