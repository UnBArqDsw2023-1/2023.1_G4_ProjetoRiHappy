import java.awt.Image;

public class Produto {
    private String estado;
    private int estoque;
    private String nome;
    private float valor;
    private String descricao;
    private String marca;
    private String fichaTecnica;
    private Image imagem;

    public Produto(String nome, float valor, String descricao, String marca, String fichaTecnica, Image imagem) {
        this.estado = "SemEstoque";
        this.estoque = 0;
        this.nome = nome;
        this.valor = valor;
        this.descricao = descricao;
        this.marca = marca;
        this.fichaTecnica = fichaTecnica;
        this.imagem = imagem;
    }

    public void mudaEstado(String estado) {
        this.estado = estado;
    }
}
