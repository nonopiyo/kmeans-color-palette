import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

# 手動で作成した印象別カラーパレットの定義
color_palettes = {
    "Elegant": ["#2C3E50", "#D4AF37", "#C0C0C0", "#6D071A", "#5F7367"],
    "Pop": ["#FFD700", "#FF69B4", "#87CEFA", "#FFA500", "#98FB98"],
    "Natural": ["#F5DEB3", "#6B8E23", "#8B4513", "#FFFFF0", "#556B2F"],
    "Modern": ["#000000", "#FFFFFF", "#808080", "#4682B4", "#008080"],
    "Romantic": ["#FFC0CB", "#E6E6FA", "#C71585", "#9370DB", "#FAF0E6"],
    "Minimal": ["#FFFFFF", "#D3D3D3", "#333333", "#C2B280", "#1C2833"],
    "Classic": ["#800020", "#1D2951", "#CD7F32", "#FFFDD0", "#002147"],
    "Fresh": ["#32CD32", "#00BFFF", "#FF6F61", "#FFF44F", "#40E0D0"],
    "Vintage": ["#D8B2A1", "#FFDB58", "#704214", "#5B768D", "#A9A9A9"],
    "Energetic": ["#FF0000", "#FF4500", "#CCFF00", "#007FFF", "#FF1493"],
    "Feminine": ["#FF007F", "#FFD1DC", "#FA8072", "#FFE5B4", "#AE7181"],
    "Cool": ["#4D4D4D", "#003366", "#B0E0E6", "#1C1C1C", "#50C878"]
}

# クラスタ数（印象ごとに調整可能）
n_clusters_per_impression = 3

# 結果を格納するリスト
clustered_palettes = {}

# 各印象ごとにK-meansを適用
for category, colors in color_palettes.items():
    # RGB値に変換
    color_data = np.array([[int(color[i:i+2], 16) for i in (1, 3, 5)] for color in colors])

    # K-meansを適用
    kmeans = KMeans(n_clusters=min(n_clusters_per_impression, len(color_data)), random_state=42, n_init=10)
    kmeans.fit(color_data)
    
    # クラスタの代表色を取得
    cluster_centers = kmeans.cluster_centers_.astype(int)
    
    # HEXに変換
    hex_colors = [f"#{r:02X}{g:02X}{b:02X}" for r, g, b in cluster_centers]
    
    # 保存
    clustered_palettes[category] = hex_colors

# カラーパレットの可視化
fig, axes = plt.subplots(len(clustered_palettes), 1, figsize=(10, len(clustered_palettes) * 1.5))

for i, (category, colors) in enumerate(clustered_palettes.items()):
    for j, color in enumerate(colors):
        axes[i].fill_between([j, j + 1], 0, 1, color=color)
    axes[i].set_xticks(range(len(colors)))
    axes[i].set_xticklabels(colors, rotation=45, ha="right")
    axes[i].set_yticks([])
    axes[i].set_title(category)

plt.tight_layout()
plt.show()
