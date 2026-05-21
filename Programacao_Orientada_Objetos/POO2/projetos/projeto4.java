import java.sql.*;

public class projeto4 {
        private static final String URL = "jdbc:mysql://localhost:3306/cadastro";
        private static final String USUARIO = "root";
        private static final String SENHA = "user_senha";
    
    private static void main(String[] args){
        try{
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conexao = DriverManager.getConnection(URL,USUARIO,SENHA);
            Statement stmt = getConexao().createStatement();
            ResultSet rs   = stmt.executeQuery("SELECT id, nome, email FROM clientes");
            System.out.println("\n┌────┬────────────────────┬──────────────────────────┐");
            System.out.println("│ ID │ Nome               │ Email                    │");
            System.out.println("├────┼────────────────────┼──────────────────────────┤");
            while (rs.next()){
                System.out.printf("│ %-2d │ %-18s │ %-24s │%n",
                    rs.getInt("id"),
                    rs.getString("nome"),
                    rs.getString("email")
                );
            }
            conexao.close();
        }catch(ClassNotFoundException | SQLException e){
            System.out.println("X Erro" + e.getMessage());
        }
    }
}
