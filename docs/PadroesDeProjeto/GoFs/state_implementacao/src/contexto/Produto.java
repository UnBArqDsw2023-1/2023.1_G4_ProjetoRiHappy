package contexto;

import estados.EstadoProduto;

public class Produto {
    private String nome;
    private EstadoProduto estado;

    public Produto(String nome, EstadoProduto estado) {
        this.nome = nome;
        this.estado = estado;
    }

    public void atualizarEstado(EstadoProduto novoEstado) {
        this.estado = novoEstado;
    }

    public void exibirEstado() {
        System.out.print("O produto " + nome + " está: ");
        estado.exibirEstado();
    }
}
