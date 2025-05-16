# -*- coding: utf-8 -*-
"""
Block diagram of MacBook Pro (M2 Max) audio path + extended frequency-coverage chart  
Data sources (clearly labeled):  
 • Apple tech specs – six-speaker system & studio-quality 3-mic array :contentReference[oaicite:0]{index=0}  
 • RTINGS speaker Bass Extension ≈ 112 Hz, Treble Extension 20 kHz, max 78 dB SPL :contentReference[oaicite:1]{index=1}  
 • Notebookcheck audio analysis confirms ≈ 90 Hz low-end roll-off :contentReference[oaicite:2]{index=2}  
 • DXOMARK capture response graph shows mic usable ≳ 100 Hz, smooth to 20 kHz :contentReference[oaicite:3]{index=3}  
 • Apple discussion thread lists 20 Hz–20 kHz spec for built-in audio I/O (legacy reference) :contentReference[oaicite:4]{index=4}  
 • Developer forum: built-in mics default to 48 kHz sample-rate (Nyquist 24 kHz) :contentReference[oaicite:5]{index=5}  
 • Apple Support: integrated DAC supports up to 96 kHz/24-bit monitoring :contentReference[oaicite:6]{index=6}  
 • DXOMARK blog: MacBook Pro playback shows strong bass; mic capture filtered < 100 Hz :contentReference[oaicite:7]{index=7}  
 • Reddit community measurement verifies flat response to 20 kHz on speakers :contentReference[oaicite:8]{index=8}  
 • Apple generic specs reiterate high-SNR directional beam-forming mic array :contentReference[oaicite:9]{index=9}
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ── layout: two stacked plots ────────────────────────────────────────────────────
fig, (ax, axf) = plt.subplots(
    nrows=2, figsize=(11, 9), gridspec_kw={"height_ratios": [2, 1]}
)
fig.subplots_adjust(hspace=0.4)
ax.axis("off")

# ── original signal-flow blocks (unchanged) ─────────────────────────────────────
blocks = {
    "Mic Array\n3 × beam-forming\n100 Hz – 20 kHz\nSNR > 66 dB": (0.05, 0.55, .18, .25),
    "ADC + DSP\n24-bit / 48 kHz\nApple M2 Max":                 (0.28, 0.55, .18, .25),
    "Audio Engine\nNoise-red.,\nbeam-form,\nspatial audio":      (0.51, 0.55, .18, .25),
    "Speaker Amp\nClass-D":                                      (0.74, 0.55, .18, .25),
    "6-Speaker Array\n2 tweeters 2 mids\n2 × force-cancel\n90 Hz – 20 kHz\n78 dB SPL": (0.74, 0.15, .18, .3),
    "Thematic Outputs\n• voice chat\n• Dolby Atmos\n• system alerts": (0.51, 0.15, .18, .3),
    "Manufacturing\nApple Inc.\nModel A2780\nAssembled in China\n(2023)": (0.28, 0.15, .18, .3),
    "Agency / LE Uses\nremote warrants,\nforensic review,\nsecure comms": (0.05, 0.15, .18, .3),
}

for text, (x, y, w, h) in blocks.items():
    ax.add_patch(
        patches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.02",
            linewidth=1.2, edgecolor="#333", facecolor="#dde8ff"
        )
    )
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=8)

def arrow(src, dst):
    sx, sy, sw, sh = blocks[src]
    dx, dy, dw, dh = blocks[dst]
    ax.annotate(
        "", xy=(dx, dy + dh / 2), xytext=(sx + sw, sy + sh / 2),
        arrowprops=dict(arrowstyle="->", lw=1.2)
    )

arrow("Mic Array\n3 × beam-forming\n100 Hz – 20 kHz\nSNR > 66 dB",
      "ADC + DSP\n24-bit / 48 kHz\nApple M2 Max")
arrow("ADC + DSP\n24-bit / 48 kHz\nApple M2 Max",
      "Audio Engine\nNoise-red.,\nbeam-form,\nspatial audio")
arrow("Audio Engine\nNoise-red.,\nbeam-form,\nspatial audio",
      "Speaker Amp\nClass-D")
arrow("Speaker Amp\nClass-D",
      "6-Speaker Array\n2 tweeters 2 mids\n2 × force-cancel\n90 Hz – 20 kHz\n78 dB SPL")

# ── frequency-coverage chart ────────────────────────────────────────────────────
axf.set_xscale("log")
axf.set_xlim(20, 20000)
axf.set_xlabel("Frequency (Hz)")
axf.set_yticks([0.5, 1.5, 2.5])
axf.set_yticklabels(["Speaker-only\n(emits, mic misses)",
                     "Mic Capture\n(100 Hz – 20 kHz)",
                     "Speaker Emission\n(90 Hz – 20 kHz)"])
axf.set_ylim(0, 3)
axf.grid(which="both", axis="x", linestyle=":", alpha=0.4)

# Speaker emission band
axf.add_patch(
    patches.Rectangle((90, 2.2), 20000 - 90, 0.6,
                      color="#b3d9ff", label="Speaker range")
)
# Mic capture band
axf.add_patch(
    patches.Rectangle((100, 1.2), 20000 - 100, 0.6,
                      color="#ffd9b3", label="Mic range")
)
# Speaker-only (= difference) band
axf.add_patch(
    patches.Rectangle((90, 0.2), 100 - 90, 0.6,
                      color="#ffb3b3", label="Speaker-only range")
)

for f in [20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000]:
    axf.axvline(f, ymin=0, ymax=1, color="#ccc", linewidth=0.4)

axf.legend(loc="lower center", ncol=3, bbox_to_anchor=(0.5, -0.35), frameon=False)

plt.tight_layout()
plt.show()
