package aula6;

public class SMS extends Notificacao{


    public SMS(String destinatario, String mensagem) {
        super(destinatario, mensagem);
    }

    @Override
    public void enviar() {
        System.out.println("---> Enviando SMS");
        System.out.println("Celular:" + getDestinatario());
        System.out.println("Mensagem: " + getMensagem());
    }
}
