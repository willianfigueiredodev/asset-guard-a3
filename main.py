import numpy as np
from cenario import CenarioDeMonitoramento
from detector import DetectorDeAnomalias

if __name__ == "__main__":

    np.random.seed(42)
    centros_operacionais = [
        [-12.91, -38.33],  # Pátio de Bagagens
        [-12.90, -38.32]   # Área de Manutenção
    ]
    pontos_anomalos_teste = [
        [-12.93, -38.34], # Perto da pista
        [-12.89, -38.35], # Perto do terminal
    ]

    cenario = CenarioDeMonitoramento(centros_normais=centros_operacionais, dados_anomalos=pontos_anomalos_teste)
    detector = DetectorDeAnomalias(n_clusters=len(centros_operacionais))

    cenario.gerar_cenario()
    cenario.visualizar()
    detector.treinar(cenario.dados_normais)
    
    print("\n--- Testando a Lógica de Detecção ---")
    ponto_normal = [-12.911, -38.331]
    ponto_anomalo = [-12.93, -38.34]

    e_anomalia_normal, dist_normal = detector.verificar(ponto_normal)
    print(f"Verificando ponto NORMAL {ponto_normal}:")
    print(f"  > É uma anomalia? {'SIM' if e_anomalia_normal else 'NÃO'} (Dist: {dist_normal:.5f})")
    
    e_anomalia_anomalo, dist_anomalo = detector.verificar(ponto_anomalo)
    print(f"Verificando ponto ANÔMALO {ponto_anomalo}:")
    print(f"  > É uma anomalia? {'SIM' if e_anomalia_anomalo else 'NÃO'} (Dist: {dist_anomalo:.5f})")


# Na nossa main mais Clean e funcional, importando os metodos que criamos.

# 1 - Primeiro, ele configura os parâmetros do cenário que queremos simular.
# 2 - Depois, ele cria os objetos, ou seja, 'contrata' um Cenario e um Detector.
# 3 - Em seguida, ele orquestra a operação: manda o Cenario gerar os dados, depois manda o Detector treinar com esses dados.
# 4 - Por fim, ele valida a solução, pedindo ao Detector que verifique alguns pontos de teste.

# Esta arquitetura demonstra um design de software maduro e, mais importante, flexível. Se amanhã quisermos adicionar um alerta por e-mail, por exemplo, não precisamos mexer em nenhuma das classes existentes.
# Apenas adicionaríamos um novo passo aqui no main.py, provando a escalabilidade do nosso projeto."