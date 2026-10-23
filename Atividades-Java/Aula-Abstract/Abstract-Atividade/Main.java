package Abstract;

public class Main {
    public static void main(String[] args) {

        //Tentar instanciar classe abstrata, mostra a mensagem:
        // 'Doacao' is abstract; cannot be instantiated
        //Doacao doacao = new Doacao();

        DoacaoDinheiro doacao1 = new DoacaoDinheiro(10, "Carlos Henrique", 20.0, "PIX");

        DoacaoSuprimento doacao2 = new DoacaoSuprimento(11, "Anny Gabrielly", 40.50, 22.0);

        emitirComprovante(doacao1);
        System.out.println("-----------------------------------------------------------------------------");
        emitirComprovante(doacao2);


    }

    public static void emitirComprovante(Doacao d) {
        System.out.println("--- COMPROVANTE ---");
        System.out.println("ID do doador:" + d.getId());
        System.out.println("Nome do doador:" + d.getDoador());
        System.out.println("Valor base:" + d.getValorBase());
        d.calcularTaxaAdministrativa();
        d.processarDoacao();
        System.out.println("----Taxa Administrativa: " + d.getValorBase() + "----");


    }
}
