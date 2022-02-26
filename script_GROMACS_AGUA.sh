#!/bin/bash

# Script para fazer simulacoes em agua usando a ferramenta gromacs no Linux
# Site para tutorial de GROMACS: http://www.mdtutorials.com/gmx/

# Fazer variavel que pra pegar os nomes dos arquivos
# e criar um diretorio com o nome da sequencia, para
# todos os arquivos serem escritos la

################# Pegando o primeiro paramêtro(nome do arquivo .pdb) 
molecula=$1;

molecula_sem_extensao=${molecula%.pdb};
molecula_clean=$molecula_sem_extensao"_clean.pdb";

##### 1 - Limpar o arquivo de moleculas de HOH #####
# Usando o programa grep para realizar essa tarefa
# passando o parametro -v, ignoramos as linhas que 
# contenham HOH, assim o arquivo ARQUIVO_clean.pdb
# nao tera HOH. 

grep -v HOH $molecula > $molecula_clean;


##### 2- Preparar os arquivos para poder fazer as simulacoes #####

# Usando o parametro pdb2gmx no gromacs(gmx)
# Serao gerados 3 arquivos: 

# 1- topologia para a molecula;                             (arquivo = topol.top)
# 2- Um arquivo para restringir as posicoes da molecula;    (posre.itp)
# 3- Estrutura para o arquivo pos-processado, que           (ARQUIVO_processed.gro)
# contenha todos os atomos definidos pelo campo de forca escolhido  

# Apos executado o comando abaixo, varias opcoes de campos de forca 
# irao ser exibidos para a escolha. Escolha uma das opcoes de forca
# (o exemplo usa a de numero 15-OPLS-AA/L)  


molecula_processed=${molecula_clean%clean*}"processed.gro"

echo $molecula_processed;

echo 15 |time gmx pdb2gmx -f $molecula_clean -o $molecula_processed -water spce;

# Explicando os parametros utilizados (ex:-water spce)
# "-f"(file): Indica que sera passado um arquivo(file), apos esse parametro
# precisa-se passa o nome do arquivo a ser processado

# "-o"(output): Indica o nome do arquivo de saida, ou seja, o nome
# do arquivo que sera criado depois de processado. 

# "-water": Parametro passado ao pdb2gmx para preparar o arquivo
# para uma simulacao em agua, assim necessitando de outro parametro
# no caso "spce". Apos o parametro "-water", pode-ser passar outros
# parametros especificando o modelo de agua a ser usado; none, spc, spce,
# tip3p, tip4p, tip5p, tips3p.

# -ignh: Ignora atomos de H no arquivo pdb, util para estruturas NMR,
# caso contrario, precisa especificar como os campos de forca irao
# atuar no GROMACS


# -ter: Atribui os estados de carga para as regioes N- e C- t terminais.

# -inter:  Atribui os estados de carga para Glu, Asp, Lys, Arg, e His,
# escolha quais Cys estao envolvidas nas ligacoes dissulfeto.


##### 3- Definir a caixa e o solvente #####

# 1- Definir as dimensoes da caixa usando o editconf
# 2- Encher a caixa com agua usando o solvente.


molecula_newbox=${molecula%.pdb*}"_newbox.gro";
echo $molecula_newbox;

time gmx editconf -f $molecula_processed -o $molecula_newbox -c -d 1.0 -bt cubic;

# Parametros
# "-c": Centraliza a molecula na caixa

# "-d": Especifica a distancia das bordas(Pelo menos 1.0nm, no exemplo acima)

# "-bt" Define o tipo de caixa, pode ser: cubic, triclinic, dodecahedron, octahedron

molecula_solv=${molecula%.pdb*}"_solv.gro";
echo $molecula_solv;

time gmx solvate -cp $molecula_newbox -cs spc216.gro -o $molecula_solv -p topol.top;

# Parametros:
# "-cp": A configuracao da proteina a ser especificada, contida no arquivo
# processado anteirormente

# "-cs": Configuracao do solvente, configuracao padrao do GROMACS


##### 4- Adicionar ions #####

# grompp(GROMACS pre-processor) = processa o arquivo de coordenadas e a topologia 
# (que descreve as moléculas) para gerar uma entrada de nível 
# atômico (.tpr). O arquivo .tpr contém todos os parâmetros de 
# todos os átomos do sistema.

# genion = le a topologia e substitui as moléculas de água 
# pelos íons que o usuário especificar. A entrada é chamada de 
# arquivo de entrada de execução, que possui uma extensão de .tpr;

# AQUI O TUTORIAL USA UM ARQUIVO .mdp(molecular dynamics parameter file)
# E DISPONIBILIZA.
# IMPORTANTE: os arquivos .mdp foram feitos para serem usados
# com o campo de forca OPLS-AA


time gmx grompp -f ions.mdp -c $molecula_solv -p topol.top -o ions.tpr;

# Agora temos uma descrição em nível atômico do nosso sistema no 
# arquivo binário ions.tpr. Vamos passar este arquivo para o genion

