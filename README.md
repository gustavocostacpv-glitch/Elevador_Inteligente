 # Elevador_Inteligente
Simulador interativo de elevador desenvolvido para um desafio de programação, comparando algoritmos de atendimento de chamadas."

Tecnologias e Conceitos Utilizados
* **IDLE (Python 3.14)** (Lógica do algoritmo e execução via terminal)
* **Estrutura de Dados** (Listas e Tuplas para gerenciamento da fila de chamadas)
* **Lógica de Busca Otimizada** (Uso de funções matemáticas de distância absoluta)

---

## 📑 Relatório Técnico (Respostas do Desafio)

### 1. Criar um algoritmo
O algoritmo foi totalmente desenvolvido em Python e está estruturado no arquivo `elevador.py`. Ele simula o comportamento físico do elevador, contabilizando o tempo gasto para abrir/fechar as portas (5 segundos por parada) e o tempo de deslocamento entre andares (3 segundos por andar).

### 2. Justificativa da Estratégia Escolhida
A estratégia selecionada como principal para o projeto foi a de **"Atender o Mais Próximo Primeiro"** (baseada no conceito do algoritmo *SSTF - Shortest Seek Time First*).

* **Justificativa:** Em sistemas de elevadores, o atendimento por ordem de chegada puro (*FCFS*) costuma gerar viagens longas com a cabine ociosa (vazia), cruzando vários andares apenas para buscar um único usuário. Ao priorizar a chamada mais próxima da posição atual do elevador, reduzimos o tempo de deslocamento sem passageiros, otimizamos o fluxo de atendimento e evitamos o desgaste mecânico desnecessário do motor, além de economizar energia elétrica no prédio da escola.

### 3. Comparação com Outra Estratégia
Para validar a escolha, o desempenho do algoritmo otimizado foi comparado diretamente com a **Estratégia A (Ordem de Chegada)**, utilizando a mesma lista de chamadas fornecida pelo desafio: `[(0,4), (2,1), (3,0), (4,2)]`.

* **Estratégia A: Ordem de Chegada (FCFS)**
  * **Ordem de Atendimento:** (0,4) → (2,1) → (3,0) → (4,2)
  * **Deslocamento Total:** 18 andares percorridos
  * **Tempo Total Gasto:** 94 segundos

* **Estratégia Escolhida: Mais Próximo Primeiro (Otimizado)**
  * **Ordem de Atendimento:** (0,4) → (4,2) → (2,1) → (3,0)
  * **Deslocamento Total:** 12 andares percorridos
  * **Tempo Total Gasto:** 76 segundos

### 4. Conclusão e Resultados (Qual teve melhor resultado)
A estratégia de **Atender o Mais Próximo Primeiro** apresentou o melhor resultado prático e matemático.

O algoritmo em Python reduziu o deslocamento do elevador em **6 andares** (uma economia de **33%** no trajeto) e diminuiu o tempo total de operação em **18 segundos** (caindo de 94s para 76s). Esses dados comprovam que a lógica de proximidade é muito superior para o gerenciamento de chamadas, garantindo menos tempo de espera para os alunos/professores e maior eficiência para a escola.

---

##  Como Executar o Projeto:

1. Baixe o arquivo `elevador.py` ou utilize o código deste repositório.
2. Certifique-se de ter o Python instalado em sua máquina , a ferramenta utilizada foi: IDLE (Python 3.14).
3. Abra o terminal ou prompt de comando na pasta do arquivo e execute o arquivo utilizado:
4. Execução:
   - Abra o ficheiro `elevador.py` no IDLE.
   - Pressione `F5` para rodar o codigo executado.
