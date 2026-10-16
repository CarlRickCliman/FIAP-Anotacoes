package aula6;

public class Notificacao {

    private String destinatario;
    private String mensagem;

    public Notificacao(String destinatario, String mensagem) {
        this.destinatario = destinatario;
        this.mensagem = mensagem;

    }

    public String getDestinatario() {
        return destinatario;
    }

    public void setDestinatario(String destinatario) {
        this.destinatario = destinatario;
    }

    public String getMensagem() {
        return mensagem;
    }

    public void setMensagem(String mensagem) {
        this.mensagem = mensagem;
    }

    //comportamento genérico que será SOBRESCRITO (Override)
    public void enviar() {
        System.out.println("Enviando uma mensagem (genérica) para " + this.destinatario);
    }
}
