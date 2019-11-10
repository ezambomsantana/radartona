Radartona 2019 - InterSCity team 
===================================================

Desafio Radares x Acidentes

Para relacionar radares com acidentes, o grupo desenvolveu um sistema Web para visualizar as posições de todos os radares da cidade de São Paulo e os acidentes de Fevereiro de 2016, 2017, 2018 e 2019. Esse sistema permite a filtragem dos acidentes por ano ou a exibição de todos os acidentes.

Os radares são exibidos com um buffer de 100 metros para mostrar os acidentes que aconteceram próximo a um radar específico. Outra funcionalidade é ao usuário clicar em um radar, dados sobre esse radar são exibidos como o número de autuações e a contagem de veículos. (Atualmente só está funcionando o número de autuações)

A imagem a seguir mostra a interface da aplicação.

![Interface da Aplicação](images/interface.png)


---------------------------------------------------
Python modules and dependencies
---------------------------------------------------
- psycopg2
- flask
- flask_restful
- unidecode
- utm

- postgresql DB



---------------------------------------------------
Data
---------------------------------------------------

---------------------------------------------------
Mortos e feridos 2011-2018
---------------------------------------------------

Arquivos originais 2011-2018:
- Bases ACIDENTES, VÍTIMAS e VEÍCULOS. Coluna comum: ID_ACIDENTE
- Base de RUAS X CODLOGS (endereços)

Arquivos processados 2011-2018 (dados padronizados e juntados):
- Base ACIDENTES - 2011-2018_Acidentes.csv.xz *
- Base VEÍCULOS - 2011-2018_Veiculos.csv.xz
- Base VÍTIMAS - 2011-2018_Vitimas.csv.xz

Base ACIDENTES - *Colunas extras adicionadas, não constantes no arquivo original:
- area40 - marcação de ponto em área de velocidade reduzida
- area40_tipo - tipo da área de velocidade reduzida
- agg_auto - veículos agregados: carros
- agg_bicicleta - veículos agregados: bicicletas
- agg_moto - veículos agregados: motos
- agg_onibus - veículos agregados: ônibus
- agg_caminhao - veículos agregados: caminhões
- agg_demais_veic - veículos agregados: outros
- agg_seminfo - veículos agregados: sem informação
- categoria - Veículos motorizados, Atropelamento a pedestre, Atropelamento a ciclista
- agg_categoria - (derivada de categoria)
- lat_tableau - latitude no formato para tableau
- long_tableau - longitude no formato para tableau
- lat100 - latitude no formato para tableau (cluster 100x100m)
- long100 - longitude no formato para tableau (cluster 100x100m)
- geocode - origem do geocode, pode ser MapInfo CET ou QGIS Google


Resumo do que tem nas bases:

