XXV Encontro Brasileiro de Psicologia e Medicina Comportamental, 2016, Foz do Iguaçu, Brasil.

# Análise do comportamento por meio de rastreamento de movimentos oculares: uma nota técnica.

Carlos Rafael Fernandes Picanço & François Jacques Tonneau.   
Universidade Federal do Pará, Belém, PA, Brasil.

**Resumo**

O rastreamento de movimentos oculares tem sido reconhecido como um método que permite estudos analítico comportamentais de novos e antigos problemas no campo de controle de estímulos, mas tem sido pouco utilizado por questões de acessibilidade. O objetivo deste trabalho foi 1) montar um laboratório acessível para a condução de tais estudos e 2) demonstrar o laboratório em funcionamento por meio de um estudo sobre discriminação simples (com delineamento ABA). O laboratório (custo total ~R$3350) dependia da plataforma opensource Pupil e incluia um rastreador (Pupil Dev), um computador (i3, 2GB-DDR3, Linux/OS), um botão de respostas, luzes dimerizadas e um descanço para o queixo. Dez universitários adultos com visão normal (4M-6F) recebiam a instrução: "A sua tarefa é ganhar pontos apertando o botão". Cada condição (A, B e A) durava 5 min e iniciava com a apresentação de dois estímulos igualmente espaçados em relação ao centro de uma tela, sendo um quadrado à esquerda (alternando sua cor entre vermelho e azul) e um círculo à direita (alternando sua cor entre verde e ciano). Controle por aspectos temporais eram evitados com a alternância de cores aleatoriamente, com duração média de 15 s (mínimo 11, máximo 20). Na condição A, vermelho e azul estavam associados a CRF, isto é, discriminações simples entre essas cores não eram possíveis. Na condição B, vermelho estava associado a CRF e azul à extinção, permitindo a ocorrência de discriminações simples. As cores verde e ciano não possuiam consequências programadas (distratores). Assim, induzia-se a alternância de fixações do olhar entre os estímulos. Os movimentos oculares foram categorizados entre esquerda e direita por meio do algoritmo DBSCAN. Foram graficados perfis temporais com a taxa de movimentos oculares em cada categoria e a taxa de respostas ao botão em cada categoria que, inspecionados visualmente, permitiam avaliar a ocorrência ou não de mudanças correlatas entre movimentos oculares e respostas ao botão.

*Palavras-chave*: rastreamento de movimentos oculares; discriminações simples; acessibilidade.

## Resumo Expandido

Carlos Rafael Fernandes Picanço

Este trabalho não seria possível sem o apoio da CAPES (Bolsa de doutorado ao primeiro autor).

Ao longo desta apresentação eu apresentarei um método automático de análise de dados comportamentais baseado em segmentação temporal e em um algoritmo (DBSCAN) de categorização amplamente reconhecido no campo da 'Descoberta de Conhecimento e Mineração de Dados'. Argumentarei que o uso da plataforma PUPIL de rastreamento de visão conjuntamente com algoritmos to tipo permite abandonar (ou ao menos reduzir o uso de) um despendioso e entediante método; a saber, a categorização por inspeção visual, quadro-a-quadro, dos vídeos produzidos por rastreadores de visão. Argumentarei, também, que a plataforma PUPIL é a mais acessível da atualidade a pesquisadores fora das ciências da computação interessados em visão computacional. Friso, e antecipo aos senhores e senhoras, que tal argumento não deve ser confundido com a mera divulgação de um produto, ao contrário, deve ser entendido como um esforço no sentido de promover o movimento de código aberto e ciência aberta em nosso campo. Em seguida, por meio de um micro-experimento, demonstrarei um sistema de rastreamento de visão em funcionamento por meio das referidas tecnologias. Por fim, deixarei a previsão de que o Aprendizado de Máquina, embora atualmente não tão acessível quanto o método proposto, irá torná-lo obsoleto e pode vir a ser uma solução última e definitiva para trabalhos futuros de categorização de estímulos e respostas em diferentes meios.

## Análise do comportamento e Rastreamento de Visão: a geração *Video Frame Coder* ®.

