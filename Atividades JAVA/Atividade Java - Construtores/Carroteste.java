package aula1;

public class Carroteste {

    public static void main(String[] args) {

        // Construtor Padrão

        Carro carro1 = new Carro();

        System.out.println("Modelo: " + carro1.getModelo());
        System.out.println("Marca: " + carro1.getMarca());
        System.out.println("Cor: " + carro1.getCor());
        System.out.println("Ano: " + carro1.getAno());
        System.out.println("Preço: " + carro1.getPreco());
        System.out.println("----------------------------------------------");

        Carro carro2 = new Carro();

        carro2.exibirInfo();


        // Construtor Parametrizado com 2
        Carro carro3 = new Carro("Fiat", "Uno",  79000);

        carro3.setCor("Preto");
        carro3.setAno("2026");

        System.out.println("----------------------------------------------");
        System.out.println("Modelo: " + carro3.getModelo());
        System.out.println("Marca: " + carro3.getMarca());
        System.out.println("Cor: " + carro3.getCor());
        System.out.println("Ano: " + carro3.getAno());
        System.out.println("Preço: " + carro3.getPreco());
        System.out.println("----------------------------------------------");


        // Construtor Parametrizado com todos
        Carro carro4 = new Carro("Jeep", "Compass", "Azul", "2026", 129000);

        carro4.exibirInfo();

    }


}
