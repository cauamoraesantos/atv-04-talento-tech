# **Gerenciador de Instrumentos Musicais** 🎸🎻  

Este projeto é um aplicativo simples desenvolvido em Python com interface gráfica utilizando a biblioteca `tkinter`. Ele permite o cadastro e a listagem de instrumentos musicais (guitarras e violões), aplicando conceitos de orientação a objetos e controle de versão com Git.

---

## **Objetivos do Projeto**  
- Desenvolver um sistema para gerenciar instrumentos musicais, permitindo o cadastro de guitarras e violões com informações detalhadas.
- Explorar o uso de Git para controle de versão, organizando o projeto de forma modular e documentada.
- Criar uma interface gráfica simples que permita a interação com o sistema.

---

## **Funcionalidades**  

- **Cadastro de instrumentos:**  
  - Guitarras: Marca, preço, modelo e tipo de captador.  
  - Violões: Marca, preço e modelo.  

- **Listagem de instrumentos:**  
  Exibe todos os instrumentos cadastrados.  

- **Remoção de instrumentos:**  
  Permite excluir instrumentos da lista.  

---

## **Estrutura do Projeto**  

O projeto está organizado nos seguintes arquivos:

- **`instrumento.py`**: Classe base `Instrumento` com atributos `marca` e `preco`.
- **`guitarra.py`**: Classe `Guitarra`, herdando de `Instrumento`, com atributos adicionais `modelo` e `captador`.
- **`violao.py`**: Classe `Violao`, herdando de `Instrumento`, com atributo adicional `modelo`.
- **`controller.py`**: Classe `InstrumentoController` para gerenciar as operações CRUD.
- **`app.py`**: Arquivo principal com a interface gráfica criada usando `tkinter`.

---

## **Como Executar o Projeto**  

### **Pré-requisitos**  
- Python 3.x instalado.

### **Passos para execução:**

1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/gerenciador-instrumentos.git
   cd src
   ```

2. Execute o aplicativo:
   ```bash
   python app.py
   ```

3. A interface gráfica será aberta, permitindo o cadastro e a listagem dos instrumentos.

---

## **Uso de Git no Projeto**  

- **Branches:** Cada funcionalidade foi desenvolvida em uma branch separada para manter o projeto modular e organizado.  
- **Commits frequentes:** Foram realizados commits frequentes com mensagens claras, facilitando o rastreamento das mudanças.  
- **Merge:** Após finalizar cada funcionalidade, foi realizado o merge para a branch principal (`main`), garantindo a integridade do projeto.