A análise comportamental no campo de rastreamento de visão frequentemente demanda como dado bruto movimentos oculares categorizados de acordo com os estímulos, respostas e condições experimentais de interesse. Uma estratégia comum (ver [Dube et al, 2010][dube]; [Huziwara, Souza & Tomanari, 2016][huziwara]; Mescouto, 2011; [Perez, Endemann, Pessôa & Tomanari, 2015][perez])para produzi-los tem sido a categorização por meio de inspeção visual *post facto* dos vídeos produzidos por rastreadores. Tal trabalho tem sido feito com o auxílio de um programa de computador chamado *Video Frame Coder* ® , que, segundo os autores, "torna a tarefa viável".

Alguns problemas merecem ser destacados sobre esse método. Primeiro, mesmo com o auxílio daquele programa de computador, trata-se de um método que consome muito tempo; um vídeo com 50.000 quadros implica ~2 h de trabalho repetitivo. Segundo, ele é especialmente suscetível ao erro humano; um aspecto intrínsico à inspeção visual. Terceiro, é plausível sugerir que é um método entediante e não provê reforçadores intrínsicos ao exercício científico. Quarto, o método depende de um *software* fechado; os cientistas interessados em um maior escrutínio do método não teriam acesso aos meios para tanto. Quinto, a categorização é feita por meio de critérios difíceis de serem operacionalizados; um maior rigor poderia ser alcançado por meio de concordância entre os categorizadores, mas isso implica um maior custo. Por fim, sugere-se que o contexto aplicado demanda uma agilidade não contemplada por esse método.

Como sofisticar esse processo tornando-o mais acessível ao cientista de tradição analítico comportamental? 

## Análise do comportamento e Rastreamento de Visão: a geração PUPIL.

Uma alternativa é automatizar o procedimento de categorização por meio de soluções open-source ou soluções livres. É importante notar que, para fins de pesquisa científica, acessibilidade não se alinha necessariamente com extremo baixo custo ou consumo de massa. O mais importante são a natureza (se é um sistema aberto ou fechado), a documentação (ser farta ou escasssa) e as funcionalidades do sistema (isto é, se permite ou fornece a automação de interesse).