OCORRÊNCIAS ("Acidentes" #naofoiacidente)
- Data/Hora
- Número (soma) de vítimas feridas e mortas por ocorrênia
- Veículos envolvidos
- Endereço (logradouros com numeral) + LatLong + Flag_Cruzamento (colunas extras na base processada)
- Origem da informação de Geocode (CET ou processo manual) (coluna extra na base processada)

VÍTIMAS
- Sexo
- Idade
- Escolarização
- Estado de alcoolização
- Tipo de vítima (pedestre, condutora, passageira)
- Veículo envolvido
- Classificação Morta/Ferida
- Data de óbito
- Data da ocorrência (coluna extra na base processada, no original é acessada via ID_ACIDENTE)
- Latitude, Longitude, Endereço (colunas extras na base processada)


---------------------------------------------------
Fiscalização (Painel Mobilidade Segura) 2014-2017
---------------------------------------------------

Arquivos originais 2011-2017:
- Fiscalização eletrônica 2014-2017 (já com LatLong adicionado)
- Fiscalização manual 2014-2017 (já com LatLong adicionado)

Arquivos processados 2011-2017:
- Fiscalizacao_Manual_e_Eletronica_2014-2017_PedCic_PorHora.csv
- PainelMobilidadeSegura_2014-2017_Cluster100Tableau.csv.xz
- PainelMobilidadeSegura_2014-2017_Cluster100Tableau_PedCic.csv.xz


Resumo do que tem nas bases:
- Data/Hora
- Departamento que registrou a infração
- Identificador do veículo infrator
- Enquadramento da infração
- Quantidade de infrações registradas
- Endereço
- Latitude, Longitude (colunas extras na base processada)
- Origem da informação de Geocode (fiscalização eletrônica, coluna extra na base processada)


Fiscalizacao_Manual_e_Eletronica_2014-2017_PedCic_PorHora.csv
- União da fiscalização manual + eletrônica com seleção de fiscalização que protege ciclistas e pedestres
- LatLong da fiscalização manual está agrupada em clusters de 100x100m
- LatLong está no formato Tableau (separador do float é uma vírgula)

PainelMobilidadeSegura_2014-2017_Cluster100Tableau.csv.xz
- Todas as fiscalizações manuais
- LatLong da fiscalização manual está agrupada em clusters de 100x100m
- LatLong está no formato Tableau (separador do float é uma vírgula)

PainelMobilidadeSegura_2014-2017_Cluster100Tableau_PedCic.csv.xz
- Seleção da base acima só com fiscalização manual que protege ciclistas e pedestres
- LatLong da fiscalização manual está agrupada em clusters de 100x100m
- LatLong está no formato Tableau (separador do float é uma vírgula)


---------------------------------------------------
Relatório Volumes e Velocidades 2011-2017
---------------------------------------------------

Arquivos originais 2011-2017

Resumo do que tem nas bases:

VELOCIDADES (Não é base, mas um Excel)
- Data
- Trecho percorrido pela medição (fluxo e contrafluxo)
- Período (manhã ou tarde)
- Velocidade média
- Tempo médio do trajeto

VOLUMES
- Data
- Trecho percorrido pela medição (fluxo e contrafluxo)
- Período (manhã ou tarde)
- Hora (intervalos de 15min)
- Veículos contados



SMDU - Secretaria Mun. de Desenvolvimento Urbano
===================================================

---------------------------------------------------
Shapefiles - Calçadas de São Paulo 2016
---------------------------------------------------

Arquivos originais 2016

- Largura das calçadas de São Paulo 2016



SMS - Secretaria Municipal de Saúde
===================================================

---------------------------------------------------
SAMU - Ambulâncias 2011-2017
---------------------------------------------------

Arquivos originais 2011-2017

Resumo do que tem nas bases:
- Datas de abertura e fechamento do chamado
- Prioridade de atendimento (protocolo Medical Priority Dispatch System)
- Tipo e subtipo do atendimento (protocolo Medical Priority Dispatch System)
- Escala Glasgow sobre gravidade das ocorrências
- Respiração por minuto
- Idade paciente
- Sexo paciente
- Estabelecimento para onde ambulância levou paciente
- Subprefeitura do atendimento
- Endereço do atendimento (sem número e sem LatLong)


---------------------------------------------------
SIVVA - At. ambulatoriais e hospitalares 2011-2017
---------------------------------------------------

Arquivos originais 2011-2017

Resumo do que tem nas bases:
- Data da ocorrência
- Data de atendimento
- Faixa etária da vítima (diferentes categorizações)
- Escolaridade
- Sexo da vítima
- Data de nascimento
- Raça/Cor
- Flag gravidez
- Estado de alcoolismo
- Estado de uso de drogas
- Diagnóstico da lesão (CID10)
- Evolução do atendimento (alta, óbito etc)
- Tipo de vítima (pedestre, ocupante de veículo)
- Tipo de veículo envolvido
- Flag pessoa portadora de deficiência
- Flag encaminhamento para hospital



SMT - Secretaria Mun. de Mobilidade e Transportes
===================================================

---------------------------------------------------
Shapefiles - Plano Municipal de Mobilidade 2015
---------------------------------------------------

Arquivos originais 2015

- Rede cicloviária prevista até 2030
- Corredores de ônibus previstos até 2030
- Terminais de ônibus previstos
- Redes de ônibus previstas
- Garagens de ônibus previstas


---------------------------------------------------
Shapefiles - Plano de Metas 2017 (rede cicloviária)
---------------------------------------------------

Arquivos originais 2017

- Rede cicloviária existente em 2017 (Arquivo Geosampa), categorizada entre conectada/desconectada



SMIT - Secretaria Mun. de Inovação e Tecnologia
===================================================

---------------------------------------------------
SP156 - SAC da Prefeitura
---------------------------------------------------

Arquivos originais 2015-2018S1 (versão Julho/2018)

Arquivos processados 2015-2018S1:
- Dados_SP156_2015-2018s1_Integral.csv.xz
- SP156_Microdados_ReclamacoesOnibus_SPTrans.csv.xz

Para versões atualizadas, baixe do link: 
http://dados.prefeitura.sp.gov.br/dataset/dados-do-sp156.

Temas relacionados a Mobilidade estão em:
- 'Transporte'
- 'Acessibilidade'
- 'Trânsito'
- 'SAC/GRC'


SP156_Microdados_ReclamacoesOnibus_SPTrans.csv.xz
Microdados relacionados a reclamações de ônibus, retirados de uma coluna-depósito
onde há diversas informações. Dentre elas, é possível ver as linhas e prefixos dos ônibus



SPTRANS - São Paulo Transportes SA
===================================================

---------------------------------------------------
RESAM - Multas a empresas de ônibus
---------------------------------------------------

Arquivos originais 2011-2017
Arquivos processados 2015-2017 (arquivos .csv sem logomarca SPTrans)

Resumo do que tem nas bases:
- Data/hora
- Valor da multa aplicada
- Flag Reincidência
- Código do Resam (infração)
- Descrição da infração
- Linha de ônibus da infração
- Operadora/empresa de ônibus

Alguma seleção de códigos relacionados à segurança de pedestres e ciclistas

- M48 - Motorista fazendo uso em trânsito celular
- GR37 - Conduzir o veículo comprometendo a segurança de usuários ou terceiros
- GR46 - Trafegar acima do limite de velocidade permitido
- G51 - Parar afastado do meio fio, obrigando desembarque na pista
- G21 - Não trafegar por faixas/corredores exclusivos
- G56 - Tacógrafo inoperante ou inexistente
- M45 - Velocidade incompatível com a segurança em locais com grande fluxo de pessoas





SUS - Sistema Único de Saúde
===================================================

---------------------------------------------------
SIH - Internações hospitais (Transportes) 2011-2017 
---------------------------------------------------

A base do SIH é atualizada mensalmente. Download deve ser feito neste link: 
datasus.saude.gov.br/informacoes-de-saude/servicos2/transferencia-de-arquivos

Arquivos processados 2011-2017:
- SIH-SUS-CID10-V01-V89_2011-2017.xlsx.xz

Resumo do que tem nas bases:
- Data de nascimento, idade
- Sexo
- Raça/Cor
- Etnia
- Código municipal de residência
- Diárias de internação
- Diárias de acompanhante
- Diárias de UTI
- Valor da internação
- Data de saída
- Diagnóstico (segundo categorização CID10)
- Flag morte
- Nacionalidade
- CNPJ Mantendedor da instituição
- CID10 relacionada a transporte terrestre (coluna extra na base processada)
- Categorização de vítima segundo CID10 (pedestre, ciclista etc) (coluna extra na base processada)


SIH-SUS-CID10-V01-V89_2011-2017.xlsx.xz
- Seleção voltada para acidentes de transportes terrestres (V01-V89 da CID10)
- União dos anos 2011 a 2017
- Base integral de origem baixada em Agosto de 2018

---------------------------------------------------
SIM - Mortes (Transportes) 2011-2016*
---------------------------------------------------

*Ano 2017 ainda não disponível

A base do SIH é atualizada mensalmente. Download deve ser feito neste link: 
datasus.saude.gov.br/informacoes-de-saude/servicos2/transferencia-de-arquivos

Arquivos processados 2011-2016:
- SIM-SUS-CID10-V01-V89_2011-2016.xls.xz

Resumo do que tem nas bases:
- Data de nascimento, idade
- Sexo
- Raça/Cor
- Escolaridade
- Estado civil
- Ocupação
- Data/Hora de óbito
- Local da morte
- Código municipal de residência
- Flag Necropsia
- Causa da morte segundo CID10
- Acidente de trabalho
