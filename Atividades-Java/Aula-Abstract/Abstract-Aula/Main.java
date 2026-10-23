package aula7;

public class Main {
    public static void main(String[] args) {

        //1. Tentar instanciar a classe abstrata
        //Voluntario v = new Voluntario();

        //2.Criando instancia das classes concretas
        DentistaVoluntario dentista = new DentistaVoluntario("Dra. Maria", "maria@email.org", "SP-123456", 4);
        EducadorVoluntario educador = new EducadorVoluntario("Pedro", "pedro@email.org", 2);

        //3. Executando os métodos de FORMA DIRETA
        System.out.println("--- Voluntário 1 ---");
        System.out.println(dentista.getInfo());
        dentista.realizarAcao();
        System.out.println("Horas: " + dentista.calcularHorasDedicadas() + "h");

        System.out.println("--- Voluntário 2 ---");
        System.out.println(educador.getInfo());
        educador.realizarAcao();
        System.out.println("Horas: " + educador.calcularHorasDedicadas() + "h");

    }
}
