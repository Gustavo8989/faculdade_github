import javax.swing.JFrame;

public class projeto1 {
    public static void main(String[] args){
        JFrame tela = new JFrame();
        tela.setTitle("Projeto 1");
        tela.setSize(400,200);
        tela.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        tela.setLocationRelativeTo(tela);
        tela.setResizable(true);
        tela.setVisible(true);
    }
}
