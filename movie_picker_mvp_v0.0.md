# Movie Picker — MVP v0.0
> Nome provisório do produto. Documento inicial de definição de produto para estudo, validação e implementação.

---

## 1. Visão do produto

O produto é uma aplicação web para ajudar uma pessoa a decidir **qual filme assistir agora**, evitando recomendar filmes que ela já viu e permitindo aplicar alguns filtros simples antes da escolha.

A proposta principal não é competir com catálogos como IMDb, Letterboxd ou serviços de streaming. O foco é resolver um problema menor e mais específico:

> **reduzir a indecisão na hora de escolher um filme.**

A aplicação deve partir de um universo amplo de filmes, remover os títulos que o usuário já assistiu, aplicar filtros opcionais e então selecionar um candidato.

Além da recomendação, o produto deve informar **onde o filme está disponível para assistir na região do usuário**, diferenciando quando possível entre conteúdo incluído em assinatura, aluguel ou compra.

---

## 2. Problema

Usuários que já assistiram a muitos filmes podem ter dificuldade em encontrar algo novo para assistir.

Mesmo quando encontram um título interessante, ainda existe uma segunda fricção:

- descobrir onde o filme está disponível;
- descobrir se ele realmente está disponível no país do usuário;
- diferenciar streaming por assinatura de aluguel ou compra;
- evitar gastar tempo pesquisando manualmente em vários serviços.

O produto deve reduzir essas duas etapas:

1. **Escolher um filme ainda não assistido.**
2. **Mostrar onde ele pode ser assistido na região do usuário.**

---

## 3. Proposta de valor

### Frase principal

> **Escolha para mim um filme que eu ainda não assisti e que eu possa assistir agora.**

### O produto deve priorizar

- rapidez;
- baixa quantidade de decisões;
- surpresa controlada;
- exclusão de filmes já vistos;
- filtros simples;
- disponibilidade regional;
- interface direta.

### O produto não deve se transformar inicialmente em

- rede social;
- catálogo completo de cinema;
- clone do Letterboxd;
- sistema complexo de avaliações;
- plataforma de streaming;
- recomendador baseado em IA;
- sistema de crítica cinematográfica.

---

## 4. Público-alvo inicial

Usuário individual que:

- assiste filmes com frequência;
- já viu muitos títulos;
- frequentemente não sabe o que assistir;
- quer descobrir algo novo;
- pode ter preferências de gênero;
- se importa com avaliação mínima;
- quer saber onde o filme está disponível;
- prefere uma resposta direta em vez de navegar por centenas de opções.

Não existe necessidade, no MVP v0.0, de atender múltiplas personas.

---

## 5. Objetivo do MVP v0.0

Validar o fluxo principal:

```text
Usuário registra filmes já assistidos
        ↓
Solicita uma sugestão
        ↓
Define filtros opcionais
        ↓
Sistema busca candidatos
        ↓
Remove filmes já assistidos
        ↓
Escolhe um filme elegível
        ↓
Mostra o filme
        ↓
Mostra onde assistir na região do usuário
        ↓
Usuário aceita ou pede outro
```

O MVP deve provar que esse fluxo é útil e agradável antes de adicionar funcionalidades mais sofisticadas.

---

# 6. Escopo funcional do MVP v0.0

## 6.1 Conta de usuário

O usuário deve conseguir:

- criar uma conta;
- fazer login;
- encerrar a sessão;
- possuir preferências persistidas.

### Dados mínimos da conta

- identificador;
- e-mail;
- senha armazenada de forma segura;
- região de streaming;
- data de criação.

### Preferência obrigatória

- país/região de streaming.

Exemplo:

```text
BR
US
PT
DE
```

A região deve ser independente do idioma da interface.

---

## 6.2 Registro de filmes já assistidos

O usuário deve conseguir pesquisar um filme pelo título.

A busca deve exibir informações suficientes para diferenciar filmes com nomes semelhantes:

- título;
- ano;
- poster, quando disponível.

O usuário deve conseguir marcar um título como:

```text
Já assisti
```

O sistema deve persistir essa informação.

### Regra central

> Um filme marcado como assistido não pode participar das recomendações futuras daquele usuário.

### O MVP não exige

- data exata em que o filme foi assistido;
- nota pessoal;
- resenha;
- review textual;
- quantidade de vezes assistidas.

