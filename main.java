package modelo1;

public class main {

    public static void main(String[] args) {

        System.out.println("=== INÍCIO DO PROGRAMA ===");

        // 1. Cria um endereço
        Endereco endereco = new Endereco(
                "São Paulo",
                "Rua das Flores"
        );

        // 2. Cria um perfil usando o endereço
        Perfil perfil = new Perfil(endereco);

        // 3. Cria um usuário usando o perfil
        Usuario usuario = new Usuario(
                "João",
                perfil
        );

        // 4. Cria um produto
        Produto produto = new Produto("Notebook");

        // 5. Pega o carrinho que já foi criado pelo Usuario
        Carrinho carrinho = usuario.getCarrinho();

        // 6. Adiciona o produto ao carrinho
        carrinho.adicionarProduto(produto);

        // 7. Finaliza a compra
        carrinho.finalizar();

        System.out.println("=== FIM DO PROGRAMA ===");
    }
}
