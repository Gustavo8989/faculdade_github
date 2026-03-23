

public class thread extends Thread{
    public thread(){
        start();

    }
    public void run(){
        System.out.println("Minha primeira Thread");
    }
    public static void main(String[] args){
        new thread();
    }
}
