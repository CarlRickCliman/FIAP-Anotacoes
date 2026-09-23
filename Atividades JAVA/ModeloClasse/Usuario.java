package modelo1;

public class Usuario {

    private String nome;
    private Perfil perfil;
    private Carrinho carrinho;

    public Usuario(String nome, Perfil perfil) {
        this.nome = nome;
        this.perfil = perfil;
        this.carrinho = new Carrinho(this);

        System.out.println("Usuário criado: " + nome);
    }

    public Carrinho getCarrinho() {
        return carrinho;
    }
}
