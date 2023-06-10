package aplicativo;

import contexto.Produto;
import estados.EmEstoque;
import estados.SemEstoque;
import estados.EmPromocao;

public class Main {
    public static void main(String[] args) {
        Produto produto1 = new Produto("Carrinho de controle remoto", new EmEstoque());
        Produto produto2 = new Produto("Boneca Barbie", new SemEstoque());
        Produto produto3 = new Produto("Jogo de tabuleiro", new EmPromocao());

        produto1.exibirEstado(); // Saída: O produto Carrinho de controle remoto está em estoque.

        produto2.exibirEstado(); // Saída: O produto Boneca Barbie está sem estoque.

        produto3.exibirEstado(); // Saída: O produto Jogo de tabuleiro está em promoção.

        produto1.atualizarEstado(new EmPromocao());
        produto1.exibirEstado(); // Saída: O produto Carrinho de controle remoto está em promoção.
    }
}
