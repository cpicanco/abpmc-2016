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

Mas e se a questão for um falso dilema? Um primeira solução seria: pode ser sábio construir, como aquele querido professor já havia sugerido. Por exemplo, um *software* livre para experimentos comportamentais pode contribuir como um nicho de diversificação da análise do comportamento ([Reimer, 2016][reimer]). É importante notar que a engenharia de *softwares* comportamentais é uma área recente no escopo das ciências da computação ([Lenberg, 2015][lenberg]), ainda que possa ser vista com saudosismo por alguns analistas do comportamento ([Stephens, 2007][stephens]). É notável, também, que interfaces entre ciências da computação e análise do comportamento já tenham sido feitas no campo da educação técnica ([Harrison, 2005][harrison]).

### Solução 2 - Colabore!

Mas há uma outra alternativa: colaborar. Os cientistas da computação tem desenvolvido plataformas de rastreamento de visão *open-source* acessíveis. A solução para nós é usá-las; e eu devo inclusive sugerir, apoiá-las e sofisticá-las. Após comprar ou construir o seu lindo rastreador, você pesquisador deverá assegurar que pode usá-lo de maneira automatizada, transparente e inovadora. Seja durante a coleta de dados, seja durante a análise de dados. Isto simplesmente não seria possível sem a iniciativa e apoio de comunidades *open-source*. Por que a análise do comportamento não tem promovido iniciativas *open-source* e *open-science*?

____

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

## Referências
Du Plessis, J. P., & Blignaut, P. (2016). Utilising the GPU to develop a high-speed, low-cost eye tracker. Journal of Eye Movement Research, 9(4), 1:11. http://doi.org/10.16910/9.4.6

Harrison, W. (2005). Skinner Wasn’t a Software Engineer. *IEEE Software*, *22*(3), 5–7. http://doi.org/10.1109/MS.2005.76

Lenberg, P., Feldt, R., & Wallgren, L. G. (2015). Behavioral Software Engineering: a Definiton and Systematic Literature Review. *Journal of Systems and Software*, *107*, 15 – 37. http://doi.org/doi:10.1016/j.jss.2015.04.084

Reimer, D. (2016). The Future of Behavior Analysis: Why we need to Diversify, Part I. Retrieved from http://www.baquarterly.com/2016/01/the-future-of-behavior-analysis-why-we-need-to-diversify-part-i/

Stephens, K. (2007, December 30). Behavioral Software Engineering [Blog]. Retrieved from http://bbs-software.blogspot.com.br/2007/12/behavioral-software-engineering.html

[pupil-citations]:https://docs.google.com/spreadsheets/d/1ZD6HDbjzrtRNB4VB0b7GFMaXVGKZYeI0zBOBEEPwvBI/edit?ts=576a3b27#gid=0
[cogain]:http://wiki.cogain.org/index.php/Eye_Trackers
[du-plessis]:http://doi.org/10.16910/9.4.6
[harrison]:http://doi.org/10.1109/MS.2005.76
[gundlach]:https://www.researchgate.net/publication/26333272_Psychology_as_science_and_as_discipline_the_case_of_Germany
[lenberg]:http://doi.org/doi:10.1016/j.jss.2015.04.084
[reimer]:http://www.baquarterly.com/2016/01/the-future-of-behavior-analysis-why-we-need-to-diversify-part-i/
[stephens]:http://bbs-software.blogspot.com.br/2007/12/behavioral-software-engineering.html
