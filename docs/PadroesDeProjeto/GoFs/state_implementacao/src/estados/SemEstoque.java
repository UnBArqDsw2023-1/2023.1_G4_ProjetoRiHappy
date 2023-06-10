package estados;

public class SemEstoque extends EstadoProduto {
    @Override
    public void exibirEstado() {
        System.out.println("O produto está sem estoque.");
    }
}