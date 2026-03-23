public class thread implements Runnable{

    public void run(){
        System.out.println(Thread.currentThread().getName());
    }
    public static void main(String[] args){
          thread t = new thread2;
          thread Thread = new Thread(t);
          Thread.start();



    }
}   
