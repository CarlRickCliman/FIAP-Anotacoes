package modelo1;

public class Produto {

    private double preco = 99.90;
    private String nome;
    private Estoque estoque;

    public Produto(String nome) {
        this.nome = nome;
        this.estoque = new Estoque(this);

        System.out.println("Produto criado: " + nome + " - R$ " + preco);
    }
}
