from Models.Node import Node

class Graph:
    def __init__(self, nodes):
        self.__nodes = nodes
        self.__edgesNumber = len(nodes)
        self.__edges = []
        self.__weights = []
        self.__result = []
        print("Tworzenie grafu...")
        self.create()
        print("Graf stworzony...")
        print("Szukanie rozwiazania...")
        self.findRoutesWithProfit()
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
                                    sum = 0
                                    if(node.value == 40):
                                        sum =  sum + 3
                                    elif(node.value == 42):
                                        sum =  sum + 2
                                    elif(node.value == 45):
                                        sum =  sum + 1.5
                                    elif(node.value == 50):
                                        sum =  sum + 1

                                    if(delivery.value == "0-2"):
                                        sum =  sum + 3
                                    elif(delivery.value == "2-7"):
                                        sum =  sum + 2
                                    elif(delivery.value == "7-14"):
                                        sum =  sum + 1

                                    
                                    if(price.value == "7-30"):
                                        sum =  sum + 3
                                    elif(price.value == "0-3"):
                                        sum =  sum + 1
                                    elif(price.value == "3-7"):
                                        sum =  sum + 2


                                    self.__weights.append(sum) # suma ścieżki, czyli 1 krawedzi -> cena -> dostawa -> zapłata
                                    print()

    def findRoutesWithProfit(self):
        
        merged = zip(self.__weights, self.__edges)

        afterSort = sorted(merged, key=lambda x: x[0])

        self.__result = [temp[1] for temp in afterSort]


    def bestRoutes(self):

        weights = sorted(self.__weights)

        for i in range(36):
            route = self.__result[i]
            if isinstance(route, list):
                print("Sposób nr "  + str(i + 1) + ": " + str(route[0].value) + " -> " + str(route[1].value) + " -> " + str(route[2].value) + ", waga: " + str(weights[i]))


