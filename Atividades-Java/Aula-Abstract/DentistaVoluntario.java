package aula7;

//Dentista deve implementar os métodos abtratos da super classe
public class DentistaVoluntario extends Voluntario {

    private String cro;
    private int consultasRealizadas;

    public DentistaVoluntario(String nome, String email, String cro, int consultasRealizadas) {
        super(nome, email);
        this.cro = cro;
        this.consultasRealizadas = consultasRealizadas;
    }

    public String getCro() {
        return cro;
    }

    public void setCro(String cro) {
        this.cro = cro;
    }

    public int getConsultasRealizadas() {
        return consultasRealizadas;
    }

    public void setConsultasRealizadas(int consultasRealizadas) {
        this.consultasRealizadas = consultasRealizadas;
    }

    @Override
    public void realizarAcao() {
        System.out.println("Realizando atendimento odontológico com o CRO: " + this.cro);
    }

    @Override
    public double calcularHorasDedicadas() {
        return this.consultasRealizadas * 1.5; //Média de atendimento em horas (1.5h/consulta)
    }
}
