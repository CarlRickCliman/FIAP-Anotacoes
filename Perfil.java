package modelo1;

public class Perfil {

    private Endereco endereco;
    private Notificacao notificacao;

    public Perfil(Endereco endereco) {
        this.endereco = endereco;
        this.notificacao = new Notificacao(this);

        System.out.println("Perfil criado com endereço.");
    }

}
