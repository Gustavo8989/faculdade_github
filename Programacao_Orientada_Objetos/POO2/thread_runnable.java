public class thread_runnable implements Runnable{
    @Override
    public void run(){
        System.out.println(Thread.currentThread().getName());
    }
    public static void main(String[] args){
        thread_runnable t = new thread_runnable();
        Thread thread = new Thread();
        thread.setName("Thread Runnable");
        thread.setpr
    }
}
