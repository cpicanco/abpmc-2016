Resumo expandido referente ao trabalho "Análise do comportamento por meio de rastreamento de movimentos oculares: uma nota técnica". XXV Encontro Brasileiro de Psicologia e Medicina Comportamental, 2016, Foz do Iguaçu, Brasil.

Carlos Rafael Fernandes Picanço.
Universidade Federal do Pará, Belém, PA, Brasil.

Este trabalho não seria possível sem o apoio da CAPES (Bolsa de doutorado ao autor).

Apresenta-se um método automático de análise **post facto** de dados comportamentais baseado am ambos segmentação temporal e categorização de movimentos oculares por meio de um algoritmo (DBSCAN) amplamente reconhecido no campo da 'Descoberta de Conhecimento e Mineração de Dados'. Argumenta-se que o uso da plataforma PUPIL de rastreamento de visão conjuntamente com algoritmos to tipo permite abandonar (ou ao menos reduzir o uso de) um despendioso e entediante método; a saber, a categorização por inspeção visual, quadro-a-quadro, dos vídeos produzidos por rastreadores de visão. Argumenta-se, também, que a plataforma PUPIL é a mais acessível da atualidade a pesquisadores fora das ciências da computação interessados em visão computacional. Frisa-se, antecipadamente, que tal argumento não deve ser confundido com a mera divulgação de um produto, ao contrário, deve ser entendido como um esforço no sentido de promover o movimento de código aberto e ciência aberta no campo Analítico Comportamental. Em seguida, por meio de um micro-experimento, demonstra-se o sistema de rastreamento de visão em funcionamento por meio das referidas tecnologias. Limites do método são discutidos.

## Análise do comportamento e Rastreamento de Visão: a geração *Video Frame Coder* ®.

A análise comportamental no campo de rastreamento de visão frequentemente demanda como dado bruto movimentos oculares categorizados de acordo com os estímulos, respostas e condições experimentais de interesse. Uma estratégia comum (ver [Dube et al, 2010][dube]; [Huziwara, Souza & Tomanari, 2016][huziwara]; Mescouto, 2011; [Perez, Endemann, Pessôa & Tomanari, 2015][perez]) para produzi-los tem sido a categorização por meio de inspeção visual *post facto* dos vídeos produzidos por rastreadores. Tal trabalho tem sido feito com o auxílio de um programa de computador chamado *Video Frame Coder* ® , que, segundo os autores, "torna a tarefa viável".

Alguns problemas merecem ser destacados sobre esse método. Primeiro, mesmo com o auxílio daquele programa de computador, trata-se de um método que consome muito tempo; um vídeo com 50.000 quadros implica ~4-6 h de trabalho repetitivo. Segundo, ele é especialmente suscetível ao erro humano; um aspecto intrínsico à inspeção visual. Terceiro, é plausível sugerir que é um método entediante e não provê reforçadores intrínsicos ao exercício científico. Quarto, o método depende de um *software* fechado; os cientistas interessados em um maior escrutínio do método não teriam acesso aos meios para tanto. Quinto, a categorização é feita por meio de critérios difíceis de serem operacionalizados; um maior rigor poderia ser alcançado por meio de concordância entre os categorizadores, mas isso implica um maior custo. Por fim, sugere-se que o contexto aplicado demanda uma agilidade não contemplada por esse método.

Como sofisticar esse processo tornando-o mais acessível ao cientista de tradição analítico comportamental? 

## Análise do comportamento e Rastreamento de Visão: a geração PUPIL.

Uma alternativa é automatizar o procedimento de categorização por meio de soluções open-source ou soluções livres. É importante notar que, para fins de pesquisa científica, acessibilidade não se alinha necessariamente com extremo baixo custo ou consumo de massa. O mais importante são a natureza (se é um sistema aberto ou fechado), a documentação (ser farta ou escasssa) e as funcionalidades do sistema (isto é, se permite ou fornece a automação de interesse).

