public class mainsin {
    public static void main(String[] args){
        Singleton singleton1 = Singleton.getInstancia();
        Singleton singleton2 = Singleton.getInstancia();
        if(singleton1 == singleton2){
            System.out.println("Instância Singleton criada!");
        }
    }
}
