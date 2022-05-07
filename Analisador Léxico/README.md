# Análise Léxica

O analisador léxico é o primeiro passo do "front-end" de compiladores e sua principal função é transformar uma sequência de caracteres sem nenhum significado em uma sequência de tokens. Por exemplo, a seguinte sequência:

~~~C
int x = 20 + 50;
~~~

Irá gerar os seguintes tokens: *int*, *x*, *=*, *20* , *+* , *50* , *;*

<br/>

### Divisão de etapas
Geralmente a análise léxica é dividida em 2 principais etapas:

1. **Escandimento:** Essa é a etapa na qual uma simples varredura no código irá remover os comentários e espaços em branco desnecessários.
2. **Análise Léxica:** Nessa etapa ocorre a análise léxica propriamente dita, onde o texto será quebrado em lexemas e tokens.
>Lexema: é uma sequência de caracteres reconhecidos por um padrão. Token: é um par constituído de um nome e um valor de atributo opcional. [1](https://johnidm.gitbooks.io/compiladores-para-humanos/content/part1/lexical-analysis.html)

<br/>

### Tokens

Os tokens são símbolos léxicos reconhecidos por meio de um padrão. Geralmente tokens na análise léxica possuem a seguinte estrutura:

~~~
    <nome-do-token, valor-atributo>
~~~
Onde o *nome-do-token* corresponde a uma classificação do token, por exemplo: numero, identificador, const. E o *valor-atributo* corresponde a um valor qualquer que pode ser atribuído ao token.
#### Divisão dos tokens
Há dois tipos de tokens em uma análise léxica:

1. **Tokens simples:** são tokens que não têm valor associado pois a classe do token já a descreve. Exemplo: palavras reservadas, operadores, delimitadores. Nesse caso o *valor-atributo* fica vazio.
    
    ~~~
        <if,> <*,> <for,> <while,>
    ~~~
2. **Tokens com argumento:** são tokens que têm valor associado e corresponde a elementos da linguagem definidos pelo programador. Exemplo: identificadores, constantes numéricas.
    ~~~
       <id, 5> <numero, 26> <literal, "Teste"> 
    ~~~