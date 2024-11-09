import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data preparation
data = [
        [200, 200, 0.281],
        [200, 100, 0.331],
        [200,  50, 0.310],
        [200,  20, 0.306],
        [100, 100, 0.299],
        [100,  50, 0.324],
        [100,  20, 0.340],
        [100,  10, 0.348],
        [100,   5, 0.360],
        [100,   4, 0.340]
        [50,    5, 0.325]
]

# Convert to numpy array
data = np.array(data)

# Create a pivot table for the heatmap
feat_sel_unique = sorted(list(set(data[:,0])))
dim_red_unique = sorted(list(set(data[:,1])))

# Initialize the matrix with NaN values
heatmap_data = np.full((len(feat_sel_unique), len(dim_red_unique)), np.nan)

# Fill the matrix with F1 scores
for row in data:
    feat_sel, dim_red, f1_score = row
    i = feat_sel_unique.index(feat_sel)
    j = dim_red_unique.index(dim_red)
    heatmap_data[i, j] = f1_score

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# 1. Heatmap
sns.heatmap(heatmap_data, 
            annot=True, 
            fmt='.3f',
            cmap='YlOrRd',
            xticklabels=dim_red_unique,
            yticklabels=feat_sel_unique,
            ax=ax1)

ax1.set_title('F1 Macro Score Heatmap')
ax1.set_xlabel('Dimensionality Reduction')
ax1.set_ylabel('Feature Selection')

# 2. Bubble plot
scatter = ax2.scatter(data[:,1], data[:,0], s=data[:,2]*1000, 
                     c=data[:,2], cmap='YlOrRd', alpha=0.6)

# Add value annotations
for i, row in enumerate(data):
    ax2.annotate(f'{row[2]:.3f}', (row[1], row[0]), 
                xytext=(5, 5), textcoords='offset points')

ax2.set_title('F1 Macro Score Bubble Plot')
ax2.set_xlabel('Dimensionality Reduction')
ax2.set_ylabel('Feature Selection')
ax2.grid(True, alpha=0.3)

# Add colorbar
plt.colorbar(scatter, ax=ax2, label='F1 Macro Score')

plt.tight_layout()
plt.show()

# Print best combination
best_idx = np.argmax(data[:,2])
print(f"\nBest combination:")
print(f"Feature Selection: {data[best_idx,0]}")
print(f"Dimensionality Reduction: {data[best_idx,1]}")
print(f"F1 Macro Score: {data[best_idx,2]:.3f}")