Essas informações podem ser consideradas em versões posteriores.

---

## 6.3 Lista de filmes assistidos

O usuário deve conseguir visualizar os filmes marcados como assistidos.

A lista pode ser simples.

Funcionalidades mínimas:

- visualizar filmes;
- remover um filme da lista caso tenha sido marcado por engano.

Não é necessário implementar filtros avançados nessa tela no v0.0.

---

# 7. Escolha do filme

A tela principal do produto deve responder à pergunta:

> **O que assistir hoje?**

O sistema deve permitir dois tipos de uso.

## 7.1 Modo rápido

O usuário não configura nada.

Exemplo:

```text
[ Escolher um filme para mim ]
```

O sistema utiliza critérios padrão definidos pelo produto.

O objetivo é minimizar a tomada de decisão.

---

## 7.2 Modo com filtros

O usuário pode opcionalmente restringir os candidatos.

### Filtros obrigatórios no v0.0

#### Gênero

Exemplos:

- terror;
- drama;
- ficção científica;
- comédia;
- suspense;
- ação.

O usuário pode deixar o campo vazio.

#### Avaliação mínima

Exemplo:

```text
Qualquer
6+
7+
8+
```

O usuário pode deixar o campo sem restrição.

---

## 7.3 Filtro candidato para v0.1

### Duração

Exemplo:

```text
Qualquer
Até 90 min
Até 120 min
Mais de 120 min
```

Duração é considerada uma evolução de alta prioridade, mas não é obrigatória para fechar o v0.0.

---

# 8. Critério de elegibilidade

Um filme só pode participar da seleção se:

1. existir no catálogo externo utilizado;
2. respeitar os filtros definidos;
3. não estiver marcado como assistido pelo usuário;
4. possuir quantidade mínima de avaliações suficiente para evitar títulos com nota pouco confiável;
5. respeitar os critérios básicos de qualidade definidos pelo produto.

Exemplo conceitual:

```text
Todos os filmes
      ↓
gênero = terror
      ↓
nota >= 7
      ↓
quantidade mínima de votos
      ↓
remove assistidos
      ↓
candidatos elegíveis
```

---

# 9. Estratégia inicial de seleção

O MVP **não precisa implementar um sistema de recomendação por IA**.

Também não deve necessariamente aplicar um `random.choice()` completamente ingênuo sobre todo o catálogo.

A estratégia inicial pode ser:

1. obter um conjunto de candidatos elegíveis;
2. excluir títulos assistidos;
3. garantir critérios mínimos de qualidade;
4. escolher aleatoriamente um título entre os candidatos restantes.

Esse comportamento já é suficiente para validar o produto.

---

## 9.1 Por que não usar aleatoriedade totalmente irrestrita

Um catálogo amplo pode conter:

- filmes com pouquíssimos votos;
- títulos obscuros;
- curtas;
- obras cadastradas de forma inconsistente;
- filmes com nota alta baseada em poucas avaliações.

Por isso, o sistema deve considerar pelo menos:

```text
nota média mínima
+
quantidade mínima de votos
```

Os valores exatos devem ser calibrados durante o desenvolvimento.

---

## 9.2 Evolução futura

Posteriormente, a seleção pode se tornar ponderada.

Exemplo:

```text
score =
    qualidade
  + afinidade com preferências
  + disponibilidade
  + serviço já assinado
  + componente aleatório
```

Isso não faz parte do MVP v0.0.

---

# 10. Resultado da recomendação

Ao escolher um filme, a aplicação deve exibir no mínimo:

- poster;
- título;
- ano;
- gêneros;
- nota;
- sinopse;
- disponibilidade de streaming na região configurada.

Exemplo conceitual:

```text
┌─────────────────────────────────────┐
│ The Lighthouse                     │
│ 2019 · Drama / Terror              │
│ ★ 7.4                              │
│                                     │
│ Sinopse...                          │
│                                     │
│ Disponibilidade no Brasil           │
│ MUBI — incluído na assinatura       │
│ Apple TV — aluguel                  │
│                                     │
│ [ Vou assistir ]                    │
│ [ Escolher outro ]                  │
└─────────────────────────────────────┘
```

---

# 11. Ações sobre a recomendação

## 11.1 Vou assistir

