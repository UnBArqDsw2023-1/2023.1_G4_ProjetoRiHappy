abstract class PaymentFactory {

    abstract GerarPagamento(name:string, cpf:string, endereco:string): Payment;
    
}


class CartaoFactory extends PaymentFactory {
    public GerarPagamento(name:string, cpf:string, endereco:string): Payment {
        return new Cartao(name, cpf, endereco,);
    }
}

class PixFactory extends PaymentFactory {
    public GerarPagamento(name:string, cpf:string, endereco:string): Payment {
        return new Pix(name, cpf, endereco);
    }
} 

class BoletoFactory extends PaymentFactory{
    public GerarPagamento(name:string, cpf:string, endereco:string): Payment{
        return new Boleto(name, cpf, endereco);
    }
}

//Criado interface
interface Payment {
    GerarNF():String;
}

class Cartao implements Payment {
    constructor(private name:string, private cpf:string, private endereco:string){}

    GerarNF(): String {
        return `Nota Fiscal do Cartao: ${this.name} ${this.cpf} ${this.endereco}`
    }
}

class Pix implements Payment {
    constructor(private name:string, private cpf:string, private endereco:string){}

    GerarNF(): String {
        return `Nota Fiscal do Pix: ${this.name} ${this.cpf} ${this.endereco}`
    }
}

class Boleto implements Payment {
    constructor(private name:string, private cpf:string, private endereco:string){}

    GerarNF(): String {
        return `Nota Fiscal do Boleto: ${this.name} ${this.cpf} ${this.endereco}`
    }
}


console.log('Testando BoletoFactory.');

const boletoFactory = new BoletoFactory(); //crio a factory
const boleto1 = boletoFactory.GerarPagamento("joao", "12345678900", "Rua Alagoas"); //crio o objeto boleto
console.log(boleto1.GerarNF())
const boleto2 = boletoFactory.GerarPagamento("Cleber", "23487654890", "Rua Jabuti"); //crio o objeto boleto
console.log(boleto2.GerarNF())

console.log(' ')

console.log('Testando PixFactory.');

const pixFactory = new PixFactory();
const pix1 = pixFactory.GerarPagamento("Maria", "09876543210", "rua Salvador");
console.log(pix1.GerarNF())
const pix2 = pixFactory.GerarPagamento("Beto", "09246238210", "rua Pirenol");
console.log(pix2.GerarNF())

console.log(' ')

console.log('Testando CartaoFactory.');

const cartaoFactory = new CartaoFactory();
const cartao1 = cartaoFactory.GerarPagamento("Jorge", "23415612334", "Rua Maringa")
console.log(cartao1.GerarNF())
const cartao2 = cartaoFactory.GerarPagamento("Carlos", "23415698734", "Rua Betinho")
console.log(cartao2.GerarNF())