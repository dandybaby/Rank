import networkx as nx
import matplotlib.pyplot as plt

# 创建有向图
G = nx.DiGraph()
# 设计有向图的边集合
edges = [("A", "B"), ("A", "D"), ("A", "E"), ("A", "F"), ("B", "C"), ("C", "E"), ("D", "A"),
         ("D", "C"), ("D", "E"), ("E", "B"), ("E", "C"), ("F", "D")]
for edge in edges:
    G.add_edge(edge[0], edge[1])
    # 有向图可视化
layout = nx.spring_layout(G)
nx.draw(G, pos=layout, with_labels=True, hold=False)
plt.savefig('fig.png', bbox_inches='tight')  # 替换 plt.show()
# 计算简化模型的PR值
pr = nx.pagerank(G, alpha=1, max_iter=100)
print("简化模型的PR值：", pr)
# 计算随机模型的PR值
pr = nx.pagerank(G, alpha=0.8, max_iter=100)
print("随机模型的PR值：", pr)
