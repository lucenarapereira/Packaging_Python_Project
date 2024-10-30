O CLAHE (Contrast Limited Adaptive Histogram Equalization) é uma técnica de processamento de imagens usada para melhorar o contraste, especialmente em áreas muito claras ou escuras, e é uma extensão do AHE (Adaptive Histogram Equalization). O CLAHE é amplamente utilizado em áreas de visão computacional e análise de imagens médicas, onde o ajuste de contraste detalhado em pequenas regiões é essencial.

* Conceito e Funcionamento do CLAHE
A equalização de histograma é uma técnica que redistribui os valores de intensidade (ou brilho) de uma imagem para aumentar o contraste, deixando a imagem mais equilibrada. O CLAHE vai além disso ao trabalhar em blocos menores (ou "tiles") da imagem em vez da imagem inteira. Isso permite ajustar o contraste em diferentes partes da imagem separadamente.

* Passo a Passo do Processo
- Divisão em Blocos Locais (Tiles): A imagem é dividida em blocos menores, normalmente de tamanhos como 8x8 pixels ou 16x16 pixels. Cada bloco terá sua própria equalização de histograma aplicada.

- Equalização do Histograma em Blocos: Dentro de cada bloco, o CLAHE redistribui os níveis de intensidade de forma que fiquem mais equilibrados, aumentando o contraste local.

- Limitação do Contraste (Clip Limit): Para evitar que o contraste se torne exagerado e introduza ruído (ou um efeito de "ampliação" excessiva), o CLAHE define um limite máximo para o contraste, chamado clipLimit. Esse limite restringe a intensidade do aumento de contraste para evitar artefatos.

- Interpolações nas Bordas dos Blocos: Após a equalização dos blocos, o CLAHE suaviza as transições entre eles por interpolação, mantendo a imagem uniforme e evitando que ela apresente divisões abruptas.

* Parâmetros Importantes
Clip Limit: Define o limite máximo de aumento de contraste permitido em cada bloco. Valores mais altos aumentam o contraste, enquanto valores mais baixos mantêm um efeito mais suave.
Tile Grid Size: Controla o tamanho dos blocos para a equalização. Blocos maiores tendem a tratar áreas mais amplas, enquanto blocos menores oferecem um ajuste mais detalhado e local.

* Benefícios do CLAHE
Aprimora Detalhes em Áreas Superexpostas e Subexpostas: Ideal para imagens com áreas muito claras ou escuras, como fotos em luz direta do sol ou sombras intensas.
Reduz Introdução de Ruído: O limite de contraste evita que ruído ou artefatos apareçam em áreas de baixo contraste.
Melhoria de Contraste Local: Comparado à equalização de histograma global, o CLAHE fornece melhorias mais focadas e naturais.

* Aplicações do CLAHE
Imagem Médica: Ajuda a destacar estruturas de baixo contraste em radiografias, tomografias e ressonâncias.
Visão Computacional e Segurança: Melhora a visibilidade em câmeras de segurança com iluminação variável.
Fotografia Digital: Usado para recuperar detalhes em fotos com iluminação inconsistente, como fotos em contraluz ou cenas com luz solar intensa.

O CLAHE é, portanto, uma poderosa ferramenta para ajustar o contraste, especialmente quando queremos melhorar a visibilidade em áreas específicas sem comprometer a qualidade geral da imagem.






