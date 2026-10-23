package aula7;

//Não pode ser instanciada diretamente: new Voluntario() gera um erro de compilação
public abstract class Voluntario {

    private String nome;
    private String email;

    public Voluntario(String nome, String email) {
        this.nome = nome;
        this.email = email;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    //Metodo concreto: compartilhado por todas as subclasses
    public String getInfo() {
        return "Nome: " + this.nome + "| Email: " + this.email;
    }

    //MÉTODOS ABSTRATOS: Não tem corpo {} (implementação)
    //Obrigam qualquer classe filha concreta a implementar a loja especifica do metodo
    public abstract void realizarAcao();
    public abstract double calcularHorasDedicadas();

}