Considerando esses três pontos, a plataforma PUPIL (https://pupil-labs.com; uma iniciativa da *Pupil Labs*, uma *startup* alemã fundada por M. Kassner, W. Patera e A. Bulling; ver [Kassner, Patera & Bulling, 2014][pupil]) apresenta-se como uma alternativa do tipo promissora. Primeiro, porque baseia-se em *softwares* 100% *open-source*. Segundo, possui farta documentação tanto a cientistas de dentro quanto a cientistas de fora das ciências da computação. E terceiro, fornece e permite a automação de diferentes tarefas.

Considerando as funcionalidades dessa plataforma, destaco agora três aspectos que foram especialmente úteis para o sistema até então montado.

### PUPIL: Transformações homográficas de superfícies de interesse

A plataforma permite a detectação automática de superfícies (áreas de interesse) por meio de marcadores fiduciários. A detecção e a trasformação de perspetiva das superfícies é feita automaticamente. Os dados, então, podem ser exportados para análises subsequentes.

### PUPIL: Plugins de Tempo de Execução

A plataforma é facilmente adaptável por meio da linguagem Python. O experimento que apresentarei envolvia distratores e como os marcadores fiduciários também poderiam funcionar como distratores, optei por evitar o seu uso. Assim, adaptei um plugin da plataforma para utilizar a tela de apresentação dos estímulos, ao invés dos marcadores, como referência para as superfícies.

### PUPIL: Modelo 3D dos olhos

A plataforma possui um algoritmo de detecção ocular baseado na construção de um modelo 3D dos olhos do participante. Essa construção tanto permite grande estabilidade na acurácia durante longos períodos quanto permite uma calibragem mais ágil do sistema (que dura aproximadamente 30 s). O experimento que estarei apresentando exigia no mínimo 15 min de estabilidade. Infelizmente, essa funcionalidade não estava disponível na época em que os dados que apresentarei foram coletados. Mesmo assim, o fato de a plataforma fornecer tal funcionalidade merece destaque.

### PUPIL: um atalho para a aplicação?

A plataforma permite pronta adaptação de técnicas e métodos análicos desenvolvidos no laboratório ao contexto aplicado. Essa portabilidade se reduz com sistemas exclusivamente estacionários.

### PUPIL: notas avulsas.

Sistemas comerciais (**CITAR**) e outros sistemas abertos (**CITAR**) não possuem comparável acessibilidade, seja porque não fornecem funcionalidades, seja porque não forcenem um ambiente de código aberto tanto no contexto de coleta quanto no contexto de análise de dados, pós coleta. Argumenta-se, portanto, que a plataforma PUPIL é a mais acessível da atualidade para pesquisas analítico comportamentais em conformidade com padrões de ciência aberta.

- possui uma comunidade ativa e está em pleno e estável desenvolvimento a mais de 4 anos;
- tem tido notável impacto no [campo acadêmico][pupil-citations] com mais de 60 citações nos últimos 3 anos;
- possui farta documentação;
   - para cientistas de dentro e de fora das ciências da computação;
   - com base em minha própria experiência de aluno familiarizado com computadores:
      - estimo 3 meses de estudo para o operador iniciante antes da primeira coleta monocular (Dado bruto: pontos);
      - estimo 6 meses de estudo para o operador iniciante antes da primeira coleta binocular (Dado bruto: vetores);
- permite investigações no campo do rastreamento de visão e visão egocêntrica;
- permite experimentos estacionários e em movimento;
- possui qualidade de dados aceitáveis para análises comportamentais;
   - acurácia de 0.5 a 1.0 grau do ângulo de visão;
   - precisão 0.08 grau;
   - granularidade 30 hz a 120 hz;
- possui um preço rasoável para uso não comercial em contexto acadêmico;
   - você pode montar um Pupil Dev por $300 + tempo de construção;
   - ou comprar um Pupil Pro (Monocular) €1050;

## DBSCAN: uma rápida introdução.

Após exportar os dados por meio da plataforma PUPIL, as categorias eram automaticamente identificadas por meio do algoritmo DBSCAN, acrônimo para "categorização espacial baseada em densidade para aplicações com ruído". Este algoritmo demanda apenas duas informações para funcionar. Um conjunto de dados e um critério de densidade. Lembre que densidade é igual a massa sobre o volume. Para os objetivos dessa apresentação identificarei massa como um número de pontos em um plano cartesiano, isto é, a posição dos olhos na tela de apresentação dos estímulos. Identificarei o volume como uma distância euclidiana nesse espaço, que aqui chamaremos de vizinhança N de uma certa posição dos olhos. Uma descrição detalhada da lógica interna do algoritmo está fora do escopo desse trabalho. Para o momento, basta saber que ele é capaz de identificar categorias com diferentes formas e que não é possível categorizar dados sobrepostos espacialmente por meio de um mesmo critério de densidade.

## Um micro-experimento comportamental

Este estudo foi aprovado pelo comitê de ética (CAAE: 35142814.0.0000.5172).

### Objetivo

Na medida em que um responder discriminativo ocorresse, se esperava que o comportamento ocular tendesse para o lado esquerdo, local no qual os estímulos relevantes eram apresentados, ao invés da direita, aonde estímulos distratores eram apresentados. Diferentemente, se o responder discriminativo não ocorresse, tal tendência de olhares à esquerda não deveria ocorrer.

O objetivo, dessa forma, era identificar correlações entre movimentos oculares e o responder discriminativo em uma tarefa de discriminação simples sucessiva com estímulos distratores.

### Método
#### Participantes

6 mulheres e 4 homens, com idade entre 18 e 27 anos, participaram do estudo, todos com visão normal, universitários de diferentes cursos exceto o de psicologia. Todos eles assinaram um termo de consentimento livre e esclarecido autorizando a participação no estudo.

#### Equipamento

O estudo era conduzido em uma sala com iluminação não controlada entre 300 e 640 LUX (lumens/m2). Os movimentos oculares eram capturados por meio do rastreador ocular Pupil Dev, que possui uma câmera frontal e uma câmera ocular, ambas com 30hz. Uma tela de apresentação era projetada em uma das paredes da sala e um descanço para o queixo planejado ergonomicamente para se adequar a postura natural dos participantes assegurava que a tela sempre estava no campo de gravação da câmera frontal. O projetor e um botão de respostas ambidestro estavam conectados a um computador executando o programa *[Stimulus Control][stimulus-control]*. O programa registra as respostas ao botão e controlava a apresentação de estímulos de maneira sincronizada (por meio de *sockets* TCP/IP) com o programa Pupil Capture, que por sua vez registrava os movimentos oculares e controlava a calibragem do rastreador. Posteriormente a coleta, o programa *Pupil Player* detectava a tela de apresentação dos estímulos e permitia exportar os dados para categorização por meio do algoritmo DBSCAN ([Ester et al, 1996][ester]), tal como implementado por [Pedregosa et al, 2011][scikit-learn]. A implementação da categorização foi escrita na linguagem Python (**O código está em outro repositório, mas será incluido posteriormente neste repositório**).

#### Procedimento e Análise de dados

Com as categorias de movimentos oculares em mãos, a taxa de movimentos oculares era calculada em cada um dos estímulos apresentados. Isso só era possível porque todos os eventos de interesse (isto é, movimentos oculares, respostas, início dos estímulos, etc.) recebiam um tempo extraido de um mesmo fluxo de tempo monotônico. Nós chamamos isso de segmentação temporal, ilustrada por meio dos cubos e eventos na Figura 1. A taxa de respostas ao botão durante o estímulo vermelho e o estímulo azul também eram calculadas.

Um delineamento ABA era apresentado. Na condição A, vermelho e azul estavam associados a CRF. Na condição B, apenas vermelho estava associado a CRF, o que permitia a ocorrência de discriminações.

Vermelho e azul sempre eram apresentados à esquerda; verde e ciano sempre à direita (distratores). Controle por aspectos temporais eram evitados com a alternância de cores aleatoriamente. Note, embora aleatoriamente, as cores se alternavam sempre sucessivamente, nunca simultaneamente, de acordo com a ordem temporal apresentada nas Figuras 1,2, 3 e 4.

#### Resultados

Um responder discriminativo foi observado no desempenho de sete dos dez participantes deste estudo. Dentre desempenhos discriminativos, três deles envolveram movimentos oculares de acordo com a predição, isto é, foi observada uma tendência de olhares à esquerda na condição B em contraste com os olhares à direita e à esquerda na condição A. Embora apenas trẽs participantes tenham demonstrado um desempenho de acordo com a previsão, foram observadas mudanças no padrão de movimentos oculares durante a condição B com outros dois participantes. Ou seja, foram observadas mudanças no padrão de movimentos oculares entre as condições A e B com cinco daqueles sete participantes.

Mudanças no padrão de movimentos oculares entre as condições A e B não foram observadas no desempenho dos três participantes que não responderam discriminativamente.

#### Etapas seguintes

Aplicar o método a uma tarefa com nove estímulos apresentados simultaneamente e explorar métodos computacionais com o objetivo de automatizar a inspeção visual dos dados.

- Otimização não assistida de densidade do DBSCAN.

## Análise do comportamento e Rastreamento de Visão: a geração Aprendizado de Máquina?

A detecção automática e em tempo real (ver [Arcas, 2016][arcas]) de eventos por meio de máquinas treinadas para isso tornará o método apresentado obsoleto.

## Nota sobre rastreadores de visão e sua dependência de *softwares* 

### Hardware

Atualmente, [diferentes empresas][cogain] vendem rastreadores que atendem a diferentes públicos alvo, desde aqueles de baixo custo para desenvolvedores de jogos (e.g., https://theeyetribe.com/), até aqueles com altas especificações para pesquisas científicas onde o tempo é uma variável crítica (e.g., [Du Plessis, 2016][du-plessis]). Um saudoso e querido professor (José Carlos Martins Fontes, o Zé Carlos) uma vez me disse: "Se você tem o dinheiro, compre. Se não, construa." Bem, eu frequentemente não tenho o dinheiro.

Para a minha felicidade, entranto, hoje se você sabe o básico sobre soldagem SMD, eletrônica e possui o tempo necessário para importar peças do exterior, você pode optar por montar seu próprio rastreador. No meu caso, todo o processo de pesquisa preliminar, importação e montagem inicial durou três meses. De fato, na atualidade, montar ou comprar um *hardware* é o menor dos problemas no campo das pesquisas científicas sobre rastreamento de visão.

### Software

O maior custo não está sobre a manufatura do *hardware*, mas no desenvolvimento do *software*. A saber, o campo de rastreamento de visão demanda frequentemente três tipos de *softwares*:
   
   - dois de coleta
      - um para o rastreamento ocular propriamente dito;
      - outro para o controle da apresentação de estímulos;
   - e um de análise
      - mas note que novas análises frequentemente demandam novos *softwares*;

E aqui encontramos um dilema ao refletir sobre a sabedoria daquele querido professor. Primeiro, comprar ou usar uma caixa-preta comercial não é uma alternativa cientificamente aceitável. É simplesmente inaceitável, para um cientista como eu, não ter acesso a implementação e documentação das soluções que permitem o rastreamento de visão (Este ponto é especialmente verdadeiro para um cientista da computação ao se deparar com algoritmos patenteados). É igualmente inaceitável, para um cientista como eu, não ter acesso aos detalhes do tratamento e nem liberdade para inovar na análise de dados. Enfim, é especialmente inaceitável ter de mudar a pesquisa ao invés de adaptar o *software* com finalidade de apresentar os estímulos.

Segundo, construir pode não parecer uma opção das mais viáveis para os cientistas do comportamento de tradição estritamente psicológica (a psicologia institucionalizada tradicionalmente tem permanecido distante de disciplinas como a matemática, estatística e afins, mesmo que tal distanciamento não seja verdadeiro para a psicologia como ciência; ver [Gundlach, 2006][gundlach]), pois o desenvolvimento de programas de computador é um serviço de alta complexidade. Mas o que nos resta se não é sábio construir e nem mesmo faz sentido para fins científicos comprar?

### Solução 1 - Construa!

Mas e se a questão for um falso dilema? Um primeira solução seria: pode ser sábio construir, como aquele querido professor já havia sugerido. Por exemplo, um *software* livre para experimentos comportamentais pode contribuir como um nicho de diversificação da análise do comportamento (Reimer, 2016). É importante notar que a engenharia de *softwares* comportamentais é uma área recente no escopo das ciências da computação ([Lenberg, 2015][lenberg]), ainda que possa ser vista com saudosismo por alguns analistas do comportamento ([Stephens, 2007][stephens]). É notável, também, que interfaces entre ciências da computação e análise do comportamento já tenham sido feitas no campo da educação técnica ([Harrison, 2005][harrison]).

### Solução 2 - Colabore!

Mas há uma outra alternativa: colaborar. Os cientistas da computação tem desenvolvido plataformas de rastreamento de visão *open-source* acessíveis. A solução para nós é usá-las; e eu devo inclusive sugerir, apoiá-las e sofisticá-las. Após comprar ou construir o seu lindo rastreador, você pesquisador deverá assegurar que pode usá-lo de maneira automatizada, transparente e inovadora. Seja durante a coleta de dados, seja durante a análise de dados. Isto simplesmente não seria possível sem a iniciativa e apoio de comunidades *open-source*. Por que a análise do comportamento não tem promovido iniciativas *open-source* e *open-science*?

## Referências

Arcas, B. A. (2016, May). How computers are learning to be creative. Filmed presented at the TED@BCG Paris, Paris. Retrieved from https://www.ted.com/talks/blaise_aguera_y_arcas_how_computers_are_learning_to_be_creative?language=en

Dube, W. V., Dickson, C. A., Balsamo, L. M., O’Donnell, K. L., Tomanari, G. Y., Farren, K. M., … McIlvane, W. J. (2010). Observing Behavior and Atypically Restricted Stimulus Control. *Journal of the Experimental Analysis of Behavior*, *94*(3), 297–313. http://doi.org/10.1901/jeab.2010.94-297

Ester, M., Kriegel, H.-P., Sander, J., & Xu, X. (1996). A density-based algorithm for discovering clusters in large spatial databases with noise. *In 2nd International Conference on Knowledge Discovery and Data Mining* (pp. 226–231). Menlo Park, CA: AAAI Press. Retrieved from https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf

Kassner, M., Patera, W., & Bulling, A. (2014). Pupil: an open source platform for pervasive eye tracking and mobile gaze-based interaction. In Proceedings of the 2014 ACM International Joint Conference on Pervasive and Ubiquitous Computing: Adjunct Publication (pp. 1151–1160). Seattle, United States: ACM Press. http://doi.org/10.1145/2638728.2641695

Lenberg, P., Feldt, R., & Wallgren, L. G. (2015). Behavioral Software Engineering: a Definiton and Systematic Literature Review. *Journal of Systems and Software*, *107*, 15 – 37. http://doi.org/doi:10.1016/j.jss.2015.04.084

Mescouto, W. de A. (2011). Efeitos de contingências e instruções sobre respostas de escolha e de movimento dos olhos durante o estabelecimento de discriminações simples simultâneas (Dissertação de mestrado). Universidade Federal do Pará, Belém, PA, Brasil.

Harrison, W. (2005). Skinner Wasn’t a Software Engineer. *IEEE Software*, *22*(3), 5–7. http://doi.org/10.1109/MS.2005.76

Huziwara, E. M., de Souza, D. das G., & Tomanari, G. Y. (2016). Patterns of eye movement in matching-to-sample tasks. *Psicologia: Reflexão E Crítica*, *29*(1). http://doi.org/10.1186/s41155-016-0010-3

Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., … Duchesnay, E. (2011). Scikit-learn: Machine Learning in Python. *Journal of Machine Learning Research*, *12*, 2825–2830.

Perez, W. F., Endemann, P., Pessôa, C. V. B. B., & Tomanari, G. Y. (2015). Assessing Stimulus Control in a Discrimination Task with Compound Stimuli: Evaluating Testing Procedures and Tracking Eye Fixations. *The Psychological Record*, *65*(1), 83–88. http://doi.org/10.1007/s40732-014-0092-1

Du Plessis, J. P., & Blignaut, P. (2016). Utilising the GPU to develop a high-speed, low-cost eye tracker. Journal of Eye Movement Research, 9(4), 1:11. http://doi.org/10.16910/9.4.6

Reimer, D. (2016). The Future of Behavior Analysis: Why we need to Diversify, Part I. Retrieved from http://www.baquarterly.com/2016/01/the-future-of-behavior-analysis-why-we-need-to-diversify-part-i/

Stephens, K. (2007, December 30). Behavioral Software Engineering [Blog]. Retrieved from http://bbs-software.blogspot.com.br/2007/12/behavioral-software-engineering.html

[dube]:http://doi.org/10.1901/jeab.2010.94-297
[perez]:http://doi.org/10.1007/s40732-014-0092-1
[huziwara]: http://doi.org/10.1186/s41155-016-0010-3
[arcas]:https://www.ted.com/talks/blaise_aguera_y_arcas_how_computers_are_learning_to_be_creative?language=en
[pupil]:http://doi.org/10.1145/2638728.2641695
[pupil-citations]:https://docs.google.com/spreadsheets/d/1ZD6HDbjzrtRNB4VB0b7GFMaXVGKZYeI0zBOBEEPwvBI/edit?ts=576a3b27#gid=0
[cogain]:http://wiki.cogain.org/index.php/Eye_Trackers
[ester]:https://www.aaai.org/Papers/KDD/1996/KDD96-037.pdf
[du-plessis]:http://doi.org/10.16910/9.4.6
[scikit-learn]:http://dl.acm.org/citation.cfm?id=1953048.2078195
[harrison]:http://doi.org/10.1109/MS.2005.76
[gundlach]:https://www.researchgate.net/publication/26333272_Psychology_as_science_and_as_discipline_the_case_of_Germany
[lenberg]:http://doi.org/doi:10.1016/j.jss.2015.04.084
[reimer]:http://www.baquarterly.com/2016/01/the-future-of-behavior-analysis-why-we-need-to-diversify-part-i/
[stephens]:http://bbs-software.blogspot.com.br/2007/12/behavioral-software-engineering.html
[stimulus-control]:https://github.com/cpicanco/stimulus_control