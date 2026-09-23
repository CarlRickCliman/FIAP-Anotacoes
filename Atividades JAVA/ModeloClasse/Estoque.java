package modelo1;

public class Estoque {

    private Produto produto;
    private int quantidade;

    public Estoque(Produto produto) {
        this.produto = produto;
        this.quantidade = 20;
        System.out.println("Estoque criado com " + quantidade + " unidades.");
    }
}
