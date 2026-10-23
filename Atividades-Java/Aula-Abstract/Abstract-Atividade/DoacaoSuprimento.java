package Abstract;

public class DoacaoSuprimento extends Doacao{

    private double pesoKG;

    public DoacaoSuprimento(int id, String doador, double valorBase, double pesoKG) {
        super(id, doador, valorBase);
        this.pesoKG = pesoKG;
    }

    public double getPesoKG() {
        return pesoKG;
    }

    public void setPesoKG(double pesoKG) {
        this.pesoKG = pesoKG;
    }

    @Override
    public double calcularTaxaAdministrativa() {
        setValorBase(getPesoKG() * 5.0);
        return 0;
    }

    @Override
    public void processarDoacao() {
        System.out.println("Agendando triagem e transporte para " + this.pesoKG + "kg de suprimentos.");
    }
}
