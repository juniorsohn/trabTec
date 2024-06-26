Este é um projeto desenvolvido como parte de um trabalho prático da disciplina de Teoria da Computação (TEC). O objetivo deste projeto é implementar um conversor de Máquina de Fita Duplamente Infinita (MTFDI) para Máquina de Fita Semi-infinita (MTFSI), permitindo assim a conversão entre esses dois modelos de máquinas de Turing.

Para executá-lo, clone o repositório em sua máquina local:
```
git clone https://github.com/juniorsohn/trabTec
```

**ALTERNATIVAMENTE**, você pode simplesmente utilizar o arquivo comprimido ``TrabTecGilson.tar.gz`` para execução e retorná-lo à sua forma original utilizando:

```
tar -xzvf trabTecGilson.tar.gz
```

Navegue até o diretório criado e lá dentro, rode a aplicação com:
```
python3 main.py
```

Para alterar entradas a serem processadas, navegue até a linha ``298`` do código:
```
with open("SeuNomeDeArquivo.extensão", "r") as arquivo_in:
```
E faça a modificação necessária. Vale ressaltar que o arquivo de entrada, se não for uma das três já incluídas no repositório, precisa estar no mesmo diretório que o código fonte.

Ao final da execução, o código irá gerar um arquivo ``output.txt``, contendo uma aplicação modificada para execução no simulador https://morphett.info/turing/turing.html. Basta colar o conteúdo do arquivo ``output.txt`` na caixa do simulador e executar.

PS: É possível que o simulador reclame sobre estados duplicados no programa resultante da aplicação. Isso não é um problema pois não há não-determinismo, são apenas linhas replicadas que fazem exatamente a mesma coisa. É um bugzinho menor que não interfere na execução da aplicação, só gera umas linhas extras.

**IMPORTANTE: O ARQUIVO DE ENTRADA NÃO DEVE CONTER LINHAS VAZIAS! SE NÃO, É POSSÍVEL (E PROVÁVEL) QUE OCORRA OUT OF INDEX ERROR NO CÓDIGO!**
