# ⚡ Cyber Runner 3D: Neon Overdrive (AAA Edition)

Next-generation high-speed 3D synthwave arcade runner powered by Three.js, Web Audio procedural synthesis, and WebGL post-processing.

![Gameplay Preview](preview.png)

## 🕹 Live Web Game
Play directly in browser: [https://adamhasani.github.io/cyber-runner-3d/](https://adamhasani.github.io/cyber-runner-3d/)

---

## 🚀 Key Features & AAA Enhancements

1. **Next-Gen WebGL Post-Processing Pipeline**:
   - **UnrealBloomPass**: Emissive luminescence on neon curbs, plasma thrusters, glowing billboards, and laser gates.
   - **Custom Cyberpunk Post-Shader**: Radial chromatic aberration with sharp center focal tracking, dynamic CRT scanlines, screen glitch impacts, and radial motion blur during nitro overdrive.
   - **Bloom Quality Toggle**: Switchable on-the-fly via the top-right HUD button (`✨ BLOOM: ON/OFF`).

2. **High-Fidelity Hovercraft & Aerodynamics**:
   - Aerodynamic delta wings with active elevon flaps (ailerons) that articulate smoothly during steering.
   - Dynamic banking & roll physics with realistic port/starboard thruster flares.
   - Dual glowing plasma exhaust cones with turbulent particle spark trails.
   - Forward spotlight illumination casting dynamic specular reflections across wet asphalt tarmac.

3. **Living Cyber Cityscape & Highway Architecture**:
   - Towering skyscrapers with procedural illuminated window matrices in neon cyan, pink, and amber.
   - Rooftop antenna masts with synchronized red aviation warning beacons.
   - Overhead truss gantries with glowing holographic signage.
   - High-speed elevated maglev bullet train traversing above the city skyline.

4. **Dynamic Hazard & Traffic System**:
   - **Neon Barriers**: Jumpable obstacles requiring timing precision.
   - **Dual Plasma Laser Gates**: Pulsating laser beams traversing across lanes.
   - **EMP Sentry Drones**: Floating gyroscopic mines with sinusoidal oscillating sweep paths.
   - **Autonomous Cyber Cargo Haulers**: Moving traffic vehicles cruising forward at 22 km/h. Tailgate directly behind them to trigger **⚡ Slipstream Drafting** (+Speed & free Nitro recharge!).
   - **Boost Launch Pads**: High-velocity road arrow strips that launch hovercraft into instant supersonic overdrive (+500 pts).

5. **Procedural Web Audio Synthwave Engine & Neural Co-Pilot**:
   - Built-in multi-oscillator 128 BPM Synthwave synthesizer (kick, snare, hi-hats, arpeggiated bassline).
   - Dynamic hovercraft engine sound that smoothly shifts pitch based on real-time speed (80 Hz to 350 Hz).
   - High-impact sound effects: Jump, Sonic Boom Boost, Near Miss Whoosh, Shield Absorption, and Crash.
   - Real-time voice telemetry co-pilot via Speech Synthesis announcing system updates (*"Hyperdrive active"*, *"Shield matrix online"*, *"Near miss!"*).

---

## 🎮 Controls

| Action | Keyboard | Touch / Mobile |
| :--- | :--- | :--- |
| **Steer & Bank** | `A` / `D` or `◀` / `▶` | Left / Right D-Pad |
| **Supersonic Jump** | `SPACE` or `▲` / `W` | Jump Button (`▲`) |
| **Nitro Hyperdrive** | `SHIFT` or `E` | Boost Button (`⚡`) |
| **Air Brake** | `S` or `▼` | - |
| **Audio Toggle** | Click `SFX/BGM: ON` | Tap HUD Toggle |
| **Bloom Toggle** | Click `BLOOM: ON` | Tap HUD Toggle |

---

## 🛠 Tech Stack
- **Engine**: Three.js (r128)
- **Post-Processing**: Three.js EffectComposer, UnrealBloomPass, ShaderPass
- **Audio**: Web Audio API (Procedural Synthesizer) & Web Speech API
- **Deployment**: GitHub Pages (Fastly CDN)
