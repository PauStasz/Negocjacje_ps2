#!/usr/bin/python3
# -*- coding: utf-8 -*-

from Models.Node import Node
from Models.Graph import Graph
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # wagi:    100/3                  50/2                    25/1.5           10/1
    nodes = [Node(40, "CENA"), Node(42, "CENA"), Node(45, "CENA"), Node(50, "CENA"),
    #wagi:               100/3                    50/2                       10/1
             Node("0-2", "DOSTAWA"), Node("2-7", "DOSTAWA"), Node("7-14", "DOSTAWA"),
    #wagi:          10/1                       50/2                          100/3
             Node("0-3", "ZAPŁATA"), Node("3-7", "ZAPŁATA"), Node("7-30", "ZAPŁATA")]

    graph = Graph(nodes)
    graph.visualize()