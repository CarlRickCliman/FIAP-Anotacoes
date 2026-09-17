package modelo1;

public class Pagamento {

    private String status = "PENDENTE";
    private Carrinho carrinho;
    private Notificacao notificacao;

    public Pagamento(Carrinho carrinho) {
        this.carrinho = carrinho;
        this.notificacao = new Notificacao(null);

        System.out.println("Pagamento criado. Status: " + status);
    }
}
