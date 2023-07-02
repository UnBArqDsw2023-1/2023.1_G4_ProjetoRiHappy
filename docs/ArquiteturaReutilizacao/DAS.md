# Documento de Arquitetura de Software - DAS

## 1. Introdução
### 1.1 Finalidade
Este documento oferece uma visão arquitetural geral do sistema, usando diversas
visões arquiteturais para representar diferentes aspectos do mesmo. O objetivo deste
documento é capturar e comunicar as decisões arquiteturais significativas que foram
tomadas no decorrer do processo de desenvolvimento.
### 1.2 Escopo

O projeto possui foco em compreender o melhor o perfil de um comprador do site da RiHappy, alem de entender o fluxo de cadastro na plataforma e de perceber os processos de  vizualização, compra e pagamento dos produto.

### 1.3 Visão Geral

Após a introdução, é possível obter uma compreensão básica sobre o DAS e seu propósito. Em seguida, o documento prossegue fornecendo uma visão mais detalhada da arquitetura do projeto, abrangendo tanto sua forma geral quanto cada uma de suas visões (lógica, implementação, implantação e dados).
## 2. Representação Arquitetural


[Escrever sobre como o artefato foi ou será feito.]

## 3. Metas Arquiteturais e Restrições da Arquitetura
### 3.1 Metas 
A seguir é possivel ver os objetivos do software. 
| Categoria | Metas            | 
| ------ | -------------------- | 
|Segurança e confiabilidade|A aplicação tem a responsabilidade de assegurar a proteção dos dados sensíveis dos usuários, garantindo sua confidencialidade. Qualquer falha ou erro deve ser prontamente comunicado ao usuário. Além disso, o sistema deve fornecer a funcionalidade de autenticação, onde cada usuário é identificado de forma exclusiva por meio de um endereço de e-mail e uma senha.|
| Portabilidade e suportabilidade  |  O usuário deve conseguir acessar o portal a partir de qualquer dispositivo com conexão a internet.  |
| Acessibilidade | O portal deve fornecer assistência aos usuários com necessidades especiais. |
| Responsividade | As páginas devem trocar a resolução de acordo com o tamanho da tela do usuário. | 

### 3.2 Restrições 

| Categoria | Restrições             | 
| ------ | -------------------- | 
|Conectvidade | O usuário tem que estar conectado à internet durante todo o período de utilização do portal e ter acesso a um navegador web.|
| Idioma  | O usuário deve poder escolher qual o idiomo que mais facilita a compreensão das funcionalidade do portal.  |

## 4. Visões 
### 4.1 Visão Logica 
### 4.1.1 Diagrama de Classe

<iframe height="600" width="700" src="https://unbarqdsw2023-1.github.io/2023.1_G4_ProjetoRiHappy/#/Modelagem/2.1.1.1.DiagramadeClasses"></iframe>

### 4.1.2 Diagrama de Pacote

<iframe height="600" width="700" src="https://unbarqdsw2023-1.github.io/2023.1_G4_ProjetoRiHappy/#/Modelagem/2.1.1.1.DiagramadeClasses"></iframe>

### 4.1.3 Diagrama de Estado 

<iframe height="600" width="700" src="https://unbarqdsw2023-1.github.io/2023.1_G4_ProjetoRiHappy/#/Modelagem/2.1.2.1DiagramaDeSequencia"></iframe>


### 4.2 Visão de Processo 

### 4.1.4 Diagrama de Sequência 

<iframe height="600" width="700" src="https://unbarqdsw2023-1.github.io/2023.1_G4_ProjetoRiHappy/#/Modelagem/2.1.2.2.DiagramadeEstados"></iframe>



## 5. Histórico de versões

| Versão | Descrição            | Autor             | Revisor           | Data          |
| ------ | -------------------- | ----------------- | ----------------- | ------------- |
| 1.0    | Abertura do artefato | Pedro Henrique Nogueira, Mateus Caltabiano, Matheus Soares, João Victor e Felipe Alef | Revisor da versão | 29/06/2023    |
| 1.1 | Finalidade   | Pedro Henrique Nogueira | - | 29/06/2023| 
| 1.2 | Escopo e Visão Geral| Pedro Henrique Nogueira | - | 30/06/2023| 
| 1.3 | Metas e Restrições | Pedro Henrique Nogueira | - | 01/07/2023|
|1.4| Visões | Pedro Henrique Nogueira | - | 01/07/2023 | 


## 6. Referências bibliográficas

> Adicionar as referências
