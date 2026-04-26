public class projeto2 implements Runnable {
    public void run(){
        System.out.println("Numero de 1 a 10 com intervalo de 1 segundo");
        for(int c =1;c < 11;c++){
            System.out.println(c);
        try {
            Thread.sleep(1000);
        }catch (InterruptedException e){
            e.printStackTrace();
        }
    }
    int contador = 2;
    for(int j=1;j<11;j++){
    try{
        Thread.sleep(2000);
        System.out.printf("A mensagem surgiu em %d segundos\n",contador);
        contador = contador + 2;
    }catch (InterruptedException e){
        e.printStackTrace();
            }
        }
    }

    public static void main(String[] args){
        projeto2 therad01 = new projeto2();
        Thread t = new Thread(therad01);
        t.start();

    }
}
