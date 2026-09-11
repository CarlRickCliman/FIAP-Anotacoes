package aula2;

public class TelevisaoTeste {

    public static void main(String[] args){

        System.out.println(" --- Minha Televisão ---");

        //Criação do objeto de Televisão

        Televisao tv = new Televisao();

        System.out.println("Marca: " + tv.getMarca());
        System.out.println("Canal: " + tv.getCanal());
        System.out.println("Volume: " + tv.getVolume());
        System.out.println("Ligado: " + tv.getLigado());

        //Alterando o dados do objeto tv(forma direta)

        //tv.canal = 50;
        tv.setCanal(50);
        //tv.volume = 1000;
        tv.setVolume(1000);
        //tv.ligado = true;
        tv.setLigado(true);
        //tv.marca = LG;
        tv.setMarca("LG");

        System.out.println("\n------------------------------\n");

        System.out.println("Canal: " + tv.getCanal());
        System.out.println("Volume: " + tv.getVolume());
        System.out.println("Ligado: " + tv.getLigado());
        System.out.println("Marca: " + tv.getMarca());

    }
}
