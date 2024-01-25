# Charmm-gui

https://charmm-gui.org/?doc=tutorial&project=membrane

## 1°- Passo
No site:
	-->*Input Generator*
	-->Membrane Builder-->Bilayer Builder

## 2°- Passo
Seleciona "Protein/Membrane System"  e coloca o pept em .pdb
-->**NEXT STEP**

## 3°- Passo
PDB info vai mostrar as informações do arquivo passado
-->**NEXT STEP**

## 4°- Passo
Selecione "Protonation state" e adicione "Protonation" para os átomos necessários
-->**NEXT STEP**

## 5°- Passo
* Step1:
	* Orientation Options:
		* Align the First Principal Axis Along Z
	* Positioning Options:
		* Rotate Molecule respect to the Y axis(90° | Pode trocar se necessário)
		* Translate Molecule along Z axis(35-40 Angstrom)
-->**NEXT STEP**

## 6°- Passo
* Step2:
	*  **Heterogeneous Lipid**
		* 1- Box type--> Rectangular
		* 2- Mexer na água quando o sistema estiver mto pesado
		* Length of X and Y: 75 Angstrom

Ver qual a proporção de lipídios para o que vc for simular. Para fungo ergosterol upper:30 e lower:30 e POPC upper:70 e lower:70.

Clique em "Show the system info"
-->**NEXT STEP**

## 7°- Passo
* Step3:
	* Basic Ion Types--> NaCl e remover Kcl, clicar em em "add Simple Ion type" para adicionar o NaCl
-->**NEXT STEP**

## 8°- Passo
-->**NEXT STEP**

## 9°- Passo
* Step3:
-->**NEXT STEP**

## 10°- Passo
* Step5:
	* Force Field Options:
		* CHARMM36m
	* Input Generation Options:
		* GROMACS
	* Equilibration Options:
		* NPT ensemble
		* Temperature: 310
-->**NEXT STEP**

## 11°- Passo
Baixar o arquivo .tgz
