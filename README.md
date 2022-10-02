# Projeto E-Tickets

<hr>

<h2>Sumário</h2>

- [0. Introdução](#0-introducao)
  - [0.1. Problema de Negócio](#01-problema-de-negocio)
- [1. Justificativa](#02-justificativa)
  - [1.1. Proposta de Solução](#11-proposta-de-solucao)
- [2. Objetivos](#2-objetivos)
  - [2.1. Primeiro Cíclo de Desenvolvimento](#21-primeiro-ciclo-de-desenvolvimento)
    - [2.1.1. Kickoff do MVP E-Tickets](#211-kickoff-do-mvp-etickets)
- [3. Desenvolvimento](#3-desenvolvimento)
  - [3.1. Análise do MVP](#31-analise-do-mvp)
    - [3.1.1. O Produto É, Não É...](#311-o-produto-e-nao-e)
    - [3.1.2. Identificação das Personas](#312-identificacao-das-personas)
    - [3.1.3. Brainstorm de Funcionalidades](#313-brainstorm-de-funcionalidades)
  - [3.2. Fluxo da Aplicação](#31-macro-fluxo-da-aplicacao)
    - [3.2.1. Macro Fluxo & Macro Fluxo Detalhado](#321-macrofluxo-e-macrofluxo-detalhado)
    - [3.2.2. Diagrama de Relacionamento](#322-diagrama-de-relacionamento)
  - [3.3. Implementações](#33-implementacoes)
    - [3.3.1. Layout & Banco de Dados](#331-layout-e-banco-de-dados)
    - [3.3.2. Solução de pagamento com picpay](#332-solucao-de-pagamento-com-picpay)
    - [3.3.3. Deploy da Solução para Segmentos Específicos](#333-deploy-do-mvp-para-segmentos-especificos)
- [4. Conclusão & Próximos Passos](#4-conclusao-e-proximos-passos)
- [5. Bibliografia](#5-bibliografia)

<hr>

<h2>0. Introdução</h2>
<hr>

<p>A aplicação E-Tickets é um projeto integrador da Universidade Cruzeiro do Sul Virtual que foi desenvolvido em Python e o framework de desenvolvimento web chamado Streamlit.</p>
<p>O intuito desse projeto foi aplicar todo o conhecimento teórico adquirido em mais um projeto integrador, esse por final, integrando várias áreas do conhecimento que foram estudadas ao longo do curso. Partindo de diversos conceitos como análise de negócio com o stakeholder do problema até a parte do deploy com a Streamlit Cloud.</p>
<p>A ideia era desenvolver um  E-Commerce que vende tickets para eventos culturais npara a cidade de Fraiburgo, onde José, personagem fictício, empreendedor e principal stakeholder e demandante da solução, o mesmo possui de alguns empreendimentos do mesmo gênero, requisitou essa aplicação.</p>
<a href="https://youtu.be/fZ-2bu7mfo0">Vídeo demostrativo do projeto E-Tickets</a>


<h3>0.1. Problema de Negócio</h3>
<hr>

<p>Primeiramente, a ideia inicial e motivação desse projeto veio à mente quando meu amigo empreendedor José um jovem de 24 anos, dono de alguns estabelecimentos na cidade de Fraiburgo-SC tentou alavancar seu relacionamento com os seus clientes que é uma das bases do Lean Canvas uma ferramenta de modelos de negócios que ele conheceu pesquisando mais sobre empreendimentos online.</p>
<p>Para atingir tais relacionamentos, ele precisava de uma ferramenta ou mais uma proposta de valor, a ideia dele foi contratar alguém para rapidamente desenvolver um mvp de um e-commerce de vendas de tickets online para assim conseguir ter mais uma proposta de valor, porém, ele estipulou alguns prazos para a entrega do projeto, deveria estar pronta em pelo menos três dias uma semana para assim não gastar muito dinheiro com recursos em uma ferramenta que talvez seus clientes nem utilize, essa é um dos conceitos do mvp. Com base no parágrafo anterior, foi contratado um desenvolvedor para atuar nesse projeto passando todo o contexto atual da empresa.</p>


<h2>1. Justificativa</h2>
<hr>

<p>A justificativa dessa iniciativa basicamente se dá pelo fato do empreendedor José querer gerar mais valor para seus clientes utilizando uma ferramenta que é a tecnologia para seus clientes, essa solução de valor deve ser entregue o mais rápido possível com as funcionalidades mínimas necessárias e uma documentação detalhada para somente assim não custar muito dinheiro para o jovem empreendedor e também para que o mesmo não invista demasiados esforços em uma hipótese que essa solução vai gerar valor aos seus clientes.</p>
<p>Com essa aplicação, seus usuários de maior valia vão ter acesso a aplicação para testes e vão poder comprar tickets do conforto de sua residência ou de qualquer outro lugar precisando apenas de uma conexão com a internet, até o cliente valioso mais velho de casa sem muita experiência com o atual cenário tecnológico e inovador que a sociedade vive vai poder fazer a compra de seu ticket de uma forma simples, em questão de dificuldade a ideia é ter zero!</p>
<p>Toda a aplicação deve responder rapidamente ao cliente com as devidas informações dos tickets e de alguma forma deve ser de fácil acesso tanto para todos quando o mvp for validado pelo cliente e seus clientes valiosos ou early adopters do José, artistas e microempresas do ramo cultural e social também podem se beneficiar com a aplicação, devido que uma das ideias futuras é implementar um sistema que eles mesmos, baseados no cnpj, pessoas ou terceiros poderão fazer o uso da aplicação para inserir nela seus tickets de show ou relacionados, fazendo assim alianças fortes que é um dos princípios do Lean Canvas com até mesmo grandes empresas do ramo cultural.</p>


<h3>1.1. Proposta de SOlução</h3>
<hr>

<p>A solução então foi proposta ao Empreendedor que gostou da aideia da aplicação e das primeiras reuniões, logo o levantamento dos devidos requisitos da aplicação foram levantados e toda a documentação devidamente registrada.</p>

<h2>2. Objetivos</h2>
<hr>

<p>Para resumir todo o levantamento de requisitos, basicamente aqui abaixo no readme, tentei enxugar em três principáis parted o levantamento de requisitos baseados na minha experiência e também para deixar mais simples o readme.</p>
<ul>
  <li>Análise do Produto</li>
  <li>Análise do Fluxo do Cliente</li>
  <li>Análise do Desenvolvimento</li>
</ul>

<p>Para a análise do primeiro ciclo relacionado ao produto, é como que esse produto vai ser desenvolvido, para que ele serve, o'que ele faz, quem vai utilizar o mesmo, essas e outras são perguntas que devem ser detalhadas para essa primeira análise do levantamento dos requisitos. Para a sessão fluxo de cliente são diagramas gerais e mapas mentais de como a aplicação se comporta diante do usuário e o'que ele faz na mesma. Por fim, a análise do desenvolvimento é, baseada em todo o pipeline previamente estabelecido, como que vai ser a modelagem dos dados, qual ferramenta usar para desenvolver e assim por diante.</p>

<h3>2.1. Primeiro Cíclo de Desenvolvimento</h3>
<hr>

<p></p>

<h4>2.1.1. Kickoff do MVP E-Tickets</h4>
<hr>

<p>Foi utilizado como base o Livro Lean Inception e conhecimentos adquiridos no curso para desenvolver esse kickoff e muitos outros conceitos utilizados na elaboração deste trabalho, como análise de swot, trade-off, etc. Mas para o0 Kickoff basicamente é a demanda do projeto depois da conversa com o cliente, foi demandado uma aplicação onde o usuário pode comprar seus tickets em uma plataforma simples e rápida, onde o conceito de mvp cabe perfeitamente.</p>


<h2>3. Desenvolvimento</h2>
<hr>


<h3>3.1. Análise do MVP</h3>
<hr>

<p>O desenvolvimento geralmente começa da quebra do problema de negócio em tarefas menores, com essa atividade puramente lógica, o desenvolvedor consegue entender sobre o negócio e mapear pontos de melhoria, possíveis impeditivos e algumas das vezes, responder uma pergunta pertinente o porquê do desenvolvimento dessa aplicação, a resposta para a última pergunta ajuda o dev a elaborar uma solução e a definição de um escopo mais claro e entender o negócio e também de alguma forma quais as personas que vão ser afetadas pelo investimento dessa aplicação.</p>
<p>Basicamente o conceito de MVP, citado no livro Lean Inception resumidamente afirma que é a primeira versão do produto a ser desenvolvida baseada em pesquisas com os clientes, existem diversas metodologias utilizadas no livro que foram citadas no projeto integrador que resumidamente vou citar ao decorrer do desenvolvimento :)</p>


<h4>3.1.1. O Produto É, Não É...</h4>
<hr>

<p>Essa etapa irá guiar todo o time para responder a seguinte pergunta, para que serve a aplicação?</p>
<p>Respondendo essa pergunta ajuda o time a focar esforços em análises mais precisas em certas áreas (análise de trade-off) e também todo o time já sabe o'que o desenvolvedor pretende ou vai fazer reduzindo assim o tempo elaborando 'features' que não seram utilizadas ou para o momento do mvp são irrelevantes ou não fazem sentido. Um exemplo simples é, a aplicação E-Ticket 'não é' para assistir vídeos. Todas essas respostas são anotadas em uma tabela com todos da equipe alinhando expectativas de negócio e de desenvolvimento.</p>


<h4>3.1.2. Identificação das Personas</h4>
<hr>

<p>Essa etapa é muito importante também, responde mais uma pergunta, para quem é meu produto?</p>
<p>A aplicação E-Tickets é para jovens, adultos, artistas em geral que querem comprar um determinado ticket ou registrar um ticket na aplicação para ser possivelmente vendida, resumidamente isso serve para o desenvolvedor com ajuda do time de UX selecionar cores mais atrativas e toda a parte de pesquisa qualitativa e até possíveis testes de inferência futuramente na aplicação.</p>


<h4>3.1.3. Brainstorm de Funcionalidades</h4>
<hr>

<p>Após todo o time alinhado e devidamente sabendo de todas as etapas e para quem é o produto, vem a análise de brainstorm de funcionalidades, nessa etapa é mapeado processos, fluxos etc, em diversas ferramentas como Mind-maps, fluxogramas, análise de swot/fofa, politicas de privacidade e proteção dos dados etc.</p>


<h3>3.2. Fluxo da Aplicação</h3>
<hr>

<p>De alguma forma seria o conceito sistema Cliente-Servidor para a aplicação que vai estar hospedada na web e toda a interação que o cliente vai ter e os determinados fluxos na aplicação, os mesmos caso o mvp seja continuado já até podem ser mapeados em futuros testes a/b entre outros conceitos importantes, para não 'viajar' muito nessa etapa do processo, já foi pré-determinada na análise de trade-off, swot e nos levantamentos de requisitos anteriores com o time de desenvolvimento e negócio.</p>


<h4>3.2.1. Macro Fluxo & Macro Fluxo Detalhado</h4>
<hr>

<p>É o detalhamento do fluxo do usuário com a aplicação, esse diagrama serve para ilustra todos os processos do cliente detalhando até exeções e tratamentos de erros, principalmente em aplicações puramente comerciais como é o caso da aplciação e-ticket para o José.</p>
<p>Para ilustração, imagine-se em qualquer e-commerce, existe um funil caso você selecione um produto e próxima ao pagamento, para evitar distrações e possível perda da venda não existem muitos 'ramos' da aplicação quando você está no processo de compra, qualquer distração ou erro de sistema como exemplo a demora no processamento pode levar o cliente a descontinuar o processo de compra e aumentando a métrica de abandono de carrinho.</p>


<h4>3.2.2. Diagrama de Relacionamento</h4>
<hr>

<p>Está ligado no processo de modelagem de dados, toda aplicação precisa gerar dados, sejam transacionais ou até mesmo processos de iteração como clicks, scroll, clique no carrossel de produtos, tempo de página entre outros, diante desse processo, como você pretende armazenar esses dados, qual vai ser o diagrama de entidade de relacionamentos dessas tabelas, essa etapa define esses relacionamentos, dado o mvp, não foi incluído análises do google analytics (GA), apenas um processo simples de armazenamento dos tickets a venda, sistema de compra e venda de tickets e a tabela de registros do picpay.</p>


<h3>3.3. Implementações</h3>
<hr>

<h4>3.3.1. Layout & Banco de Dados</h4>
<hr>

<p>Quanto ao desenvolvimento, escolhi o framework de desenvolvimento em python chamado Streamlit e a ferramenta de busca chamada Elasticsearch para a recuperação de nomes de tickets rapidamente, para incrementar a interação do usuário inserindo um sistema de pesquisa de tickets e um sistema de cadastro de usuários, pois o cliente só consegue efetivamente concluir a compra caso o mesmo já esteja cadastrado na aplicação, caso contrário não vai conseguir visualizar o carrinho de compras. Com as devidas autenticações o fluxo segue para o carrinho e o preenchimento do formulário que será enviado ao Picpay com a cobrança do ticket escolhido.</p>
<p>Tanto no momento do registro do cliente e no momento quando o mesmo efetivamente realiza a requisição ao picpay, são respectivamente enviados dois e-mail de confirmação ao usuário.</p>

<h4>3.3.2. Solução de pagamento com picpay</h4>
<hr>

<p>A solução para o pagamento do picpay foi escolhida justamente pela simplicidade na implementação, outras soluções mais automaticas podem não ser tão simples de implementar, e como o mvp deve ser rápido como cita no livro Lean Inception, foi escolhido o Picpay para fazer as devidas requisiçẽos de compra.</p>
<a href='https://studio.picpay.com/produtos/e-commerce/checkout/resources/api-reference'>Documentação da API do Picpay</a>

<h4>3.3.3. Deploy da Solução para Segmentos Específicos</h4>
<hr>

<p>Dado a magnitude e o cuidado com a aplicação, o empreendedor José decidiu que para a primeira solução em produção, a mesma só vai ser disponível a segmentos de clientes específicos, como já citado no livro 'Business Model', a segmentação de clientes podem ser feitas de diversas formas como por tipo de mercado, clientes específicos, geográficos, físicos, culturais, entre outros fatores. Para o caso de José, ele escolheu os clientes mais importantes da base para testarem a aplicação dando reconhecimento a esses clientes e para testar o mvp também.</p>

![image](https://user-images.githubusercontent.com/75986085/193456748-ce35ad84-6f91-4332-809a-66a87281e010.png)

Capítulo I, Segmentos de Clientes, Livro: Business Model Generation.

<h2>4. Conclusão & Próximos Passos</h2>
<hr>

<p>A solução foi desenvolvida rapidamente para gerar valor ao José e confiabilidade dele no desenvolvimento da solução. Diante disso, muitos detalhes levantadas na etapa de trade-off e levantamento de requisitos foram deixadas de lado por que não era momento dado a etapa do mvp (que não tinha saído do papel) então, futuras implementações destas vão ser elaboradas ao decorrer das novas versões do MVP, como soluções diferentes de pagamentos de tickets, incremento na base de tickets e até possíveis testes de inferência estatística podem ser implementados para melhorar a experiência do usuário, mas isso são conceitos para futuras versões do MVP.</p>
<p>Conceitos como MVP e desenvolvimento cíclico são muito importantes, principalmente para startups que possuem um crescimento muito rápido, ideias são descartadas em semanas se não forem implementadas rapidamente.</p>

<h2>5. Bibliografia (Livros)</h2>
<hr>

<a href='https://tudelft.openresearch.net/image/2015/10/28/business_model_generation.pdf'>Livro: Business Model Generation</a>
<a href='https://caroli.org/en/livro/lean-inception-how-to-align-people-and-build-the-right-product'>Livro: Lean Inception</a>
