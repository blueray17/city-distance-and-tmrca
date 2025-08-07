import pandas as pd
import json

# Baca file Excel
df = pd.read_excel("city_distance.xlsx", index_col=0)

# Buat nodes dan edges
cities = df.index.tolist()
nodes = [{'id': city} for city in cities]
edges = []

for i, source in enumerate(cities):
    for j, target in enumerate(cities):
        if j > i:
            distance = df.iloc[i, j]
            if pd.notna(distance):
                edges.append({
                    'source': source,
                    'target': target,
                    'distance': round(distance, 2)
                })

# Simpan sebagai JSON
data = {"nodes": nodes, "edges": edges}
with open("city_graph_all.json", "w") as f:
    json.dump(data, f, indent=2)

print("Berhasil disimpan ke city_graph.json")
