# AssetGuard: Protótipo de Detecção de Anomalias por Clusterização

![Status do Projeto: Em Desenvolvimento](https://img.shields.io/badge/status-em%20desenvolvimento-yellowgreen)

## 1. Visão Geral do Projeto

Este repositório contém um protótipo acadêmico, desenvolvido para a disciplina de **Sistemas Computacionais**, que implementa um sistema de detecção de anomalias utilizando aprendizado de máquina não supervisionado. O projeto, intitulado **AssetGuard**, simula um cenário de monitoramento de ativos (veículos) em uma área restrita (aeroporto) e utiliza o algoritmo de clusterização K-Means para identificar comportamentos que desviam de um padrão pré-estabelecido de normalidade.

A solução foi arquitetada em Python com foco em modularidade e boas práticas de engenharia de software, seguindo um paradigma Orientado a Objetos.

## 2. O Conceito: Detecção Não Supervisionada

A principal abordagem deste protótipo é a **detecção de anomalias por meio de aprendizado não supervisionado**. Em vez de treinar um modelo com exemplos de "comportamento bom" e "comportamento ruim", nossa estratégia é mais robusta:

> Ensinamos ao sistema apenas o que é **normal**. Qualquer comportamento que fuja desse padrão de normalidade aprendido é, por definição, uma **anomalia**.

Essa metodologia é ideal para cenários de segurança, onde é impossível prever todas as formas de comportamento anômalo que podem ocorrer.

## 3. Arquitetura do Software

Para garantir clareza, manutenibilidade e escalabilidade, o projeto foi estruturado em três módulos distintos, aplicando o princípio da **Separação de Responsabilidades**:

-   #### `cenario.py` (O Construtor de Mundos)
    A classe `CenarioDeMonitoramento` é responsável por toda a **gestão dos dados**. Sua única função é criar o ambiente de simulação (gerando coordenadas normais e anômalas) e fornecer uma forma de visualizá-lo. Ela não possui conhecimento sobre a lógica de detecção.

-   #### `detector.py` (O Cérebro de IA)
    A classe `DetectorDeAnomalias` encapsula toda a **lógica de Machine Learning**. Ela recebe os dados, treina o modelo K-Means para aprender os padrões de normalidade e, por fim, implementa o método para verificar se um novo ponto de dado é uma anomalia. É um componente especialista e reutilizável.

-   #### `main.py` (O Maestro)
    Este script atua como o **ponto de entrada e orquestrador** da aplicação. Ele não contém lógica de negócio complexa; sua função é instanciar os objetos das outras classes e coordenar a sequência de ações:
    1.  Configura os parâmetros do cenário.
    2.  Instancia o `Cenario` e o `Detector`.
    3.  Comanda o `Cenario` para gerar os dados.
    4.  Comanda o `Detector` para treinar com esses dados.
    5.  Valida a solução, pedindo ao `Detector` que classifique pontos de teste.

## 4. Metodologia (Passo a Passo)

O pipeline de execução do protótipo segue uma sequência lógica de quatro etapas:

1.  **Simulação de Dados:** Utilizando a biblioteca `NumPy`, o sistema gera nuvens de pontos de dados em torno de centróides pré-definidos, representando a operação normal, e pontos dispersos para representar as anomalias. A reprodutibilidade é garantida pelo uso de uma semente (`np.random.seed`).

2.  **Treinamento do Modelo (K-Means):** O modelo `KMeans` da biblioteca `scikit-learn` é treinado **exclusivamente** com o conjunto de dados normais. O algoritmo identifica os centros geométricos (`centroides`) desses agrupamentos de dados.

3.  **Cálculo do Limiar de Anomalia:** Após o treinamento, o sistema calcula a distância de cada ponto de dado normal ao seu centróide mais próximo. O valor da **maior** dessas distâncias é selecionado e multiplicado por um fator de segurança (1.1) para criar um **limiar**. Este limiar define uma "fronteira matemática" em torno das zonas de operação normal.

4.  **Verificação e Classificação:** Uma função `verificar()` recebe um novo ponto de coordenadas. Ela calcula a distância deste ponto ao centróide mais próximo e a compara com o limiar pré-calculado. Se a distância for maior que o limiar, o ponto é classificado como uma anomalia.

## 5. Como Executar o Protótipo

### Pré-requisitos
- Python 3.8+
- Git

### Instalação
1.  Clone o repositório para sua máquina local:
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd [NOME_DA_PASTA_DO_PROJETO]
    ```
2.  Crie um arquivo `requirements.txt` com o seguinte conteúdo:
    ```txt
    numpy
    scikit-learn
    matplotlib
    ```
3.  Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

### Execução
Navegue até a pasta do projeto e execute o script principal:
```bash
python main.py