Considerando esses três pontos, a plataforma PUPIL (https://pupil-labs.com; uma iniciativa da *Pupil Labs*, uma *startup* alemã fundada por M. Kassner, W. Patera e A. Bulling; ver [Kassner, Patera & Bulling, 2014][pupil]) apresenta-se como uma alternativa do tipo promissora. Primeiro, porque baseia-se em *softwares* 100% *open-source*. Segundo, possui farta documentação tanto a cientistas de dentro quanto a cientistas de fora das ciências da computação. E terceiro, fornece e permite a automação de diferentes tarefas.

Considerando as funcionalidades dessa plataforma, três aspectos que foram especialmente úteis para o sistema até então montado serão destacados a seguir.

### PUPIL: Transformações homográficas de superfícies de interesse

A plataforma permite a detectação automática de superfícies (áreas de interesse) por meio de marcadores fiduciários. A detecção e a trasformação de perspetiva das superfícies é feita automaticamente. Os dados, então, podem ser exportados para análises subsequentes.

### PUPIL: Plugins de Tempo de Execução

A plataforma é facilmente adaptável por meio da linguagem Python. O experimento que apresentarei envolvia distratores e como os marcadores fiduciários também poderiam funcionar como distratores, optei por evitar o seu uso. Assim, adaptei um plugin da plataforma para utilizar a tela de apresentação dos estímulos, ao invés dos marcadores, como referência para as superfícies.

### PUPIL: Modelo 3D dos olhos

A plataforma possui um algoritmo de detecção ocular baseado na construção de um modelo 3D dos olhos do participante. Essa construção tanto permite grande estabilidade na acurácia durante longos períodos quanto permite uma calibragem mais ágil do sistema (que dura aproximadamente 30 s). O experimento que estarei apresentando exigia no mínimo 15 min de estabilidade. Infelizmente, essa funcionalidade não estava disponível na época em que os dados que apresentarei foram coletados. Mesmo assim, o fato de a plataforma fornecer tal funcionalidade merece destaque.

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

O estudo era conduzido em uma sala com iluminação não controlada entre 300 e 640 LUX (lumens/m2). Os movimentos oculares eram capturados por meio do rastreador ocular Pupil Dev, que possui uma câmera frontal e uma câmera ocular, ambas com 30hz. Uma tela de apresentação era projetada em uma das paredes da sala e um descanço para o queixo planejado ergonomicamente para se adequar a postura natural dos participantes assegurava que a tela sempre estava no campo de gravação da câmera frontal. O projetor e um botão de respostas ambidestro estavam conectados a um computador executando o programa *[Stimulus Control][stimulus-control]*. O programa registra as respostas ao botão e controlava a apresentação de estímulos de maneira sincronizada (por meio de *sockets* TCP/IP) com o programa Pupil Capture, que por sua vez registrava os movimentos oculares e controlava a calibragem do rastreador. Posteriormente a coleta, o programa *Pupil Player* detectava a tela de apresentação dos estímulos e permitia exportar os dados para categorização por meio do algoritmo DBSCAN ([Ester et al, 1996][ester]), tal como implementado por [Pedregosa et al, 2011][scikit-learn]. A implementação da categorização utilizou a linguagem Python.

#### Procedimento e Análise de dados

Com as categorias de movimentos oculares em mãos, a taxa de movimentos oculares era calculada em cada um dos estímulos apresentados. Isso só era possível porque todos os eventos de interesse (isto é, movimentos oculares, respostas, início dos estímulos, etc.) recebiam um tempo extraido de um mesmo fluxo de tempo monotônico. Os eventos permitiam a segmentação temporal das respostas ao botão e movimentos oculares. A taxa de respostas ao botão durante o estímulo vermelho e durante o estímulo azul também eram calculadas.

Um delineamento ABA era apresentado. Na condição A, vermelho e azul estavam associados a CRF (pressionar uma vez o botão produzia um som associado a dinheiro). Na condição B, apenas vermelho estava associado a CRF, o que permitia a ocorrência de discriminações.

Vermelho e azul sempre eram apresentados à esquerda; verde e ciano sempre à direita (distratores). Controle por aspectos temporais eram evitados com a alternância de cores aleatoriamente. Note, embora aleatoriamente, as cores se alternavam sempre sucessivamente, nunca simultaneamente, da seguinte maneira: Vermelho e Verde, Vermelho e Ciano, Azul e Ciano, Azul e Verde.

#### Resultados

Um responder discriminativo foi observado no desempenho de sete dos dez participantes deste estudo. Dentre desempenhos discriminativos, três deles envolveram movimentos oculares de acordo com a predição, isto é, foi observada uma tendência de olhares à esquerda na condição B em contraste com os olhares à direita e à esquerda na condição A. Embora apenas trẽs participantes tenham demonstrado um desempenho de acordo com a previsão, foram observadas mudanças no padrão de movimentos oculares durante a condição B com outros dois participantes. Ou seja, foram observadas mudanças no padrão de movimentos oculares entre as condições A e B com cinco daqueles sete participantes.

Mudanças no padrão de movimentos oculares entre as condições A e B não foram observadas no desempenho dos três participantes que não responderam discriminativamente.

Figuras e dados brutos disponíveis em https://github.com/cpicanco/abpmc-2016.

#### Discussão

Embora a utilização do DBSCAN tenha se mostrado precisa, mais acessível e menos custosa do que a categorização manual, a estratégia é adequada apenas para análises **post facto** e não permite a categorização em tempo real dos movimentos oculares. Entretanto, até o momento de escrita do presente estudo, métodos mais econômicos computacionalmente ou não eram de conhecimento deste autor ou não eram comparavelmente acessíveis. Prevê-se, por fim, que a detecção de categorias em tempo real poderá tornar o método obsoleto.

É possível considerar como possíveis etapas para estudos futuros os seguintes pontos:
 - Aplicar o método a uma tarefa com nove estímulos apresentados simultaneamente.
 - Explorar métodos computacionais com o objetivo de automatizar a inspeção visual dos dados.
 - Explorar métodos computacionais com o objetivo de detectar os movimentos oculares em tempo real.
 - Otimização automática dos parâmetros de densidade do DBSCAN.

## Referências

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
