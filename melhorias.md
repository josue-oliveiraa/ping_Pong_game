# Melhorias Implementadas no Jogo Pong

Este documento descreve as melhorias implementadas no jogo Pong durante o desenvolvimento. O objetivo principal foi tornar o jogo mais funcional, interativo e completo.

---

## Funcionalidades Adicionadas

### 1. **Tecla para Pausar o Jogo**
- **Descrição:** Adicionada a funcionalidade de pausa do jogo ao pressionar a tecla `P`.
- **Comportamento:** 
  - Quando o jogador pressiona `P`, o jogo é pausado e uma mensagem informando que o jogo está pausado é exibida.
  - Pressionar `P` novamente retoma o jogo de onde ele foi pausado.

### 2. **Tecla para Sair do Jogo**
- **Descrição:** Adicionada a funcionalidade de encerrar o jogo ao pressionar a tecla `Q`.
- **Comportamento:**
  - Quando o jogador pressiona `Q`, o jogo é encerrado de forma limpa, liberando todos os recursos utilizados.
  - Esta funcionalidade foi adicionada para facilitar o encerramento rápido sem necessidade de interagir diretamente com a interface do sistema.

---

## Melhorias Visuais e de Interface

### 1. **Menu Principal**
- **Descrição:** O menu principal permite configurar a velocidade da bola e das raquetes antes do início do jogo.
- **Opções Disponíveis:**
  - Configurações de velocidade da bola: Lenta, Média, Rápida e Impossível.
  - Configurações de velocidade da raquete: Lenta, Normal e Rápida.
  - Opção para começar o jogo.

### 2. **Tela de Jogo**
- **Plano de Fundo:**
  - Uma imagem personalizada foi adicionada como plano de fundo, representando uma mesa de ping-pong.
- **Placar:**
  - O placar foi posicionado na parte superior da tela e mostra os pontos de ambos os jogadores em tempo real.

### 3. **Tela de Pausa**
- **Descrição:** Durante a pausa, uma mensagem "Jogo Pausado - Pressione P para Continuar" é exibida na tela.
- **Objetivo:** Informar o estado do jogo de forma clara ao jogador.

---

## Funcionalidades de Jogo

### 1. **Reinício da Bola**
- **Descrição:** A bola reinicia automaticamente no centro da tela sempre que um jogador marca um ponto.
- **Velocidade:** A direção da bola é aleatória, mas sua velocidade é mantida conforme configurada no menu.

### 2. **Condição de Vitória**
- **Descrição:** Um jogador vence quando alcança a pontuação máxima definida (10 pontos por padrão).
- **Tela de Vitória:** Uma mensagem indicando o vencedor é exibida e o jogo é encerrado automaticamente após alguns segundos.

---

## Uso de Teclas

| Tecla | Ação                          |
|-------|-------------------------------|
| `P`   | Pausar/Retomar o jogo         |
| `Q`   | Sair do jogo                  |
| `W`   | Mover a raquete do Jogador 1 para cima |
| `S`   | Mover a raquete do Jogador 1 para baixo |
| `↑`   | Mover a raquete do Jogador 2 para cima |
| `↓`   | Mover a raquete do Jogador 2 para baixo |

---

## Observações

- Certifique-se de que o arquivo `table.jpg` (imagem de fundo) esteja localizado no mesmo diretório que o código principal.
- O jogo está configurado para rodar em tela cheia. Caso haja problemas de resolução, ajustes podem ser feitos diretamente no código.
