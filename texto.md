# Texto de análise

## Descrição do Simulador

O nosso código de simulação funciona principalmente, com base em 2 elementos:

  1. Território, que contém uma densidade populacional e um PIB per capita
  2. Campus, que geram produção científica

A cada _step_, os agentes Território tentam criar um novo campus associado a si. Esse processo leva em conta os campi que já existem naquele território, a sua densidade populacional e o seu PIB per capita. A cada step, os Campi e os Territórios recalculam as suas propriedades, com base nos seus valores anteriores e um fator aleatório.

## Descrição da simulação e dos dados gerados

A construção do código levou em conta dados populacionais e de PIB per capita baseado em valores reais encontrados no brasil. Para a média de PIB per capita, nós usamos como base os dados em [https://pt.tradingeconomics.com/brazil/gdp-per-capita-ppp](https://pt.tradingeconomics.com/brazil/gdp-per-capita-ppp), que mostra que no final de 2020, o Brasil tinha um PIB per capita de aproximadamente 10.500 dólares. E para os dados de densidade populacional, usamos como fonte o site [https://mundoeducacao.uol.com.br/geografia/densidade-demografica-brasil.htm](https://mundoeducacao.uol.com.br/geografia/densidade-demografica-brasil.htm), onde foi encontrado tanto a densidade média, como também um valor de referencial mínimo e um máximo. 

Com o uso de dados reais para alimentar a lógica do código, esperávamos conseguir uma simulação mais fidedigna possível.

No final da simulação foi gerado um arquivo .csv, com uma lista das seguintes propriedades de todos os territórios:

  1. _id_ único
  2. _PIB per capita_
  3. Densidade populacional
  4. _Produção científica_ (definida aqui, como na atividade 3.5., como número programas de pós-graduação existentes)

## Análise dos dados gerados

Os gráficos da nossa simulação, comparados com os gráficos dos dados empíricos apresentados previamente, encontram algumas semelhanças que corroboram nossas suposições iniciais, mas também apresentam inconsistências decorrentes de problemas no desenvolvimento do código, tanto problemas de lógica, quanto de planejamento, quanto de impossibilidade de simular todas as inúmeras variáveis que afetam a construção de instituições e campi no mundo real.

Primeiramente analisando e comparando o gráfico de produção científica por estado. No mundo real nós verificamos que os maiores produtore científicos no Brasil são São Paulo e Rio de Janeiro, que também são os dois estados com maior densidade populacional do Brasil. Na nossa simulação encontramos que os lugares com maior produção científica tinham uma densidade populacional desproporcionalmente alta quando comparada com o resto dos territórios simulados.

Houveram, como achado na tarefa 3.5, casos divergentes onde um lugar alcançava grande número de produção com baixa densidade, e outros casos em que lugares com alta densidade geravam pouca ou nenhuma produção científica.

Analisando o gráfico de produção científica por PIB per capita observamos que a distribuição de produção científica é fracamente correlata com o PIB per capita, de forma semelhante ao achado com os dados empíricos. Existem vários territórios com produção científica zero, o que não condiz com os dados empíricos, que são próximos de zero.

## Discussão de problemas da simulação

Como comentado antes, diversos fatores contribuiram para uma diferença entre os gráficos reais e os gráficos da simulação em alguns aspectos. A maioria desses fatores podem ser divididos em algumas categorias:

  1. Problema de implementação: Por dificuldade de implementar alguma lógica ou cálculo, como por exemplo geração dos dados de pib per capita e densidade populacional. Esse tipo de problema fez com que buscássemos diferentes estratégias para conseguir representar uma medida, por vezes abrindo mão de precisão por facilidade de implementação e de manipulação de dados.

  2. Problema de representação de variáveis: Nos dados empíricos existe um número grande de variáveis não contadas que afetam um determinado acontecimento. No caso de construção de instituições e campi, podemos listar de forma não exaustiva o IDH local, escolaridade média, iniciativas públicas, investimento interno e externo, incentivo à profissionalização, terreno, pirâmide etária local, entre tantas outras. Para simplificar a simulação, decidimos simplificar as várias variáveis em somente duas: PIB per capita e densidade populacional. Dessa forma podemos simular a quantidade de dinheiro disponível tanto para investimentos e incentivos populacional desproporcionalmente alta quando comparada com o resto dos territórios simuladoslicos, quanto em dinheiro à disposição do cidadão comum para poder buscar ensino superior. A escolha dessas propriedades também foi fortemente influênciada pela dificuldade na tarefa 3.5 de achar bases de dados contendo outros relevantes para a questão foco, em um formato que pudesse ser cruzado com a base de produção científica por território.

  3. Problema de planejamento: Dificuldades de adquirir algum conhecimento necessário para a construção da simulação, seja esse conhecimento algum dado empírico, seja a forma de implementar algo em específico na linguagem. De forma geral esse problema só resultou em menos precisão nos resultados e maior demora para implementação.

## Reflexões pessoais

Lucas Vinicius:
Em retrospectiva, as tarefas da disciplina me deram uma base para entender como fazer, para que serve e qual a importância da busca de dados e de artigos, tanto para conhecimento pessoal quanto utilização dos dados para propósitos de criar novos estudos e simulações. Com a matéria eu aprendi a selecionar que tipo de dado eu quero, de acordo com determinada variável como local, assunto, revista de publicação, entre outros. Isso permite com que eu consiga ir atrás de dados que sejam mais relevantes para quaisquer trabalho que eu esteja desenvolvendo, e faz com que quaisquer conclusões que eu extraia desse estudo, seja o mais realista e completa possível.

Rafael Golçalves: 

Leonardo Rodrigues:
