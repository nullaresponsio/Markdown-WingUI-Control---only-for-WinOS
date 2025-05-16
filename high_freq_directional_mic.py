"""
Directed Sound Array Systems — concise reference for Bo

Sources
-------
LRAD 450XL spec :contentReference[oaicite:0]{index=0}  
LRAD police deployments :contentReference[oaicite:1]{index=1}  
HyperSpike HS-18 spec :contentReference[oaicite:2]{index=2}  
Audio Spotlight AS-24i spec :contentReference[oaicite:3]{index=3}  
Brown Innovations SB-24 spec :contentReference[oaicite:4]{index=4}  
Soundlazer SL-01 details :contentReference[oaicite:5]{index=5}  
Focusonics Model A manual :contentReference[oaicite:6]{index=6}  
Federal Signal DSA array :contentReference[oaicite:7]{index=7}  
FBI Waco ‘psycho-acoustic correction’ :contentReference[oaicite:8]{index=8}  
NSA “LOUDAUTO” audio exploit :contentReference[oaicite:9]{index=9}
"""

speaker_systems = {
    "LRAD 450XL": {
        "manufacturer": "Genasys Inc.",
        "frequency_range": "≈300 Hz–8 kHz (voice-optimised)",
        "beam_width_deg": 30,  # ±15° @ 1 kHz
        "peak_spl_db": 150,
        "max_range_m": 1700,
        "agency_use": ["US police crowd-control", "US Navy", "DHS"],
        "thematic_sounds": ["voice commands", "alert siren", "evacuation message",
                            "wildlife deterrent tone"]
    },
    "HyperSpike HS-18": {
        "manufacturer": "Ultra Electronics",
        "frequency_range": "245 Hz–10 kHz",
        "beam_width_deg": 10,  # ±5°
        "peak_spl_db": 156,
        "max_range_m": 3000,
        "agency_use": ["military hailing", "law-enforcement perimeter"],
        "thematic_sounds": ["spoken warnings", "high-freq alert chirp",
                            "marine hailing"]
    },
    "Audio Spotlight AS-24i": {
        "manufacturer": "Holosonics",
        "frequency_range": "≈200 Hz–15 kHz (demodulated)",
        "beam_width_deg": 5,
        "peak_spl_db": 90,
        "max_range_m": 50,
        "agency_use": ["museum kiosk", "secure ops centers (rumoured NSA)"],
        "thematic_sounds": ["private narration", "masked speech", "directional music"]
    },
    "Brown Innovations SB-24": {
        "manufacturer": "Brown Innovations",
        "frequency_range": "150 Hz–20 kHz",
        "beam_width_deg": 20,
        "peak_spl_db": 100,
        "max_range_m": 30,
        "agency_use": ["retail display", "police interview booths"],
        "thematic_sounds": ["focused dialog", "background-noise masking"]
    },
    "Soundlazer SL-01": {
        "manufacturer": "Richard Haberkern (Soundlazer)",
        "frequency_range": "ultrasonic carrier 40 kHz, audio 1–16 kHz",
        "beam_width_deg": 3,
        "peak_spl_db": 88,
        "max_range_m": 20,
        "agency_use": ["acoustic research", "experimental covert ops"],
        "thematic_sounds": ["whispered speech", "psycho-acoustic tone"]
    },
    "Focusonics Model A": {
        "manufacturer": "Neurotechnology",
        "frequency_range": "parametric 40 kHz carrier, audio 250 Hz–15 kHz",
        "beam_width_deg": 5,
        "peak_spl_db": 85,
        "max_range_m": 15,
        "agency_use": ["immersive exhibits", "confidential briefings"],
        "thematic_sounds": ["localized music", "language prompts"]
    },
    "Federal Signal DSA": {
        "manufacturer": "Federal Signal Corp.",
        "frequency_range": "300 Hz–6 kHz (voice)",
        "beam_width_deg": 70,
        "peak_spl_db": 133,
        "max_range_m": 600,
        "agency_use": ["industrial evacuation", "police mobile PA"],
        "thematic_sounds": ["alarm tones", "public-address"]
    }
}

block_diagram_components = [
    "Audio Input (20 Hz–20 kHz)",
    "Ultrasonic Carrier Generator (40 kHz)",
    "Modulator (AM/SSB)",
    "Class-D Amplifier",
    "Piezoelectric Transducer Array (64 elements)",
    "Acoustic Lens/Waveguide",
    "Beam-Steering Actuators",
    "DSP Controller",
    "Power Supply",
    "Directional Sound Beam (3°–15°)"
]

if __name__ == "__main__":
    import json, pprint
    pprint.pp(speaker_systems)
