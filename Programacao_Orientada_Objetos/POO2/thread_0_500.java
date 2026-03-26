public class thread_0_500 extends Thread{
    public void run(){
        System.out.println("Minha Thread em java");
        Sustem.out.println(Thread.currentThread().getName());
        // loop até 500 
        for (int c = 0; c < 500; c++){
            System.out.println("Fazendo Download");
        }
    }
    public static void main(String[] args){
        thread_0_500 t = new thread_0_500();
        t.setName("Thread 3");
        t.start();
        for(int c = 0; c< 500; c++){
            System.out.println("Executado um programa.... ")
        }

    }
}