molecula_solv_ions=${molecula%.pdb*}"_solv_ions.gro";
echo $molecula_solv_ions;

echo 13 | time gmx genion -s ions.tpr -o $molecula_solv_ions -p topol.top -pname NA -nname CL -neutral;

# Apos executada a linha acima, varias opcoes irao aparecer,
# no tutorial usa-se a opcao 13 "SOL", para incorporar os ions.

# Parametros genion:
# "-s": Para especificar uma estrutura

# "-o": Para gerar o arquivo de saida .gro

# "-p": Para colocar a topologia e o programa saber onde trocas as
# moleculas de agua por ions.

# "-pname": Dar nomes aos ions positivos

# "-nname": Dar nomes aos ions negativos

# "-neutral": Especificar o quantidade de ions apenas para neutralizar
# o sistema


##### 5- Minimizacao de energia #####

# Vamos usar o grompp para incorporar a estrutura, topologia, e parametros
# de simulacao para os arquivo binario (.tpr) 

# IMPORTANTE DE NOVO OUTRO ARQUIVO ESPECIFICO DADO PELO TUTORIAL
# (minim.mdp = http://www.mdtutorials.com/gmx/lysozyme/Files/minim.mdp)

time gmx grompp -f minim.mdp -c $molecula_solv_ions -p topol.top -o em.tpr;


# Agora podemos chamar o parametrp mdrun para iniciar a minimizacao de energia
time gmx mdrun -v -deffnm em;


# Parametros
# "-v": Imprime os passos que estao sendo realizados

# "-deffnm": Define os nomes dos arquivos de entrada e saida  
# Exemplos:
# em.log: ASCII-text log file of the EM process
# em.edr: Binary energy file
# em.trr: Binary full-precision trajectory
# em.gro: Energy-minimized structure


# Analisando o arquivo produzido em.edr
echo 10 0 | time gmx energy -f em.edr -o potential.xvg;

# Apos executar digita "10 0", 10 para selecionar o Potencial
# e 0 para encerrar a entrada. 




##### 6-1- Equilibrio #####

# A Minimizacao de Energiagarantiu que tivéssemos uma estrutura 
# inicial razoável, em termos de geometria e orientação do solvente. 
# Para começar a dinâmica real, devemos equilibrar o solvente e os 
# íons ao redor da proteína. Se tentarmos uma dinâmica desenfreada 
# neste ponto, o sistema pode entrar em colapso. A razão é que o 
# solvente é principalmente otimizado dentro de si mesmo, e não 
# necessariamente com o soluto. Ele precisa ser levado à temperatura 
# que desejamos simular e estabelecer a orientação adequada sobre o 
# soluto (a proteína). Depois de chegarmos à temperatura correta 
# (com base nas energias cinéticas), aplicaremos pressão ao sistema 
# até atingir a densidade adequada.


# O objetivo do posre.itp é aplicar uma força de restrição de posição 
# nos átomos pesados ​​da proteína (qualquer coisa que não seja um 
# hidrogênio). O movimento é permitido, mas somente depois de superar 
# uma penalidade de energia substancial. A utilidade das restrições 
# de posição é que elas nos permitem equilibrar nosso solvente em 
# torno de nossa proteína, sem a variável adicional de mudanças 
# estruturais na proteína. A origem das restrições de posição 
# (as coordenadas nas quais o potencial de restrição é zero) é 
# fornecida através de um arquivo de coordenadas passado para a 
# opção -r do grompp.


# O equilíbrio geralmente é realizado em duas fases. A primeira 
# fase é conduzida sob um conjunto NVT (Número constante de partículas, 
# Volume e Temperatura). Este conjunto também é referido como "isotérmico-isocórico" 
# ou "canônico". O prazo para tal procedimento depende do conteúdo do 
# sistema, mas no NVT, a temperatura do sistema deve atingir um platô 
# no valor desejado. Se a temperatura ainda não se estabilizou, será 
# necessário um tempo adicional. Normalmente, 50-100 ps devem ser 
# suficientes, e realizaremos um equilíbrio NVT de 100 ps para este 
# exercício.


# AQUI USA OUTRO ARQUIVO 
# .mdp(nvt.mdp = http://www.mdtutorials.com/gmx/lysozyme/Files/nvt.mdp)
time gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr;


time gmx mdrun -deffnm nvt;


# Analizando a progressao da temperatura, usando a energia.
echo 16 0 | time gmx energy -f nvt.edr -o temperatura.xvg;

# Apos a execucao da linha acima escolher "16 0", para selecionar
# a temperatura do sistema e sair.


##### 6-2- Equilibrio #####

# Os passos anteriores estabilizaram a temperatura do sistema. Agora
# precisamos estabilizar a pressao(e portanto a densidade) do sistema.

