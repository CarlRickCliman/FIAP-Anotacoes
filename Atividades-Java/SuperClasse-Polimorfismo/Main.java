package aula6;

public class Main {


    //Metodo que aceita qualquer tipo de notificação - O coraçao do Polimorfismo
    public static void dispararAlerta(Notificacao notificacao) {
        System.out.println("\n [SISTEMA DE ALERTA]");
        notificacao.enviar(); //O java decide em tempo de execução qual metodo enviar() será chamado.
    }

    public static void main(String[] args) {

        // Declaração de tipo genérico (Generics) apontando para instâncias específicas

        //Generalização - Especialização
        //     ^                ^
        Notificacao n1 = new Email("aluno@fiap.com.br", "CP realizado com sucesso!!", "Aviso importante");
        Notificacao n2 = new SMS("1199999-8888", "Aula de hoje - Não se atrase!");

        // Chamada Direta
        n1.enviar();
        n2.enviar();

        //Usando o metodo POLIMORFICO sem condicionais
        dispararAlerta(n1);
        dispararAlerta(n2);

        //Usando o metodo POLIMORFICO com condicionais
        // 1 - Email
        // 2 - SMS
        int tipoCanal = 2;
        Notificacao notificaoEscolhida = null;

        if(tipoCanal == 1) {
            notificaoEscolhida = new Email("aluno2@fiap.com.br", "Alo turma!", "Aula de Java");
        } else if(tipoCanal == 2) {
            notificaoEscolhida = new SMS("1197777-1111","Aula de hoje, estamos quase terminando...");
        }

        //Não importa o tipo de dado concreto, o metodo trata TODOS como notificacao
        dispararAlerta(notificaoEscolhida);
    }
}