Ao aceitar a recomendação, o MVP pode simplesmente registrar que o usuário escolheu aquele filme naquela interação.

Não é obrigatório marcar automaticamente como assistido.

Motivo:

> escolher um filme não significa necessariamente que ele foi assistido.

A marcação como assistido deve continuar sendo uma ação explícita.

---

## 11.2 Escolher outro

O usuário deve poder rejeitar a sugestão e receber outro candidato.

Durante a mesma sessão, o sistema deve evitar, se possível, repetir imediatamente um filme já rejeitado.

No v0.0 essa informação pode ser temporária e não precisa ser persistida no banco.

---

# 12. Disponibilidade em streaming

Uma das funcionalidades diferenciais do produto será informar onde o filme está disponível na região configurada pelo usuário.

A aplicação deve diferenciar, quando os dados externos permitirem:

- incluído em assinatura;
- gratuito;
- gratuito com anúncios;
- aluguel;
- compra.

Exemplo:

```text
Disponível no Brasil

Incluído na assinatura
- Prime Video
- MUBI

Aluguel
- Apple TV
```

---

## 12.1 Região

O país deve ser uma preferência persistida do usuário.

Exemplo:

```text
streaming_region = "BR"
```

O MVP não precisa detectar localização automaticamente.

O usuário deve poder selecionar sua região.

---

## 12.2 Regra de interface

Evitar promessas absolutas como:

```text
Disponível com certeza no Prime Video
```

Preferir algo como:

```text
Disponibilidade indicada para Brasil
```

Os catálogos de streaming são dados externos e podem mudar.

---

# 13. Fonte de dados externa

A primeira integração planejada é o **TMDb**.

Responsabilidades esperadas da integração:

- pesquisa de filmes;
- dados de catálogo;
- gêneros;
- nota média;
- quantidade de votos;
- poster;
- sinopse;
- descoberta de candidatos;
- disponibilidade regional de streaming.

O produto não deve manter uma cópia completa do catálogo mundial de filmes no banco local.

O banco local deve armazenar apenas os dados necessários para o domínio da aplicação.

---

# 14. Estratégia de persistência

O sistema deve distinguir claramente:

```text
dados externos
vs.
dados do usuário
```

## Dados externos

Exemplos:

- título;
- poster;
- nota;
- sinopse;
- gênero;
- disponibilidade.

Fonte principal:

```text
TMDb
```

Esses dados podem ser consultados sob demanda.

---

## Dados locais

Exemplos:

- usuários;
- filmes assistidos;
- região;
- histórico mínimo de interação.

Esses dados pertencem à aplicação.

---

# 15. Modelo conceitual inicial

O modelo ainda deve ser refinado antes da implementação.

Uma versão mínima poderia conter:

```text
User
    id
    email
    password_hash
    streaming_region
    created_at
```

```text
WatchedMovie
    id
    user_id
    external_movie_id
    watched_at
```

Onde:

```text
external_movie_id
```

é o identificador do filme na fonte externa.

A necessidade de uma entidade local `Movie` deve ser avaliada durante a modelagem lógica.

---

# 16. Entidades candidatas pós-MVP

Não implementar sem necessidade real.

## MovieInteraction

Poderia futuramente representar:

```text
WATCHED
WANT_TO_WATCH
NOT_INTERESTED
```

---

## Recommendation

Poderia armazenar:

- filme sugerido;
- usuário;
- data;
- filtros usados;
- aceito/rejeitado.

---

## UserStreamingService

Poderia representar quais serviços o usuário assina.

Exemplo:

```text
Netflix
Prime Video
Max
MUBI
```

Isso permitiria um modo:

> **mostrar apenas filmes que posso assistir usando minhas assinaturas atuais.**

---

# 17. Funcionalidades explicitamente fora do MVP v0.0

Não implementar nesta versão:

- avaliação pessoal de filmes;
- reviews;
- comentários;
- seguidores;
- feed social;
- listas públicas;
- ranking entre usuários;
- machine learning;
- embeddings;
- LLM para recomendações;
- importação automática do Letterboxd;
- integração direta com IMDb;
- deep links perfeitos para todos os streamings;
- pagamentos;
- notificações;
- app mobile nativo;
- recomendação colaborativa;
- algoritmo sofisticado de perfil;
- múltiplos perfis por conta;
- detecção automática de país por IP.