# Chamaremos grompp e mdrun assim como fizemos para o equilíbrio NVT. Observe que agora estamos 
# incluindo o sinalizador -t para incluir o arquivo de ponto de verificação do equilíbrio NVT; 
# este arquivo contém todas as variáveis de estado necessárias para continuar nossa simulação. 
# Para conservar as velocidades produzidas durante a NVT, devemos incluir este arquivo. O arquivo 
# de coordenadas (-c) é a saída final da simulação NVT.

# OUTRO ARQUIVO DADO USANDO .mdp(npt.mdp)
time gmx grompp -f npt.mdp -c nvt.gro -r nvt.gro -t nvt.cpt -p topol.top -o npt.tpr;

time gmx mdrun -deffnm npt;

#gmx mdrun -f npt.edr -o pressure.xvg;

# Analizando a progressao da pressao, usando energia
echo 18 0 | time gmx energy -f npt.edr -o pressure.xvg;

# Apos a execucao da linha acima digitar "18 0" para 
# selecionar a pressao e sair do sistema.

# Olhando para a densidade tambem, usando a energia
# digitando "24 0"
echo 24 0 | time gmx energy -f npt.edr -o density.xvg;

##### 7- Producao da Dinamica Molecular #####

# Após a conclusão das duas fases de equilíbrio, o sistema está 
# agora bem equilibrado na temperatura e pressão desejadas. Agora 
# estamos prontos para liberar as restrições de posição e executar 
# o MD de produção para coleta de dados. O processo é exatamente 
# como vimos antes, pois usaremos o arquivo de ponto de verificação 
# (que neste caso agora contém informações de acoplamento de pressão 
# preservadas) para grompp

# USA ARQUIVO .mdp(md.mdp = http://www.mdtutorials.com/gmx/lysozyme/Files/md.mdp)
time gmx grompp -f md.mdp -c npt.gro -t npt.cpt -p topol.top -o md_0_1.tpr;

# Rodar a simulacao agora
time gmx mdrun -deffnm md_0_1;


##### 8- ANALISE  #####
# Agora que simulamos nossa proteína, devemos executar algumas análises no sistema. 
# Que tipos de dados são importantes? Essa é uma pergunta importante a ser feita antes de executar 
# a simulação, portanto, você deve ter algumas ideias sobre os tipos de dados que deseja coletar 
# em seus próprios sistemas. Para este tutorial, algumas ferramentas básicas serão introduzidas.

# O primeiro é o trjconv, que é usado como uma ferramenta de pós-processamento para remover 
# coordenadas, corrigir a periodicidade ou alterar manualmente a trajetória (unidades de tempo, 
# frequência de quadros, etc). Para este exercício, usaremos trjconv para contabilizar qualquer 
# periodicidade no sistema. A proteína se difundirá através da célula unitária e pode parecer 
# "quebrada" ou "saltar" para o outro lado da caixa. Para explicar esses comportamentos, emita o 
# seguinte:

echo 1 0 | time gmx trjconv -s md_0_1.tpr -f md_0_1.xtc -o md_0_1_noPBC.xtc -pbc mol -center;
# Selecione 1 ("Proteína") como o grupo a ser centralizado e 0 ("Sistema") para saída. 
# Faremos todas as nossas análises nesta trajetória "corrigida". Vejamos primeiro a estabilidade 
# estrutural. GROMACS tem um utilitário embutido para cálculos RMSD chamado rms. Para usar rms, 
# emita este comando:


echo 4 0 | time gmx rms -s md_0_1.tpr -f md_0_1_noPBC.xtc -o rmsd.xvg -tu ns;
# Escolha 4 ("Backbone") para o ajuste de mínimos quadrados e o grupo para cálculo de RMSD. 
# O sinalizador -tu exibirá os resultados em termos de ns, mesmo que a trajetória tenha sido 
# escrita em ps. Isso é feito para clareza da saída (especialmente se você tiver uma simulação 
# longa - 1e+05 ps não parece tão bom quanto 100 ns). O gráfico de saída mostrará o RMSD em relação 
# à estrutura presente no s minimizado e equilibrado

# If we wish to calculate RMSD relative to the crystal structure, we could issue the following:

echo 4 0 | time gmx rms -s em.tpr -f md_0_1_noPBC.xtc -o rmsd_xtal.xvg -tu ns;


# O raio de giração de uma proteína é uma medida de sua compacidade. Se uma 
# proteína for dobrada de forma estável, provavelmente manterá um valor relativamente estável 
# de Rg. Se uma proteína se desdobrar, seu Rg mudará com o tempo. Vamos analisar o raio de giração 
# da lisozima em nossa simulação:

echo 1 0 | time gmx gyrate -s md_0_1.tpr -f md_0_1_noPBC.xtc -o gyrate.xvg;
# Escolha 1  para Proteina

molecula_pdb_final=${molecula%.pdb*}"_FINAL.pdb"

# LINHA PARA EDITAR CRIAR O ARQUIVO PDB
echo 1 | time gmx trjconv -s md_0_1.tpr -f md_0_1.xtc -dump 0 -o $molecula_pdb_final;

# -dump é o paramêtro que define o tempo em que irá gerar o arquivo pdb
