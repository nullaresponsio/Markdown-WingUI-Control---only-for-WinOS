# iPhone 15 Pro Max – audio frequency blocks
# Sources
# [S1] Faber Acoustical mic response :contentReference[oaicite:0]{index=0}
# [S2] Notebookcheck speaker analysis :contentReference[oaicite:1]{index=1}
# [S3] DxOMark deep-bass commentary :contentReference[oaicite:2]{index=2}
# [S4] PowerPhone sampling-rate study :contentReference[oaicite:3]{index=3}
# Build simple diagram of speaker vs microphone vs codec bands

import matplotlib.pyplot as plt

iphone15_audio_bands = {
    # MEMS microphone array — three elements
    "microphone_array": {
        "capture_band_hz": (20, 20_000),            # full-band mic [S1]
        "speech_focus_hz": (300, 6_800),
        "lf_rolloff_hz": 20,
        "uf_rolloff_hz": 20_000,
        "sub_blocks": [
            (20, 80),
            (80, 250),
            (250, 2_000),
            (2_000, 10_000),
            (10_000, 20_000)
        ]
    },

    # Built-in hybrid stereo speakers
    "speaker_array": {
        "bottom_woofer_hz": (80, 20_000),           # bass floor ≈80 Hz [S2,S3]
        "top_earpiece_hz": (300, 18_000),
        "system_output_hz": (80, 20_000),
        "blocks": [
            (80, 120),
            (120, 300),
            (300, 2_000),
            (2_000, 10_000),
            (10_000, 20_000)
        ]
    },

    # Codec / amp signal path (A17 Pro + Cirrus front-end)
    "audio_codec": {
        "adc_passband_hz": (10, 20_000),            # 48 kHz Fs pass-band [S4]
        "dac_passband_hz": (10, 20_000),
        "internal_fs_hz": 96_000,                   # up-sampled DSP domain [S4]
        "stopband_start_hz": 24_000,
        "exclusive_blocks": [
            (0, 10),                 # DC rejected
            (10, 20_000),            # audio pass
            (20_000, 48_000),        # anti-alias region
            (48_000, 96_000)         # shaped DAC noise
        ]
    }
}

mic_band = iphone15_audio_bands["microphone_array"]["capture_band_hz"]
speaker_blocks = iphone15_audio_bands["speaker_array"]["blocks"]

speaker_only = [blk for blk in speaker_blocks
                if blk[0] < mic_band[0] or blk[1] > mic_band[1]]

fake_blocks = [(0, 80), (20_000, 24_000)]

fig, ax = plt.subplots(figsize=(10, 4))
y = [4, 3, 2, 1, 0]
labels = ['Microphone capture', 'Speaker output',
          'ADC/DAC pass', 'Speaker-only', 'Fake UI block']

ax.broken_barh([mic_band], (y[0]-0.4, 0.8), color='#a6dcef')

for blk in speaker_blocks:
    ax.broken_barh([blk], (y[1]-0.4, 0.8), color='#b8e6a3')

ax.broken_barh([iphone15_audio_bands["audio_codec"]["dac_passband_hz"]],
               (y[2]-0.4, 0.8), color='#d7b5f8')

for blk in speaker_only:
    ax.broken_barh([blk], (y[3]-0.4, 0.8), color='#ffd27f')

for blk in fake_blocks:
    ax.broken_barh([blk], (y[4]-0.4, 0.8),
                   facecolor='none', edgecolor='red', hatch='///')

for i, lab in enumerate(labels):
    ax.text(0, y[i], lab, va='center', ha='right', fontsize=9)

ax.set_xlim(0, 96_000)
ax.set_xscale('log')
ax.set_xlabel('Frequency (Hz)')
ax.set_yticks([])
ax.set_title('iPhone 15 Pro Max – audio frequency blocks\nspeaker vs microphone and codec path',
             fontsize=12, pad=12)
plt.tight_layout()
plt.show()