---

# 18. Funcionalidades candidatas para versões futuras

## v0.1

- filtro por duração;
- filtros por década/ano;
- serviços de streaming favoritos;
- “somente no que eu assino”;
- prevenção persistente de recomendações rejeitadas.

## v0.2

- watchlist;
- “não tenho interesse”;
- rating pessoal simples;
- importação CSV do Letterboxd.

## v0.3

- recomendação ponderada;
- preferências aprendidas;
- peso por gênero;
- peso por avaliação;
- histórico de recomendações.

## v1.0

Somente definir após validar o uso real do fluxo principal.

---

# 19. Telas mínimas

## 19.1 Login

```text
E-mail
Senha

[ Entrar ]
```

---

## 19.2 Cadastro

```text
E-mail
Senha
Região de streaming

[ Criar conta ]
```

---

## 19.3 Home / O que assistir?

Tela principal.

Componentes:

- ação rápida;
- gênero opcional;
- nota mínima opcional;
- botão de escolha.

Exemplo:

```text
O que assistir hoje?

Gênero
[ Qualquer ]

Avaliação mínima
[ Qualquer ]

[ Escolher por mim ]
```

---

## 19.4 Resultado

Exibe:

- filme;
- dados principais;
- sinopse;
- disponibilidade;
- aceitar;
- sortear outro.

---

## 19.5 Filmes assistidos

Permite:

- pesquisar;
- marcar;
- visualizar;
- remover marcação.

---

## 19.6 Configurações

No v0.0:

- região de streaming.

---

# 20. Fluxos essenciais

## Fluxo A — registrar filme assistido

```text
Login
 ↓
Buscar filme
 ↓
Selecionar resultado correto
 ↓
Marcar “Já assisti”
 ↓
Persistir
```

---

## Fluxo B — escolher sem filtros

```text
Home
 ↓
Escolher por mim
 ↓
Buscar candidatos
 ↓
Excluir assistidos
 ↓
Selecionar filme
 ↓
Mostrar resultado
 ↓
Mostrar disponibilidade
```

---

## Fluxo C — escolher com filtros

```text
Home
 ↓
Selecionar gênero
 ↓
Selecionar nota mínima
 ↓
Escolher
 ↓
Aplicar filtros
 ↓
Excluir assistidos
 ↓
Selecionar candidato
 ↓
Mostrar resultado
```

---

## Fluxo D — rejeitar recomendação

```text
Resultado
 ↓
Escolher outro
 ↓
Evitar repetir candidato atual
 ↓
Selecionar novo filme
```

---

# 21. Regras de negócio iniciais

1. Um filme assistido não pode ser recomendado ao mesmo usuário.
2. A região de streaming pertence às preferências do usuário.
3. Idioma e região de streaming são conceitos independentes.
4. Uma recomendação só pode usar filmes considerados elegíveis.
5. Aceitar uma recomendação não significa automaticamente que o filme foi assistido.
6. O sistema deve evitar repetir imediatamente um filme rejeitado na mesma sessão.
7. Dados externos não devem ser tratados como verdade permanente.
8. A aplicação deve separar dados locais do usuário de dados do catálogo externo.
9. A ausência de disponibilidade conhecida não deve ser interpretada como certeza de indisponibilidade.
10. Filtros são opcionais; o produto deve funcionar bem sem configuração.

---

# 22. Critérios de aceite do MVP v0.0

O MVP pode ser considerado concluído quando um usuário conseguir:

- [ ] criar conta;
- [ ] fazer login;
- [ ] selecionar sua região;
- [ ] pesquisar filmes;
- [ ] marcar filmes como assistidos;
- [ ] visualizar seus filmes assistidos;
- [ ] remover uma marcação incorreta;
- [ ] pedir uma sugestão sem filtros;
- [ ] filtrar por gênero;
- [ ] filtrar por nota mínima;
- [ ] receber somente filmes não assistidos;
- [ ] visualizar informações básicas do filme;
- [ ] visualizar disponibilidade regional quando houver dados;
- [ ] pedir outro filme;
- [ ] utilizar o fluxo completo sem intervenção manual no banco.

---

# 23. Objetivos de aprendizado do projeto

Este projeto existe também como laboratório de desenvolvimento.

Os principais tópicos de estudo são:

## Backend

