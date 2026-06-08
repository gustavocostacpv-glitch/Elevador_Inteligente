def simular_elevador(chamadas, estrategia):
    andar_atual = 0
    total_deslocamentos = 0
    tempo_total = 0
    ordem_atendimento = []
    
    print(f"\n--- Estratégia: {estrategia} ---")
    
   
    chamadas_restantes = chamadas.copy()
    
    while len(chamadas_restantes) > 0:
        
        if estrategia == "Ordem de Chegada (FCFS)":
           
            chamada_atual = chamadas_restantes.pop(0)
        else:
            
            chamada_atual = min(chamadas_restantes, key=lambda c: abs(c[0] - andar_atual))
            chamadas_restantes.remove(chamada_atual)
            
        origem = chamada_atual[0]
        destino = chamada_atual[1]
        ordem_atendimento.append(chamada_atual)
        
        
        # 1. Elevador vai até o andar de origem buscar o passageiro
        distancia_origem = abs(origem - andar_atual)
        total_deslocamentos += distancia_origem
        tempo_total += (distancia_origem * 3) + 5  # 3s por andar + 5s para abrir/fechar porta
        
        # 2. Elevador leva o passageiro até o destino
        distancia_destino = abs(destino - origem)
        total_deslocamentos += distancia_destino
        tempo_total += (distancia_destino * 3) + 5 # 3s por andar + 5s para abrir/fechar porta
        
      
        andar_atual = destino
        
  
    ordem_str = " -> ".join([f"({c[0]},{c[1]})" for c in ordem_atendimento])
    
    print(f" Ordem: {ordem_str}")
    print(f" Deslocamento: {total_deslocamentos} andares")
    print(f" Tempo total: {tempo_total} segundos")



chamadas_etec = [(0, 4), (2, 1), (3, 0), (4, 2)]

print("=== DESAFIO DO ELEVADOR ETEC (PYTHON) ===")
simular_elevador(chamadas_etec, "Ordem de Chegada (FCFS)")
simular_elevador(chamadas_etec, "Mais Próximo Primeiro (Otimizado)")
