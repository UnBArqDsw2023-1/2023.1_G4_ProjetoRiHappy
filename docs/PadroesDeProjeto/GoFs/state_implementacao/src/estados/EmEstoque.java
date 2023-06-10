package estados;

public class EmEstoque extends EstadoProduto {
    @Override
    public void exibirEstado() {
        System.out.println("O produto está em estoque.");
    }
}