- HTTP;
- REST;
- autenticação;
- autorização;
- hash de senha;
- banco relacional;
- modelagem de dados;
- migrations;
- integração com API externa;
- tratamento de erros;
- paginação;
- caching;
- testes.

## Frontend

- formulários;
- busca/autocomplete;
- componentes;
- estados de loading;
- estados de erro;
- estados vazios;
- cards;
- filtros;
- responsividade;
- hierarquia visual;
- feedback ao usuário.

## Produto

- definição de MVP;
- redução de escopo;
- fluxo principal;
- decisões de UX;
- defaults;
- priorização;
- evolução baseada em necessidade.

## Algoritmos

- filtragem;
- aleatoriedade;
- amostragem;
- ranking;
- ponderação futura.

---

# 24. Regra de desenvolvimento com agentes de código

O projeto também deve servir como prática de programação consciente.

### Princípio

> **Delegar trabalho mecânico não significa delegar entendimento.**

Durante o desenvolvimento:

- decisões de domínio devem ser feitas conscientemente;
- decisões de modelagem devem ser compreendidas antes da geração de código;
- código gerado deve ser revisado;
- nenhuma abstração importante deve permanecer “mágica”;
- funcionalidades novas devem ser implementadas manualmente ao menos até que o padrão esteja compreendido;
- tarefas repetitivas já dominadas podem ser progressivamente delegadas.

---

# 25. Ordem sugerida de implementação

```text
1. Refinar modelo conceitual
2. Criar modelo lógico
3. Definir banco
4. Criar projeto backend
5. Implementar User
6. Implementar autenticação
7. Implementar integração de busca de filmes
8. Implementar filmes assistidos
9. Implementar endpoint de candidatos
10. Implementar algoritmo de seleção
11. Implementar disponibilidade regional
12. Criar frontend mínimo
13. Integrar frontend/backend
14. Implementar estados de erro/loading
15. Criar testes do fluxo principal
16. Refinar UX
```

---

# 26. Perguntas ainda em aberto

Estas decisões não precisam ser resolvidas imediatamente.

### Produto

- Qual deve ser o nome definitivo?
- Quantos votos mínimos um filme deve possuir?
- Qual deve ser a nota mínima padrão?
- Deve existir algum limite de ano no modo rápido?
- Curtas devem participar?
- Documentários devem participar por padrão?
- Filmes sem disponibilidade conhecida podem ser recomendados?
- O usuário deve escolher um ou receber três opções?

### Dados

- Vale criar uma tabela local `Movie` ou somente armazenar IDs externos?
- Deve haver cache de informações externas?
- Por quanto tempo dados de disponibilidade devem ser considerados válidos?

### Recomendação

- Sorteio uniforme é suficiente no começo?
- Deve haver pesos por popularidade?
- Deve haver peso por nota?
- Deve existir alguma forma de diversidade entre recomendações consecutivas?

### UX

- Resultado único ou três alternativas?
- Filtros expostos ou escondidos em “mais opções”?
- Qual deve ser a ação principal da tela inicial?
- A disponibilidade deve influenciar a escolha ou apenas ser exibida depois?

---

# 27. Definição de sucesso da versão 0.0

A versão 0.0 não precisa ser comercialmente competitiva.

Ela será bem-sucedida se:

1. o fluxo principal estiver completo;
2. o usuário conseguir chegar de “não sei o que assistir” a um filme elegível;
3. filmes assistidos forem corretamente excluídos;
4. a disponibilidade regional agregar valor;
5. o projeto servir como prática real de backend, frontend, banco, APIs e design de produto;
6. a base estiver simples o suficiente para evoluir sem reescrita imediata.

---

# 28. Resumo do MVP

```text
Usuário
  ↓
registra filmes já vistos
  ↓
escolhe filtros opcionais
  ↓
sistema consulta catálogo
  ↓
remove títulos assistidos
  ↓
aplica critérios mínimos
  ↓
seleciona um filme
  ↓
mostra informações
  ↓
mostra disponibilidade regional
  ↓
usuário aceita ou pede outro
```

### Essência do produto

> **Menos tempo escolhendo. Mais tempo assistindo.**

---

**Status:** definição inicial do MVP v0.0  
**Data:** setembro de 2026  
**Natureza:** projeto pessoal de estudo e experimentação
