XXV Encontro Brasileiro de Psicologia e Medicina Comportamental, 2016, Foz do Iguaçu, Brasil.

# Análise do comportamento por meio de rastreamento de movimentos oculares: uma nota técnica.

Carlos Rafael Fernandes Picanço & François Jacques Tonneau.   
Universidade Federal do Pará, Belém, PA, Brasil.

**Resumo**

O rastreamento de movimentos oculares tem sido reconhecido como um método que permite estudos analítico comportamentais de novos e antigos problemas no campo de controle de estímulos, mas tem sido pouco utilizado por questões de acessibilidade. O objetivo deste trabalho foi 1) montar um laboratório acessível para a condução de tais estudos e 2) demonstrar o laboratório em funcionamento por meio de um estudo sobre discriminação simples (com delineamento ABA). O laboratório (custo total ~R$3350) dependia da plataforma opensource Pupil e incluia um rastreador (Pupil Dev), um computador (i3, 2GB-DDR3, Linux/OS), um botão de respostas, luzes dimerizadas e um descanço para o queixo. Dez universitários adultos com visão normal (4M-6F) recebiam a instrução: "A sua tarefa é ganhar pontos apertando o botão". Cada condição (A, B e A) durava 5 min e iniciava com a apresentação de dois estímulos igualmente espaçados em relação ao centro de uma tela, sendo um quadrado à esquerda (alternando sua cor entre vermelho e azul) e um círculo à direita (alternando sua cor entre verde e ciano). Controle por aspectos temporais eram evitados com a alternância de cores aleatoriamente, com duração média de 15 s (mínimo 11, máximo 20). Na condição A, vermelho e azul estavam associados a CRF, isto é, discriminações simples entre essas cores não eram possíveis. Na condição B, vermelho estava associado a CRF e azul à extinção, permitindo a ocorrência de discriminações simples. As cores verde e ciano não possuiam consequências programadas (distratores). Assim, induzia-se a alternância de fixações do olhar entre os estímulos. Os movimentos oculares foram categorizados entre esquerda e direita por meio do algoritmo DBSCAN. Foram graficados perfis temporais com a taxa de movimentos oculares em cada categoria e a taxa de respostas ao botão em cada categoria que, inspecionados visualmente, permitiam avaliar a ocorrência ou não de mudanças correlatas entre movimentos oculares e respostas ao botão.

*Palavras-chave*: rastreamento de movimentos oculares; discriminações simples; acessibilidade.

## Apresentação Oral

Carlos Rafael Fernandes Picanço

Este trabalho não seria possível sem o apoio da CAPES (Bolsa de doutorado ao primeiro autor).

**tl;dr**

Ao longo desta apresentação eu apresentarei um método automático de análise de dados comportamentais baseado em segmentação temporal e em um algoritmo (DBSCAN) de categorização amplamente reconhecido no campo da 'Descoberta de Conhecimento e Mineração de Dados'. Argumentarei que o uso plataforma PUPIL de rastreamento de visão conjuntamente com algoritmos to tipo permite abandonar (ou ao menos reduzir o uso de) um despendioso e entediante método; a saber, a categorização por inspeção visual, quadro-a-quadro, dos vídeos produzidos por rastreadores de visão. Argumentarei, também, que a plataforma PUPIL é a mais acessível da atualidade a pesquisadores fora das ciências da computação interessados em visão computacional. Em seguida, por meio de um micro-experimento, demonstrarei um sistema de rastreamento de visão em funcionamento por meio das referidas tecnologias. Por fim, deixarei a previsão de que o Aprendizado de Máquina, embora atualmente não tão acessível  quanto o método proposto, irá torná-lo obsoleto e pode ser uma solução última e definitiva para trabalhos futuros de categorização de estímulos e respostas em diferentes meios.

**tl;rl**

## Rastreadores de visão e sua dependência de *softwares* 
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

Pois acho que isso pode e deve mudar. Passemos, então, ao ponto específico do trabalho.

___

## Análise do comportamento e Rastreamento de Visão: a geração *Video Frame Coder* ®.

A análise comportamental no campo de rastreamento de visão frequentemente demanda como dado bruto movimentos oculares categorizados de acordo com os estímulos, respostas e condições experimentais de interesse. Uma estratégia comum para produzi-los tem sido a categorização por meio de inspeção visual *post facto* dos vídeos produzidos por rastreadores. Tal trabalho tem sido feito com o auxílio de um programa de computador chamado *Video Frame Coder* ® ([Dube et al, 2010][dube]; [Huziwara, Souza & Tomanari, 2016][huziwara]; Mescouto, 2011; [Perez, Endemann, Pessôa & Tomanari, 2015][perez]), que, segundo os autores, "torna a tarefa viável".

