// Classe Cliente
class Cliente {
  constructor(nome, email, cpf) {
    this.nome = nome;
    this.email = email;
    this.cpf = cpf;
  }

  novoCliente() {
    console.log('Novo cliente criado:', this.nome);
  }

  atualizarCliente(novoNome) {
    console.log(`Cliente ${this.nome} atualizado para ${novoNome}`);
    this.nome = novoNome;
  }

  autenticarCliente(email, cpf) {
    if (this.email === email && this.cpf === cpf) {
      console.log('Cliente autenticado com sucesso!');
    } else {
      console.log('Falha na autenticação. Verifique o email e o CPF.');
    }
  }
}
// Classe Produto
class Produto {
  constructor(categoria, nome, descricao, preco, imagem, estoque) {
    this.categoria = categoria;
    this.nome = nome;
    this.descricao = descricao;
    this.preco = preco;
    this.imagem = imagem;
    this.estoque = estoque;
  }

  static listarProdutos(produtos) {
    console.log('Lista de produtos:');
    produtos.forEach((produto) => {
      console.log(produto.nome);
    });
  }

  static filtrarProdutos(produtos, categoria) {
    console.log(`Produtos na categoria ${categoria}:`);
    const produtosFiltrados = produtos.filter((produto) => produto.categoria === categoria);
    produtosFiltrados.forEach((produto) => {
      console.log(produto.nome);
    });
  }

  static adicionarProduto(produtos, produto) {
    produtos.push(produto);
    console.log(`Produto "${produto.nome}" adicionado.`);
  }

  static removerProduto(produtos, produto) {
    const index = produtos.indexOf(produto);
    if (index !== -1) {
      produtos.splice(index, 1);
      console.log(`Produto "${produto.nome}" removido.`);
    }
  }
}
