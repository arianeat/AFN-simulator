## Simulação de um Autômato Finito Não-determinístico (AFNs)
</br>


O programa deve receber como entrada um arquivo contendo a descriçãao do AFN no seguinte formato:

</br>


    alfabeto=a,b,c,d    # Lista de símbolos do alfabeto aceito pelo autômato 
    estados=q0,q1,q2    # Lista de estados no autômato
    inicial=q0          # Indica qual é o estado inicial
    finais=q1,q2        # Especifica os estados finais do autômato 
    transicoes 
    q0,q1,a             # Representa uma transiçãao de q0 para q1 com o símbolo "a" 
    q1,q2,epsilon       # Transiçãao de cadeia vazia de q1 para q2 
    ...
