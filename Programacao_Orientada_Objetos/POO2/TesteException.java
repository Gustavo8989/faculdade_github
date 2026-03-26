

public class TesteException{
    public TesteException(){
        try{
            teste(8);

        }catch(exception e){
            e.printStackTrace();
        }finally{
            System.out.println("Finalizei a execucao utilizando o bloco Finally");
    }
    private void teste(int media) throws exception{
        if (media < 7){
            throws new exception("esta de recuperação");
        }
    }
    public static void main(String[] args){
        new TesteException(); // Invocar o construtor vamos contrutir o nosso objetos

}
