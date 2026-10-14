# ⚡ WIPEOUT // OVERDRIVE — Anti-Gravity Racing (AAA Edition)

An authentic, dark industrial anti-gravity arcade racer inspired by the classic **WipEout** and **Redout** heritage, rendered in WebGL with Three.js, PBR materials, mechanical airbrake drifting, and procedural industrial breakbeat audio.

![Gameplay Preview](preview.png)

## 🕹 Live Web Game
Play directly in your browser: [https://adamhasani.github.io/cyber-runner-3d/](https://adamhasani.github.io/cyber-runner-3d/)

---

## 🚀 Key Features & Architectural Overhaul

1. **Art Direction: Dark Gritty Industrial Sci-Fi**:
   - Zero generic neon/synthwave tropes: built with an austere palette of titanium carbon-black, hazard amber (`#ff6a00`), and tactical telemetry cyan (`#00f0ff`).
   - Brutalist megastructure skyline with communication towers, synchronized red obstruction beacons, and high-voltage mag-accel overhead gantries.

2. **Advanced PBR Materials & Road Mechanics**:
   - Wet basalt/concrete composite roadway with procedural tarmac grain, expansion seams, and worn center dashed guides.
   - Realistic specular surface reflection balanced under ACES Filmic Tone Mapping without blown-out light pools.
   - Dual-color atmospheric lighting: cool cyan guide-wash on the port curb contrasted with warm industrial sodium amber on starboard.

3. **Bespoke Anti-Gravity Craft & Airbrake Physics**:
   - Faceted stealth monocoque fuselage with polarized pilot canopy and high-output twin jet turbine pods.
   - **Articulated Mechanical Airbrakes**: Dual carbon-composite elevon flaps with hazard chevron plates and hydraulic chrome pistons that actuate dynamically during turns and drift deceleration.
   - **G-Force Centrifugal Camera Roll**: Chase camera calculates dynamic roll banking matching craft inertia and lateral G-load.

4. **Deep Racing Mechanics**:
   - **Airbrake Drifting** (`S` / `▼` or `[DRFT]` button): Engage lateral airbrakes into corners to build the **G-FLOW** combo multiplier up to **5.0x** and trigger blue-arc skid sparks.
   - **Ion Afterburner** (`SHIFT` or `[BOOST]`): Unleash high-mach boost with chromatic aberration and shockwave camera shake to obliterate blast obstacles.
   - **Supersonic Jump** (`SPACE` / `▲`): Clear heavy blast doors and elevated track barriers.
   - **Near Miss Multipliers**: Shaving hazards by centimeters awards tactical score bonuses.

5. **Procedural Industrial Breakbeat Synthesizer & AI Tactical Comms**:
   - Built-in multi-channel 134 BPM breakbeat audio engine generated entirely via Web Audio API (industrial punch kicks, filtered bandpass snares, metallic square hi-hats, and detuned Reese synth bass).
   - Dynamic jet turbine pitch shifting smoothly tracking craft speed (110 Hz to 350 Hz).
   - Diegetic tactile audio FX: hydraulic airbrake hissing, sonic boom shockwaves, kinetic shield deflection, and heavy metal impacts.
   - Real-time aerospace flight telemetry voice synthesizer announcing system state updates.

---

## 🎮 Flight Controls

| Flight Action | Keyboard | Touch / Mobile |
| :--- | :--- | :--- |
| **Steer AG-Craft** | `A` / `D` or `◀` / `▶` | Left / Right D-Pad |
| **Airbrake Drift** | `S` or `▼` | `[DRFT]` Button |
| **Supersonic Jump** | `SPACE` or `▲` / `W` | Jump (`SPACE`) |
| **Ion Afterburner** | `SHIFT` or `E` | `[BOOST]` Button |
| **Comms Audio** | Click `COMMS // LINKED` | Tap HUD Toggle |
| **Optics Pipeline** | Click `OPTICS // HDR` | Tap HUD Toggle |

---

## 🛠 Tech Stack
- **Graphics Engine**: Three.js (r128)
- **Post-Processing**: Three.js EffectComposer, UnrealBloomPass, Custom GLSL ShaderPass
- **Tone Mapping**: ACESFilmicToneMapping (Exposure: 1.2)
- **Audio Synthesizer**: Web Audio API (Procedural multi-oscillator breakbeat engine) & Web Speech API
- **Deployment**: GitHub Pages (Fastly CDN)
