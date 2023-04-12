# Atividade-Final-SO-Kauanne-e-Mariana
Atividade:
Vocês irão criar 2 programas cada um com três threads os quais receberão do usuário a quantidade de vezes que ele deverá rodar cada thread. Cada uma das threads deverá, executar funções que gravam nos arquivos registro1.txt e registro2.txt:
- O número da execução;
- Nome do programa; 
- Nome da thread;
- Data e horário do registro.
Em resumo, imagine que o usuário passou o valor 2, assim cada thread irá alternando entre uma e outra executar 2 vezes, registrando em cada um dos arquivos uma linha com o número da execução, nome do programa, nome dela e o horário que executou ficando cada arquivo como no exemplo a seguir, não necessariamente na mesma ordem:

REGISTRO1.TXT

1 Programa1 - Thread1 - Data:     Horário
1 Programa2 - Thread1 - Data:     Horário:
1 Programa1 - Thread2 - Data:     Horário:
1 Programa1 - Thread3 - Data:     Horário:
2 Programa1 - Thread1 - Data:     Horário
1 Programa2 - Thread2 - Data:     Horário:
2 Programa2 - Thread3 - Data:     Horário:
2 Programa2 - Thread2 - Data:     Horário:

Analisem o funcionamento dos programa, executando em separado e os dois ao mesmo tempo, se todas as threads conseguem gravar e se há alguma relação de intervalo de tempo entre os registros delas, isso variando de 5mil 10 mil 100 mil registros.

Envie seu relatório com o código no mesmo arquivo em arquivo editável aqui pelo Docs, e o programa pronto para executar.
