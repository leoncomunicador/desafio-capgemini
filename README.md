# DESAFIO DE PROGRAMAÇÃO - ACADEMIA CAPGEMINI 
LINGUAGEM UTILIZADA: PYTHON

## Atividades desenvolvidas:

 - [ ] Requisito 1 - A mediana de uma lista de números é basicamente o elemento que se encontra no meio da lista após a ordenação. Dada uma lista de números com um número ímpar de elementos, desenvolva um algoritmo que encontre a mediana.
   
	Exemplo:

	  Entrada:
    
    arr = [9, 2, 1, 4, 6]
    
    Saída:
    
    4

 - [ ] Requisito 2 - Dado um vetor de inteiros n e um inteiro qualquer x. Construa um algoritmo que determine o número de elementos pares do vetor que tem uma diferença igual ao valor de x.

	Exemplo:

	Entrada:

	n = [1, 5, 3, 4, 2]

	Saída:

	3

	Explicação:

	Existem 3 pares de inteiros no vetor com uma diferença de 2: [5, 3], [4, 2] e [3, 1].
	
 - [ ] Requisito 3 -   Um texto precisa ser encriptado usando o seguinte esquema. Primeiro, os espaços são removidos do 		texto. Então, os caracteres são escritos em um grid, no qual as linhas e colunas tem as seguintes regras:

	![](https://www.google.com/chart?cht=tx&chf=bg,s,FFFFFF00&chco=000000&chl=%5Csqrt%7BT%7D)<=linha<=coluna<=![](https://www.google.com/chart?cht=tx&chf=bg,s,FFFFFF00&chco=000000&chl=%5Csqrt%7BT%7D)
   
   -   Considere T, como o tamanho do texto.
   -   Se certifique de que linhas x colunas >=  ![](https://www.google.com/chart?cht=tx&chf=bg,s,FFFFFF00&chco=000000&chl=T).
   -   Se múltiplos grids satisfazem as condições, escolha aquele com a menor área.
       Escreva um algoritmo que ao receber uma string s, mostre a mensagem    encriptada de acordo com as regras descritas.

	Exemplos:

	Exemplo 1)

    Entrada:
    
    s = tenha um bom dia
    
    Saída:
    
    taoa eum nmd hbi

	Explicação:

	Depois de remover os espaços, a string tem 13 caracteres. 	![](https://www.google.com/chart?cht=tx&chf=bg,s,FFFFFF00&chco=000000&chl=%5Csqrt%7B13%7D) está entre 3 e 4, então a string é rescrita na forma de um grid com 4 linhas e 4 colunas:

    tenh  
    aumb  
    omdi  
    a

	O resultado é obtido ao mostrar os caracteres de cada coluna, com um espaço entre as colunas de texto. A mensagem encriptada é obtida ao mostrar os caracteres de cada linha com um espaço entre as colunas.

	Exemplo 2)

	Entrada:

    s = ola mundo
    
    Saída:
    
    omd luo an

	Explicação:

	Depois de remover os espaços a string tem 8 caracteres. ![](https://www.google.com/chart?cht=tx&chf=bg,s,FFFFFF00&chco=000000&chl=%5Csqrt%7B8%7D) está entre 2 e 3, então a string é reescrita na forma de um grid com 3 linhas e 3 colunas:

    ola
    
    mun
    
    do

## Clonando o projeto  
  
Abra o terminal de sua máquina

> Caso queira use um dos atalhos abaixo de acordo com o seu sistema
> operacional
>  - *Linux*: Ctrl+Alt+T
>  - *MacOS*: COMMAND + ESPAÇO
>  - *Windows*: Tecla do Windows + R

e digite o comando abaixo para clonar o projeto.  
  
  
`git clone git@github.com:leoncomunicador/desafio-capgemini.git`
   
  
  
### Para acessar o desafio:

Após o clone digite:  
  
  
`cd desafio-capgemini`
  
  
  
### Instalando as dependências  
  
**IMPORTANTÍSSIMO:** Lembre-se de primeiro  **criar e ativar o ambiente virtual**, além de também instalar as dependências do projeto. Isso pode ser feito através dos comandos:

    $ python3 -m venv .venv
    
    $ source .venv/bin/activate
    
    $ python3 -m pip install -r dev-requirements.txt

O arquivo  `requirements.txt`  contém todos as dependências que serão utilizadas no desafio.
  
  
### Executando o desafio  
  
  Acesse a pasta challenges, como no exemplo:

     user@user-Lenovo-ideapad-330-15IKB:~/desafio-capgemini$ cd challenges/

Para executar os desafios basta rodar diratamente no terminal  o comando:

    $ python3 desafio1.py
    $ python3 desafio2.py
    $ python3 desafio3.py
  
  Os códigos podem ser visualizados em qualquer Editor de Texto, como por exemplo o VSCode.
 
  ### Executando os testes 

# Importante:
Antes de rodar os testes execute o comando:
pip install more-itertools (necessário para garantir que vai rodar o teste 3)

Para rodar os testes , você deve estar na pasta raiz, e executar os arquivos conforme os exemplos abaixo:

- Teste desfio 1
 
`user@user-Lenovo-ideapad-330-15IKB:~/desafio-capgemini$ python3 -m pytest tests/desafio1_test.py`

- Teste desafio 2

`user@user-Lenovo-ideapad-330-15IKB:~/desafio-capgemini$ python3 -m pytest tests/desafio2_test.py`

- Teste desafio 3

`user@user-Lenovo-ideapad-330-15IKB:~/desafio-capgemini$ python3 -m pytest tests/desafio3_test.py`

