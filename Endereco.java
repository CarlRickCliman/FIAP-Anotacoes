package modelo1;

public class Endereco {

    private String cidade;
    private String rua;

    public Endereco(String cidade, String rua) {
        this.cidade = cidade;
        this.rua = rua;

        System.out.println("Endereço: " + rua + ", " + cidade);
    }
}
