package aula7;

public class EducadorVoluntario extends Voluntario {

    private int oficinaMinistradas;

    public EducadorVoluntario(String nome, String email, int oficinasMinistradas) {
        super(nome, email);
        this.oficinaMinistradas = oficinasMinistradas;
    }


    public int getOficinaMinistradas() {
        return oficinaMinistradas;
    }

    public void setOficinaMinistradas(int oficinaMinistradas) {
        this.oficinaMinistradas = oficinaMinistradas;
    }

    @Override
    public void realizarAcao() {
        System.out.println("Ministrando a oficina de higiene bucal e prevenção");
    }

    @Override
    public double calcularHorasDedicadas() {
        return oficinaMinistradas * 2.0; //Média de 2h por oficina
    }
}
