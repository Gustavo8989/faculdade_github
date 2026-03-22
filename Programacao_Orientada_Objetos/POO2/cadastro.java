import java.awt.Container;
import java.text.ParseException;
import java.swing.*;
import java.swing.text.MaskFormatter;

// Definindo os atributos que iram aparecer na Tela
public class PrimeiraTela extends JFrame{
    private JLabel lblNome;
    private JTextField txtnome;
    private JLabel lblCpf;
    private JTextField txtCpf;
    private JLabel lblTipo;
    private jComboBox cmbTipo;
    private final String[] tipoUsuario = {"Administrador","Geral"};
    private JButton btnOk;
    private Container ctn;
}

public PrimeiraTela(){
    setSize(400,300);
    setTitle("Tela de login");
    ctn = getContentPane();
    // Instanciando os elementos
    lblNome = new JLabel("Nome");
    txtNome = new JTextField();
    lblCpf = new JLabel("CPF");
    try{
        txtCpf = new JFormattedTextField(new MaskFormatter("###.###.###.##"));
    }catch(ParseException e){
        e.printStackTracel();
    }
    lblTipo = new JLabel("Tipo de usuario");
    cmbTipo = new jComboBox(tipoUsuario);
    btnOk = new JButton("Enviar");
    ctn.setLayout(null);
    // Configurando as posições do componente 
    lblNome.setBounds(0,0,100,25);
    txtNome.setBounds(150,0,200,25);
    lblCpf.setBounds(0,50,100,25);
    txtCpf.setBounds(150,50,200,25);
    lblTipo.setBounds(0,100,200,25);
    cmbTipo.setBounds(150,100,200,25);
    btnOk.setBounds(150,150,100,100);
    ctn.add(lblNome);
    ctn.add(txtNome);
    ctn.add(lblCpf);
    ctn.add(txtCpf);
    ctn.add(lblTipo);
    ctn.add(cmbTipo);
    ctn.add(btnOk);
    setVisible(true);
    setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
}
