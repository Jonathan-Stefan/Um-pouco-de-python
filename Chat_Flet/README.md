

```markdown
# Chat em Tempo Real com Flet

Este é um projeto de chat em tempo real desenvolvido utilizando a biblioteca Flet, que permite a criação de interfaces gráficas em Python. O chat é executado diretamente no navegador e possibilita a troca de mensagens entre diferentes usuários conectados à mesma página.

## Funcionalidades

- **Entrada no chat**: Cada usuário insere seu nome antes de participar da conversa.
- **Mensagens em tempo real**: As mensagens são transmitidas em tempo real para todos os usuários conectados.
- **Notificação de entrada**: Quando um novo usuário entra no chat, todos os participantes são notificados.
- **Interface amigável**: Interface simples com campos para digitação do nome e da mensagem.

## Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Biblioteca Flet

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/Jonathan-Stefan/Um-pouco-de-python/tree/main/Chat_Flet
   cd chat-flet
   ```

2. Instale a biblioteca Flet:

   ```bash
   pip install flet
   ```

### Execução

Para iniciar o chat, execute o seguinte comando:

```bash
python main.py
```

O chat será iniciado em um servidor local e acessível no navegador na URL `http://localhost:8000`.

## Estrutura do Código

- **main.py**: Arquivo principal que contém toda a lógica do chat, incluindo o envio e recebimento de mensagens e a configuração da interface.
- **Flet**: Usado para gerenciar a interface do usuário, incluindo o layout do chat, os campos de entrada e botões.

## Funcionamento

- Quando o usuário inicia o chat, ele deve inserir o nome para poder entrar na conversa.
- As mensagens enviadas por um usuário são transmitidas para todos os outros através de um túnel de comunicação `pubsub`.
- Cada mensagem aparece no formato: `<nome do usuário>: <mensagem>`.
- Quando um novo usuário entra, uma mensagem de notificação é exibida para os outros participantes.

## Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias e correções!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
```