Alguns problemas merecem ser destacados sobre esse método:

- mesmo com o auxílio do software, ele consome muito tempo
    - um vídeo com 50.000 quadros implica ~2 h de trabalho repetitivo;
- é especialmente suscetível ao erro humano;
   - aspecto intrínsico à inspeção visual;
- é entediante;
- depende de um *software* fechado;
- o contexto aplicado demanda uma agilidade não contemplada por esse método;

Como sofisticar esse processo tornando-o mais acessível? 

## Análise do comportamento e Rastreamento de Visão: a geração PUPIL.

A plataforma PUPIL (https://pupil-labs.com; uma iniciativa da *Pupil Labs*, uma *startup* alemã fundada por M. Kassner, W. Patera e A. Bulling; ver [Kassner, Patera & Bulling, 2014][pupil]) apresenta-se como uma alternativa promissora. Até aonde o meu conhecimento pode ir, ela é a mais acessível e sustentável solução de rastreamento de visão da atualidade:

- baseia-se em *softwares* 100% *open-source*;
- possui uma comunidade ativa;
- tem tido considerável impacto no [campo acadêmico][pupil-citations];
- possui farta documentação;
   - para cientistas de dentro e de fora das ciências da computação;
   - com base em minha própria experiência, considerando um aluno familiarizado com computadores:
      - estimo 3 meses de estudo para o operador iniciante antes da primeira coleta monocular (Dado bruto: pontos);
      - estimo 6 meses de estudo para o operador iniciante antes da primeira coleta binocular (Dado bruto: vetores);
- está em pleno e estável desenvolvimento a mais de 4 anos;	
- permite investigações no campo do rastreamento de visão e visão egocêntrica;
- permite experimentos estacionários e em movimento;
- possui qualidade de dados aceitáveis para análises comportamentais;
   - acurácia de 0.5 a 1.0 grau do ângulo de visão;
   - precisão 0.08 grau;
   - granularidade 30 hz a 120 hz;
- preço rasoável para uso não comercial em contexto acadêmico;
   - você pode montar um Pupil Dev por $300 + tempo de construção;
   - ou comprar um Pupil Pro (Monocular) €1050;
- etc.

É importante notar que, para fins de pesquisa científica, acessibilidade não se alinha necessariamente com extremo baixo custo ou consumo de massa. 

Destaco agora três aspectos da plataforma que foram especialmente úteis para o sistema até então montado.

### PUPIL: Transformações homográficas de superfícies de interesse

- A plataforma PUPIL permite a detectação automática de superfícies (áreas de interesse) por meio de marcadores fiduciários. A detecção e a trasformação de perspetiva das superfícies é feita automaticamente.

### PUPIL: Plugins de Tempo de Execução

- Facilmente adaptável por meio da linguagem Python;
- Porque a tarefa programada envolvia distratores, optei por evitar o uso dos marcadores fiduciários, pois eles poderiam funcionar também como distratores. Assim, o programa foi adaptado para utilizar a tela de apresentação dos estímulos como referência para as superfícies.

### PUPIL: Modelo 3D dos olhos

- A plataforma PUPIL possui um algoritmo de detecção ocular baseado na construção de um modelo 3D dos olhos do participante. Isto tanto permite grande estabilidade na acurácia ao longo da coleta de dados quanto permite uma calibragem mais ágil (~30 s).

### PUPIL: um atalho para a aplicação.

- A plataforma, por ser pouco obtrusiva e permitir tanto aplicações estacionárias quanto em movimento, permite avaliar prontamente técnicas e métodos análicos desenvolvidos no laboratório a problemas reais. Essa possibilidade se reduz com sistemas exclusivamente estacionários.

- A cada nova atualização a plataforma torna-se cada vez mais *plug-and-play*. 

## Um micro-experimento comportamental

Aprovado pelo comitê de ética (CAAE: 35142814.0.0000.5172).

### Objetivo

Identificar, por meio de inspeção visual, correlações entre movimentos oculares e o responder discriminativo em uma tarefa de discriminação simples sucessiva com estímulos distratores.  

### Método
#### Participantes

- 6M-4H
- visão normal
- universitários
- 19-26 anos
- termo de consentimento livre e esclarecido assinado.

#### Equipamento

**Hardware**

- Uma sala com ~640 LUX (lumens/m2). 
- Pupil Dev, câmera frontal (30hz) e câmera do olho (30hz).
- Um descanço para o queixo;
- Um botão de respostas;
- Dois computadores, um para o programa **Pupil Capture**, outro para o programa **Stimulus Control** (sincronização por meio de *sockets* TCP/IP).

**Software**

- O programa *Pupil Capture* registrava os movimentos oculares (pontos, x y) e gerenciava a calibragem do sistema.

- Um plugin do *Pupil Player* adaptado por mim para detectar e realizar a transformação homográfica da tela de apresentação dos estímulos.

- O programa *[Stimulus Control][stimulus-control]* foi utilizado para o registro e controle da apresentação dos estímulos. Ele é um programa de código livre (GPL3), uma versão modificada por mim do programa EAM (Emparelhamento ao modelo), desenvolvido por Drausio Capobianco.

Ele foi integrado com o programa Pupil Capture com objetivo de:

- automatizar o início e parada da gravação dos movimentos oculares;
- sincronização temporal eventos comportamentais e movimentos oculares registrados por um mesmo computador;
- automatizar o início e parada do procedimento de calibragem*;
- sincronização temporal de eventos comportamentais e movimentos oculares registrados por computadores distintos*;

nota: * trabalho em curso.

#### Análise de dados

**DBSCAN**

Após tratar e exportar os movimentos oculares por meio da plataforma PUPIL, o algoritmo DBSCAN era usado para gerar duas categorias de interesse. Esquerda e direita.

A estratégia assume uma condição que promova, ao menos inicialmente, movimentos oculares sobre todos os lugares nos quais os estímulos de interesse serão apresentados (posições).

O algoritmo não exige o número total de estímulos utilizados, mas apenas dois critérios:

- eps (perímetro de referência, e.g., distância euclidiana);
- limite (número mínimo de ocorrências dentro perímetro de referência);

As posições devem possuir um espaçamento maior do que o perímetro de referência.

O método pode ser adaptado a diferentes tipos de movimento oculares e um número de estímulos limitado pelo tamanho da superfície de apresentação.

**Segmentação temporal**

Com as categorias de movimentos oculares em mãos, a taxa de movimentos oculares era calculada em cada um dos estímulos de maneira correspondente. Isto só era possível porque todos os eventos (movimentos oculares, respostas, início dos estímulos, etc.) recebiam um tempo extraido de um mesmo fluxo de tempo monotônico (Ver seção Análise de Dados). 

O algoritmo DBSCAN ([Ester et al, 1996][ester]), tal como implementado por [Pedregosa et al, 2011][scikit-learn], foi utilizado para gerar duas categorias de movimentos oculares de interesse (COI): esquerda e direita. O método é análogo, mas não idêntico, ao mapeamento de áreas de interesses (AOI).

O programa *Stimulus Control* registrava os eventos comportamentais de maneira sincronizada com o programa *Pupil Capture*. Cada evento recebia um tempo extraido de um mesmo fluxo de tempo monotônico, implementado por meio da função `clock_gettime`, padrão em sistemas Linux (time.h). Assim, os eventos comportamentais eram combinados com as categorias COI e permitiam a filtragem de resposta e movimentos oculares durante cada uma das cores, de tal forma que eram calculadas oito taxas de movimentos oculares:

- Quando apresentados Vermelho e Verde: 
   1. taxa de movimentos oculares ao Vermelho
   2. taxa de movimentos oculares ao Verde
- Quando apresentados Vermelho e Ciano:
   3. taxa de movimentos oculares ao Vermelho
   4. taxa de movimentos oculares ao Verde 
- Quando apresentados Azul e Verde:
   5. taxa de movimentos oculares ao Azul
   6. taxa de movimentos oculares ao Verde
- Quando apresentados Azul e Ciano:
   7. taxa de movimentos oculares ao Azul
   8. taxa de movimentos oculares ao Ciano

A taxa de respostas ao botão durante o estímulo vermelho e a taxa de respostas ao botão durante o estímulo azul também eram calculadas. Em seguida, os dados comportamentais e de movimento ocular eram graficados e comparados por meio de inspeção visual.

#### Procedimento e Resultados

Delineamento ABA:

- A: vermelho e azul estavam associados a CRF.
- B: apenas vermelho estava associado a CRF.

Vermelho e azul sempre à esquerda; verde e ciano sempre à direita (distratores). Controle por aspectos temporais eram evitados com a alternância de cores aleatoriamente, com duração média de 15 s (mínimo 11, máximo 20). Note, embora aleatoriamente, as cores se alternavam sempre sucessivamente, nunca simultaneamente, de acordo com a seguinte ordem de apresentação dos estímulos:

- Vermelho + Verde
- Vermelho + Ciano
- Azul + Verde
- Azul + Ciano

#### Discussão

#### Etapas seguintes

 - Aplicar o método a uma tarefa com nove estímulos apresentados simultaneamente.

## Análise do comportamento e Rastreamento de Visão: a geração Aprendizado de Máquina?

Ver [Arcas, 2016][arcas].

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