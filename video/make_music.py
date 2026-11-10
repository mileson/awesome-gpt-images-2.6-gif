"""Synthesize a tech-feel electronic background loop for the GIF showcase video.

Style: 122 BPM, A minor, four-on-the-floor kick, driving saw bass,
bright 16th-note arp, hats + claps, soft pad. Intro bar and outro bar
drop the drums so the piece breathes. Output: 56.0 s, 44.1 kHz, 16-bit WAV.
Pure synthesis (numpy) — no samples, no licensing issues.
"""
import math
import wave

import numpy as np

SR = 44100
DUR = 56.0
N = int(SR * DUR)
BPM = 122
BEAT = 60.0 / BPM
SIXTEENTH = BEAT / 4
EIGHTH = BEAT / 2
BAR = 4 * BEAT

# Am - F - C - G, each 1 bar: (root Hz, chord tones Hz)
CHORDS = [
    (110.00, [220.00, 261.63, 329.63]),  # Am: A2; A3 C4 E4
    (87.31, [174.61, 220.00, 261.63]),   # F:  F2; F3 A3 C4
    (130.81, [261.63, 329.63, 392.00]),  # C:  C3; C4 E4 G4
    (98.00, [196.00, 246.94, 293.66]),   # G:  G2; G3 B3 D4
]


def bar_chord(b):
    return CHORDS[b % 4]


def add(dst, start, sig):
    s = int(start * SR)
    e = min(len(dst), s + len(sig))
    if e > s:
        dst[s:e] += sig[: e - s]


def exp_env(n, tau):
    return np.exp(-np.arange(n) / SR / tau)


def saw(freq, length, harmonics=6):
    n = int(length * SR)
    tt = np.arange(n) / SR
    s = np.zeros(n)
    for h in range(1, harmonics + 1):
        s += np.sin(2 * np.pi * freq * h * tt) / h
    return s * (2 / np.pi)


mix = np.zeros(N)
n_beats = int(DUR / BEAT)
n_eighths = int(DUR / EIGHTH)

# 1. Kick: four on the floor, skip intro bar and outro bar
kick_len = int(0.28 * SR)
kt = np.arange(kick_len) / SR
freq = 45 + (130 - 45) * np.exp(-kt / 0.03)
phase = 2 * np.pi * np.cumsum(freq) / SR
kick = np.sin(phase) * exp_env(kick_len, 0.09)
for i in range(n_beats):
    if 4 <= i < n_beats - 4:
        add(mix, i * BEAT, kick * 0.9)

# 2. Bass: eighth notes, octave lift on the "and" of beat 4
bass_len = EIGHTH * 0.92
for i in range(n_eighths):
    if i < 8 or i >= n_eighths - 8:
        continue
    bar_idx = int((i * EIGHTH) // BAR)
    root = bar_chord(bar_idx)[0]
    pos_in_bar = (i * EIGHTH) % BAR
    f = root * (2 if abs(pos_in_bar - 3.5 * BEAT) < 0.01 else 1)
    sig = saw(f, bass_len) * exp_env(int(bass_len * SR), 0.11)
    add(mix, i * EIGHTH, sig * 0.32)

# 3. Arp: 16th notes through chord tones + octave, with a short echo
arp = np.zeros(N)
arp_seq = [0, 1, 2, 3, 2, 1]
n_six = int(DUR / SIXTEENTH)
for i in range(n_six):
    bar_idx = int((i * SIXTEENTH) // BAR)
    tones = bar_chord(bar_idx)[1]
    ext = [tones[0], tones[1], tones[2], tones[0] * 2, tones[1] * 2, tones[2] * 2]
    f = ext[arp_seq[i % len(arp_seq)]]
    L = int(0.14 * SR)
    tt = np.arange(L) / SR
    sig = np.tanh(np.sin(2 * np.pi * f * tt) * 2.0) * np.exp(-tt / 0.05)
    add(arp, i * SIXTEENTH, sig * 0.14)
d = int(3 * SIXTEENTH * SR)
arp_echo = np.zeros(N)
arp_echo[d:] = arp[:-d] * 0.35
mix += arp + arp_echo

# 4. Hats: offbeat eighths, highpassed noise
rng = np.random.default_rng(7)
hat_len = int(0.05 * SR)
noise = rng.standard_normal(hat_len)
hat = np.diff(noise, prepend=0) * np.exp(-np.arange(hat_len) / SR / 0.015)
for i in range(n_eighths):
    if i % 2 == 1 and 8 <= i < n_eighths - 8:
        add(mix, i * EIGHTH, hat * 0.10)

# 5. Clap on beats 2 & 4
clap_len = int(0.15 * SR)
cn = rng.standard_normal(clap_len)
k = int(SR * 0.001)
lp = np.convolve(cn, np.ones(k) / k, mode="same")
clap = (cn - lp) * np.exp(-np.arange(clap_len) / SR / 0.05)
for i in range(n_beats):
    if i % 4 in (1, 3) and 4 <= i < n_beats - 4:
        add(mix, i * BEAT, clap * 0.22)

# 6. Pad: detuned saws on chord tones, slow attack/release, quiet
n_bars = int(math.ceil(DUR / BAR))
for b in range(n_bars):
    tones = bar_chord(b)[1]
    s0 = b * BAR
    e0 = min(DUR, (b + 1) * BAR)
    L = int((e0 - s0) * SR)
    tt = np.arange(L) / SR
    sig = np.zeros(L)
    for f in tones:
        for det in (-0.996, 1.004):
            s = np.zeros(L)
            for h in range(1, 5):
                s += np.sin(2 * np.pi * f * det * h * tt) / h
            sig += s * (2 / np.pi)
    env = np.clip(np.minimum(tt / 0.4, (L / SR - tt) / 0.4), 0, 1)
    add(mix, s0, sig * env * 0.05)

# Master: soft clip, peak normalize, fades
mix = np.tanh(mix * 1.2)
peak = np.max(np.abs(mix))
mix = mix / peak * 0.89
fade_in = min(int(0.8 * SR), N)
fade_out = min(int(2.0 * SR), N)
mix[:fade_in] *= np.linspace(0, 1, fade_in)
mix[-fade_out:] *= np.linspace(1, 0, fade_out)

pcm = (mix * 32767).astype(np.int16)
out_path = "/home/hatch/workspace/gpt-images-2-6-gif-repo-staging/video/tech-bed.wav"
with wave.open(out_path, "wb") as w:
    w.setnchannels(1)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print("wrote", out_path, "peak", round(float(np.max(np.abs(mix))), 3),
      "rms", round(float(np.sqrt(np.mean(mix ** 2))), 3))
