package Abstract;

public abstract class Doacao {

    private int id;
    private String doador;
    private double valorBase;

    public Doacao(int id, String doador, double valorBase) {
        this.id = id;
        this.doador = doador;
        this.valorBase = valorBase;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getDoador() {
        return doador;
    }

    public void setDoador(String doador) {
        this.doador = doador;
    }

    public double getValorBase() {
        return valorBase;
    }

    public void setValorBase(double valorBase) {
        this.valorBase = valorBase;
    }

    // Metodo concretos
    public void exibirResumo(int id, String doador) {
        System.out.println("ID da doação: " + this.id);
        System.out.println("Nome: " + this.doador);
    }

    // Metodos Abstratos

    public abstract double calcularTaxaAdministrativa();

    public abstract void processarDoacao();

}
