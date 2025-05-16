# Sources:
# TRW-17 frequency data :contentReference[oaicite:0]{index=0}
# ButtKicker LFE frequency data :contentReference[oaicite:1]{index=1}
# SVS PB16-Ultra frequency data :contentReference[oaicite:2]{index=2}
# Low-frequency penetration property :contentReference[oaicite:3]{index=3}

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ── RAG block diagram ──
blocks = [
    ("User\nQuery", (0.05, 0.65, 0.2, 0.2)),
    ("Embedder\nOpenAI text-embedding-3-small\n1536 dims", (0.3, 0.65, 0.25, 0.2)),
    ("Vector DB\nFAISS (Meta)\nIndex: HNSW", (0.6, 0.65, 0.25, 0.2)),
    ("Retriever\ncosine k=5", (0.6, 0.35, 0.25, 0.2)),
    ("Generator\ngpt-4o (OpenAI)", (0.3, 0.35, 0.25, 0.2)),
    ("Response", (0.05, 0.35, 0.2, 0.2)),
]

for text, (x, y, w, h) in blocks:
    ax1.add_patch(patches.Rectangle((x, y), w, h, edgecolor="black", facecolor="lightgray"))
    ax1.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=7)

arrow = dict(arrowstyle="->", lw=1)
ax1.annotate("", xy=(0.3, 0.75), xytext=(0.25, 0.75), arrowprops=arrow)
ax1.annotate("", xy=(0.55, 0.75), xytext=(0.55, 0.75), arrowprops=arrow)
ax1.annotate("", xy=(0.725, 0.65), xytext=(0.725, 0.55), arrowprops=arrow)
ax1.annotate("", xy=(0.55, 0.45), xytext=(0.55, 0.45), arrowprops=arrow)
ax1.annotate("", xy=(0.3, 0.45), xytext=(0.25, 0.45), arrowprops=arrow)
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)
ax1.axis("off")
ax1.set_title("Retrieval-Augmented Generation (RAG) Pipeline")

# ── Frequency vs. penetration ──
products = [
    ("Eminent TRW-17", 1),
    ("ButtKicker LFE", 5),
    ("SVS PB16-Ultra", 13),
]

freq = np.array([p[1] for p in products], dtype=float)
penetration = 10 - np.log10(freq) * 3  # heuristic 0-10 scale

ax2.scatter(freq, penetration, s=80, c="steelblue")
for (name, f), pen in zip(products, penetration):
    ax2.annotate(name, (f, pen), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8)

ax2.set_xscale("log")
ax2.set_xlabel("Frequency (Hz) – log scale")
ax2.set_ylabel("Relative Structure Penetration\n(arbitrary units)")
ax2.set_title("Low-Frequency Speaker Penetration Correlation")
ax2.grid(True, which="both", ls="--", lw=0.5)

plt.tight_layout()
plt.show()
