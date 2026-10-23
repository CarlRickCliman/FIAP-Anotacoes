package Abstract;

public class DoacaoDinheiro extends Doacao{

    private String meioPagamento;

    public DoacaoDinheiro(int id, String doador, double valorBase, String meioPagamento) {
        super(id, doador, valorBase);
        this.meioPagamento = meioPagamento;
    }

    public String getMeioPagamento() {
        return meioPagamento;
    }

    public void setMeioPagamento(String meioPagamento) {
        this.meioPagamento = meioPagamento;
    }

    @Override
    public double calcularTaxaAdministrativa() {
        setValorBase(getValorBase() * 0.02);
        return 0;
    }

    @Override
    public void processarDoacao() {
        System.out.println("Meio de pagamento: " + this.meioPagamento);
        System.out.println("Processando doação via " + getMeioPagamento() + "...");
    }
}
