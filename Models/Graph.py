import networkx as nx
from matplotlib import pyplot as plt

from Models.Node import Node

class Graph:
    def __init__(self, nodes):
        self.__nodes = nodes
        self.__edges = []
        self.__weights = []
        self.__result = []
        print("Tworzenie grafu...")
        self.create()
        print("Graf stworzony...")
        print("Szukanie rozwiazania po raz 1...")
        self.findRoutesWithProfit(self.__edges)
        print("Etap 2:")
        self.findRoutesWithProfitByTheSameWeight()
        self.findRoutesWithProfit(self.__result)
        print("Szukanie rozwiazania po raz 2...")
        print("Wyniki:")
        self.bestRoutes()

    def create(self):

        # tworzenie krawedzi i  przepisanie wag
        for node in self.__nodes:
            if isinstance(node, Node):
                if(node.type == "CENA"):
                    for delivery in self.__nodes:
                        if(delivery.type == "DOSTAWA"):
                            for price in self.__nodes:
                                if(price.type == "ZAPŁATA"):
                                    temp = [node, delivery, price] # tworzenie krawedzi cena -> dostawa -> zapłata
                                    self.__edges.append(temp)
                                    print("Stworzona ścieżka: " + str(node.value) + " -> " + str(delivery.value) + " -> " + str(price.value) )
                                    sum = 0 #ta czesc mozna w funkcje walnac pozniej i parametry bo sie tylko to powtarza
                                    if(node.value == 40):
                                        sum =  sum + 100
                                    elif(node.value == 42):
                                        sum =  sum + 50
                                    elif(node.value == 45):
                                        sum =  sum + 25
                                    elif(node.value == 50):
                                        sum =  sum + 10

                                    if(delivery.value == "0-2"):
                                        sum =  sum + 100
                                    elif(delivery.value == "2-7"):
                                        sum =  sum + 50
                                    elif(delivery.value == "7-14"):
                                        sum =  sum + 10

                                    
                                    if(price.value == "7-30"):
                                        sum =  sum + 100
                                    elif(price.value == "0-3"):
                                        sum =  sum + 10
                                    elif(price.value == "3-7"):
                                        sum =  sum + 50


                                    self.__weights.append(sum) # suma ścieżki, czyli 1 krawedzi -> cena -> dostawa -> zapłata
                                    print()

    def findRoutesWithProfit(self, edges):
        
        merged = zip(self.__weights, edges)

        afterSort = sorted(merged, key=lambda x: x[0])

        self.__result = [temp[1] for temp in afterSort]

        self.__weights = sorted(self.__weights)

    def findRoutesWithProfitByTheSameWeight(self):
         weights_to_update = [0 for _ in range(len(self.__weights))]
         for i in range(len(self.__result)):
            if(i + 1 < len(self.__result)):
                weightRoute = self.__weights[i]
                weightNextRoute = self.__weights[i + 1]

                if(i > 0):
                    weightPreviousRoute = self.__weights[i - 1]
                else:
                    weightPreviousRoute = 0

                if(weightRoute == weightNextRoute or weightPreviousRoute == weightRoute):
                    route = self.__result[i]
                    if(route[0].value == 40):
                        weights_to_update[i] =  weights_to_update[i] + 3
                    elif(route[0] == 42):
                        weights_to_update[i] =  weights_to_update[i] + 2
                    elif(route[0] == 45):
                        weights_to_update[i] =  weights_to_update[i] + 1.5
                    elif(route[0] == 50):
                        weights_to_update[i] =  weights_to_update[i] + 1

                    if(route[1].value == "0-2"):
                        weights_to_update[i] =  weights_to_update[i] + 3
                    elif(route[1].value == "2-7"):
                        weights_to_update[i] =  weights_to_update[i] + 2
                    elif(route[1].value == "7-14"):
                        weights_to_update[i] =  weights_to_update[i] + 1

                                    
                    if(route[2].value == "7-30"):
                        weights_to_update[i] =  weights_to_update[i] + 3
                    elif(route[2].value == "0-3"):
                        weights_to_update[i] =  weights_to_update[i] + 1
                    elif(route[2].value == "3-7"):
                        weights_to_update[i] =  weights_to_update[i] + 2
         
         self.__weights = [(self.__weights[i] + weights_to_update[i]) for i in range(len(self.__weights))]
             
                                    
    def bestRoutes(self):
        for i in range(36):
            route = self.__result[i]
            if isinstance(route, list):
                print("Wariant nr "  + str(i + 1) + ": " + str(route[0].value) + " -> " + str(route[1].value) + " -> " + str(route[2].value) + ", waga: " + str(self.__weights[i]))

    def visualize(self):
        G = nx.DiGraph()
        for edge in self.__edges:
            G.add_edge(edge[0].value, edge[1].value)
            G.add_edge(edge[1].value, edge[2].value)

        pos = {
            40: (0, 2),
            42: (0, 1),
            45: (0, 0),
            50: (0, -1),
            "0-2": (2, 2),
            "2-7": (2, 1),
            "7-14": (2, 0),
            "0-3": (4, 2),
            "3-7": (4, 1),
            "7-30": (4, 0)
        }

        labels = {}
        for node in self.__nodes:
            labels[node.value] = f"{node.type}: {node.value}"

        nx.draw(G, pos, with_labels=True, labels=labels, node_size=6000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True, arrowstyle='->')
        plt.show()