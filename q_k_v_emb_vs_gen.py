import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('off')

# box positions
boxes = {
    'Q_embed': (0.05, 0.7),
    'K_embed': (0.05, 0.45),
    'V_embed': (0.05, 0.2),
    'Q_gen':   (0.65, 0.7),
    'K_gen':   (0.65, 0.45),
    'V_gen':   (0.65, 0.2),
}

w, h = 0.22, 0.18

# draw boxes
for name, (x, y) in boxes.items():
    rect = Rectangle((x, y), w, h, fill=False, ec='black', lw=1.5)
    ax.add_patch(rect)
    label = name.split('_')[0]
    ax.text(x + w/2, y + h*0.65, label, ha='center', va='center', fontsize=14, fontweight='bold')
    ax.text(x + w/2, y + h*0.25, r'(B, T, $d_k$)', ha='center', va='center', fontsize=9)

# headings
ax.text(0.16, 0.93, 'Vector Embedding Projections', ha='center', va='center', fontsize=12)
ax.text(0.76, 0.93, 'Causally-Masked Auto-Regressive Generator', ha='center', va='center', fontsize=12)

# arrows mapping shapes
pairs = [('Q_embed', 'Q_gen'), ('K_embed', 'K_gen'), ('V_embed', 'V_gen')]
for left, right in pairs:
    x1, y1 = boxes[left]
    x2, y2 = boxes[right]
    y_mid = y1 + h/2
    arrow = FancyArrowPatch((x1 + w, y_mid), (x2, y_mid),
                            arrowstyle='->', mutation_scale=10, lw=1.3)
    ax.add_patch(arrow)

# causal mask indication
mask = Rectangle((boxes['Q_gen'][0], boxes['Q_gen'][1]-0.05), w, h*0.1, color='black', alpha=0.15)
ax.add_patch(mask)
ax.text(boxes['Q_gen'][0] + w/2, boxes['Q_gen'][1]-0.02, 'causal mask', ha='center', va='top', fontsize=8)

plt.tight_layout()
plt.show()
