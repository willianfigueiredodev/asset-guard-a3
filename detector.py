import numpy as np
from sklearn.cluster import KMeans

class DetectorDeAnomalias:
    """
    Encapsula toda a lógica de Machine Learning (o "cérebro" do AssetGuard).
    Sua responsabilidade é aprender o que é "normal" e depois identificar desvios.
    Isso é um exemplo de encapsulamento, um pilar da Orientação a Objetos.
    """
    def __init__(self, n_clusters):
        self.n_clusters = n_clusters
        self.modelo = KMeans(n_clusters=self.n_clusters, random_state=42, n_init=10)
        self.limiar_anomalia = None
        self.centroides_aprendidos = None

    def treinar(self, dados_normais):
        """
        Treina o modelo K-Means apenas com dados normais e, em seguida,
        calcula a "fronteira" matemática do que é considerado normal.
        """
        print("--- Treinando Modelo K-Means... ---")
        self.modelo.fit(dados_normais)
        self.centroides_aprendidos = self.modelo.cluster_centers_

        distancias = np.min(self.modelo.transform(dados_normais), axis=1)# Calculo distância normal ao seu centroide mais próximo
        
        
        self.limiar_anomalia = np.max(distancias) * 1.1 # Esse limiar pega a maior distância encontrada e adiciona uma margem de segurança

        print("--- Modelo K-Means Treinado com Sucesso ---")
        print(f"Limiar de anomalia calculado: {self.limiar_anomalia:.5f}")

    def verificar(self, ponto):
        """
        Recebe um novo ponto, usa o modelo treinado e retorna se é uma anomalia.
        """
        if self.limiar_anomalia is None:
            raise RuntimeError("O modelo ainda não foi treinado. Chame o método treinar() primeiro.")
            
        ponto_array = np.array([ponto])
        
        distancia_minima = np.min(self.modelo.transform(ponto_array))
        
        e_anomalia = distancia_minima > self.limiar_anomalia
        
        return e_anomalia, distancia_minima


# A segunda classe que criamos foi a DetectorDeAnomalias. Ela é o cérebro do nosso sistema e isola toda a complexidade do Machine Learning.

# 1 - O método treinar é o coração do aprendizado. 
#     Ele recebe os dados normais e faz duas coisas cruciais: primeiro, treina o modelo K-Means para encontrar os centros das operações 
#     e segundo, calcula o nosso 'limiar de anomalia', que é a fronteira matemática do que é considerado normal.

# 2 - Já o método verificar é o nosso 'guarda' em ação. 
#     Ele recebe um novo ponto, usa o modelo que já foi treinado, e retorna um veredito simples: 
#     verdadeiro se for uma anomalia, e falso se não for.

# Basicamente o ganho aqui é que o resto da nossa aplicação não precisa saber como a detecção funciona. 
# Ele só precisa criar um Detector, treiná-lo e depois fazer perguntas a ele. Isso é encapsulamento, um pilar da Orientação a Objetos."