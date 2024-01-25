## Arquivos necessários
* ions.mdp
* minim.mdp
* nvt.mdp
* npt.mdp
* md.mdp

# Minimização
## pdb2gmx
A ferramenta pdb2gmx gera uma coordenada atômica GROMACS (.gro) a partir do arquivo .pdb de entrada.

Os outros parâmetros referem-se ao tipo de solvente (por exemplo, água: flag -water spce), carga líquida (neutra; protonação: flag: -inter), modificações nos terminais N e C (bandeira: -ter) e hidrogênio polar adição ou remoção (sinalizador: -ignh).

## editconf
Determinar a caixa. Selecione o campo de força que melhor se adapta ao tipo de macromoléculas e sistema que você deseja simular. O campo de força GROMOS96 43a é comumente utilizado para peptídeos lineares e cíclicos e, portanto, foi selecionado para a metodologia aqui descrita.

## solvate
Após preparar a caixa de simulação, proceda à resolução do sistema. Para isso, utilize o sinalizador: -solvate, seguido do sinalizador: -cp para especificar os arquivos de saída da etapa anterior (editconf). O sinalizador: -cs é usado para especificar o solvente, que será a água Simple Point Charge (SPC) usando o sinalizador: -spc216.gro. No entanto, outros co-solventes também podem ser adicionados ao sistema

O arquivo de topologia (topol.top) será atualizado constantemente a partir desta etapa, pois este arquivo contém informações sobre os tipos de moléculas e o número de moléculas

## grompp
Um arquivo de entrada adicional com extensão de arquivo de parâmetro de dinâmica molecular (.mdp) será usado para produzir um arquivo .tpr com grompp. Grompp monta parâmetros especificados do arquivo .mdp com as coordenadas e informações de topologia para gerar um arquivo .tpr

## genion

Com a descrição do sistema em nível atômico no arquivo binário ions.tpr, use o comando genion. Para adicionar os íons necessários para neutralizar a carga líquida do sistema adicionando o número correto de íons negativos (Na+) ou íons positivos (Cl-), use o sinalizador: -neutro.


## energy
para gerar o grafico de energia

***

# Equilíbrio
O equilíbrio é comumente realizado em duas etapas. O primeiro é conduzido sob um conjunto NVT (número constante de partículas, volume e temperatura).

O equilíbrio de pressão é a segunda etapa conduzida em um conjunto NPT, pois o número de partículas, a pressão e a temperatura são constantes.


***

# Simulação

Após as etapas de minimização e equilíbrio, o próximo passo é liberar as restrições de posição e executar a simulação MD. É um processo semelhante aos comandos descritos acima para NVT e NPT.
