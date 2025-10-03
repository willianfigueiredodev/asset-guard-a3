import numpy as np
import matplotlib.pyplot as plt

class CenarioDeMonitoramento:
    """
    Responsável por criar, gerenciar e visualizar os dados de um cenário específico.
    Esta classe aplica o princípio da Separação de Responsabilidades: ela cuida
    dos dados, mas não sabe nada sobre a lógica de detecção (IA).
    """
    def __init__(self, centros_normais, dados_anomalos, num_pontos_por_centro=100, dispersao=0.005):
        self.centros_normais = centros_normais
        self.pontos_anomalos_definidos = np.array(dados_anomalos)
        self.num_pontos_por_centro = num_pontos_por_centro
        self.dispersao = dispersao
        self.dados_normais = None
        self.todos_os_dados = None

    def gerar_cenario(self):
        """Gera os conjuntos de coordenadas normais e anômalas para a simulação."""
        pontos_gerados = []
        for centro in self.centros_normais:
            pontos = np.array(centro) + np.random.randn(self.num_pontos_por_centro, 2) * self.dispersao
            pontos_gerados.append(pontos)
        
        self.dados_normais = np.vstack(pontos_gerados)
        self.todos_os_dados = np.vstack([self.dados_normais, self.pontos_anomalos_definidos])
        print("--- Dados Simulados Gerados com Sucesso ---")
        return self

    def visualizar(self, salvar_arquivo=True):
        """Plota e opcionalmente salva a visualização gráfica do cenário."""
        plt.figure(figsize=(10, 8))
        plt.scatter(self.dados_normais[:, 1], self.dados_normais[:, 0], c='blue', label='Operação Normal')
        plt.scatter(self.pontos_anomalos_definidos[:, 1], self.pontos_anomalos_definidos[:, 0], c='red', marker='x', s=100, label='Anomalias')
        plt.title('Mapa Simulado da Área Técnica do Aeroporto')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.legend()
        plt.grid(True)
        
        if salvar_arquivo:
            plt.savefig('mapa_simulado_aeroporto.png')
            print("--- Gráfico dos Dados Gerado e Salvo ---")


# O primeiro passo na melhoria da nossa arquitetura foi aplicar o princípio da Separação de Responsabilidades. 
# Para isso, criamos a classe CenarioDeMonitoramento. A única responsabilidade dela é cuidar dos dados. 
# Ela não sabe nada sobre Inteligência Artificial.

# 1 - O método __init__ funciona como a planta do nosso cenário, recebendo as regras, como 'onde ficam as áreas normais' e 'quais são os pontos de anomalia'.
# 2 - O método gerar_cenario é quem de fato constrói o mundo, criando os conjuntos de coordenadas que vamos usar.
# 3 - E o método visualizar é o responsável por desenhar o mapa. Separar a visualização significa que, se no futuro quisermos usar uma biblioteca de mapas diferente 
#     só precisamos alterar este método, sem quebrar o resto do código.

# Em resumo, esta classe transforma a geração de dados, que era uma parte solta no nosso script, em um componente organizado e reutilizável.