# London Bike Rides
London Bike Rides é meu primeiro projeto de análise de dados, onde utilizo Tableau, lib pandas do Python, Kaggle API para coleta de dados e mais. Trata-se de uma database que contém diversos dados de condições climáticas, horários e mais de pessoas que fizeram passeios de bicicleta em Londres. O Tableau traz vida à base de dados, com muita interação e melhor entendimento das informações.

Acesse o site interativo através do link: https://public.tableau.com/app/profile/victor.souza6834/viz/LondonBike_17239439951150/Dashboard1?publish=yes

## Explicações

Kaggle é uma ótima ferramenta para obter dados utilizáveis em projetos pessoais. Nele, obtive uma base de dados em forma de planilha .csv, na qual manipulei as colunas e determinados conteúdos para melhor entendimento visual. Além disso, no mesmo arquivo 'london_bikes.py' também há alguns outros métodos que utilizei para entender melhor a lib pandas.

## No Tableau
Através do link indicado no início, a imagem a seguir será a tela inicial do site:

![image](https://github.com/user-attachments/assets/ebf654ef-2a5d-4da3-a9c5-9d40eda29199)

Veja que há um gráfico no canto superior direito. Este gráfico é o personagem principal deste projeto. Selecione o intervalo de tempo de tempo desejado clicando e arrastando sobre o trecho que desejar. Perceba que, logo após a seleção, a quantidade total de passeios no período selecionado é atualizada logo à esquerda do gráfico.

Depois, digite o período de tempo que deseja analisar (moving average duration/period) e serão definidos os pontos do gráfico.

Passando sobre gráfico com o ponteiro do mouse, veremos informações adicionais:

![image](https://github.com/user-attachments/assets/3cf63bce-c3e4-4785-bf3d-8effc66aa083)

Supondo 10 dias de Moving Average Period, temos informações dos últimos 10 dias (contando o atual) da média de passeios diários de bicicleta, além das condições climáticas e a quantidade de passeios dividida por horários.

Também há, logo abaixo, uma tabela que informa a temperatura e velocidade do vento no período, além das informações adicionais ao passar o mouse.
