import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
  <title>WIPEOUT // OVERDRIVE - ANTI-GRAVITY RACING (AAA EDITION)</title>
  <meta name="description" content="Next-Gen Anti-Gravity Arcade Racing with Industrial Sci-Fi Art Direction, PBR Wet Asphalt, Airbrake Drifting, and Industrial Breakbeat Audio.">
  <style>
    :root {
      --tech-orange: #ff6a00;
      --tech-cyan: #00f0ff;
      --tech-amber: #ffaa00;
      --tech-red: #ff1e38;
      --tech-green: #00ff66;
      --carbon-bg: rgba(10, 12, 16, 0.85);
      --font-mono: 'SF Mono', 'Roboto Mono', 'Fira Code', 'Consolas', monospace;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      user-select: none;
      -webkit-user-select: none;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    }

    html, body {
      width: 100%;
      height: 100%;
      overflow: hidden;
      background-color: #040608;
      color: #fff;
    }

    #canvas-container {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 1;
    }

    /* --- TACTICAL AEROSPACE HUD OVERLAY --- */
    #hud-overlay {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      z-index: 10;
      pointer-events: none;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 24px 32px;
    }

    .hud-top-bar {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 16px;
    }

    .tech-panel {
      background: var(--carbon-bg);
      border: 1px solid rgba(255, 255, 255, 0.15);
      border-left: 3px solid var(--tech-orange);
      border-radius: 4px;
      padding: 10px 18px;
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.6);
      pointer-events: auto;
    }

    .telemetry-label {
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 2px;
      color: #8a9ba8;
      text-transform: uppercase;
      margin-bottom: 2px;
    }

    .telemetry-value {
      font-family: var(--font-mono);
      font-size: 28px;
      font-weight: 900;
      font-variant-numeric: tabular-nums;
      letter-spacing: 2px;
      color: #ffffff;
      text-shadow: 0 0 16px rgba(255, 106, 0, 0.6);
    }

    .telemetry-sub {
      font-family: var(--font-mono);
      font-size: 10px;
      color: #728496;
      letter-spacing: 1.5px;
      margin-top: 3px;
    }

    .top-right-cluster {
      display: flex;
      flex-direction: column;
      align-items: flex-end;
      gap: 10px;
    }

    .drift-multiplier-box {
      background: var(--carbon-bg);
      border: 1px solid rgba(0, 240, 255, 0.35);
      border-right: 3px solid var(--tech-cyan);
      border-radius: 4px;
      padding: 8px 16px;
      display: flex;
      align-items: baseline;
      gap: 8px;
    }

    .drift-mult-label {
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: var(--tech-cyan);
    }

    .drift-mult-val {
      font-family: var(--font-mono);
      font-size: 22px;
      font-weight: 900;
      color: #fff;
      text-shadow: 0 0 12px var(--tech-cyan);
    }

    .hud-btn-row {
      display: flex;
      gap: 8px;
    }

    .hud-btn {
      background: rgba(16, 20, 28, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #c0cfdb;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 1.5px;
      padding: 6px 12px;
      border-radius: 3px;
      cursor: pointer;
      pointer-events: auto;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .hud-btn:hover {
      background: rgba(255, 106, 0, 0.3);
      border-color: var(--tech-orange);
      color: #fff;
    }

    /* CENTER NOTIFICATIONS & DRIFT TAG */
    #tactical-alert {
      position: absolute;
      top: 18%;
      left: 50%;
      transform: translate(-50%, -50%) scale(0.9);
      font-family: var(--font-mono);
      font-size: 24px;
      font-weight: 900;
      letter-spacing: 5px;
      text-transform: uppercase;
      text-align: center;
      color: var(--tech-orange);
      text-shadow: 0 0 20px rgba(255, 106, 0, 0.8), 0 0 40px rgba(255, 106, 0, 0.4);
      opacity: 0;
      transition: all 0.25s cubic-bezier(0.1, 0.9, 0.2, 1);
      pointer-events: none;
      z-index: 15;
    }

    #tactical-alert.show {
      opacity: 1;
      transform: translate(-50%, -50%) scale(1.05);
    }

    #drift-status-banner {
      position: absolute;
      bottom: 110px;
      left: 50%;
      transform: translateX(-50%);
      background: rgba(0, 240, 255, 0.15);
      border: 1px solid var(--tech-cyan);
      padding: 5px 20px;
      border-radius: 4px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 900;
      letter-spacing: 3px;
      color: var(--tech-cyan);
      text-shadow: 0 0 10px var(--tech-cyan);
      opacity: 0;
      transition: opacity 0.15s ease;
      z-index: 14;
    }

    #drift-status-banner.active {
      opacity: 1;
    }

    /* FLOATING COMBAT TEXT */
    #floating-popups {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      pointer-events: none;
      overflow: hidden;
      z-index: 12;
    }

    .combat-text {
      position: absolute;
      font-family: var(--font-mono);
      font-weight: 900;
      font-size: 16px;
      letter-spacing: 2px;
      text-shadow: 0 0 10px currentColor;
      animation: combatFloat 1.1s forwards cubic-bezier(0.1, 0.9, 0.2, 1);
      transform: translate(-50%, -50%);
    }

    @keyframes combatFloat {
      0% { opacity: 0; transform: translate(-50%, 0) scale(0.7); }
      15% { opacity: 1; transform: translate(-50%, -15px) scale(1.1); }
      80% { opacity: 1; transform: translate(-50%, -40px) scale(1.0); }
      100% { opacity: 0; transform: translate(-50%, -60px) scale(0.9); }
    }

    /* BOTTOM TELEMETRY BAR */
    .hud-bottom-bar {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      gap: 16px;
    }

    .capacitor-panel {
      min-width: 270px;
      padding: 10px 16px;
    }

    .capacitor-header {
      display: flex;
      justify-content: space-between;
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 800;
      letter-spacing: 1.5px;
      color: #8a9ba8;
      margin-bottom: 6px;
    }

    .capacitor-track {
      width: 100%;
      height: 8px;
      background: rgba(255, 255, 255, 0.1);
      border-radius: 2px;
      overflow: hidden;
      border: 1px solid rgba(255, 106, 0, 0.3);
      position: relative;
    }

    .capacitor-fill {
      height: 100%;
      width: 50%;
      background: linear-gradient(90deg, #ff3b00, var(--tech-orange), #ffdd00);
      box-shadow: 0 0 12px var(--tech-orange);
      transition: width 0.1s linear;
    }

    /* CENTER SPEEDOMETER GAUGE */
    .speedo-panel {
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 160px;
      padding: 8px 18px;
      background: var(--carbon-bg);
      border-bottom: 3px solid var(--tech-orange);
    }

    .speedo-val {
      font-family: var(--font-mono);
      font-size: 38px;
      font-weight: 900;
      line-height: 0.95;
      color: #fff;
      text-shadow: 0 0 16px rgba(255, 106, 0, 0.6);
      letter-spacing: 2px;
    }

    .speedo-unit {
      font-family: var(--font-mono);
      font-size: 9px;
      font-weight: 800;
      letter-spacing: 2px;
      color: var(--tech-orange);
      margin-top: 3px;
    }

    .gforce-val {
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      color: #8a9ba8;
      letter-spacing: 1px;
      margin-top: 2px;
    }

    .systems-panel {
      display: flex;
      flex-direction: column;
      gap: 6px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1px;
      padding: 10px 16px;
      border-left: 3px solid var(--tech-cyan);
    }

    .system-row {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .system-dot {
      width: 7px;
      height: 7px;
      border-radius: 2px;
      background-color: #555;
    }

    /* TOUCH CONTROLS FOR MOBILE */
    #touch-controls {
      display: none;
      position: absolute;
      bottom: 20px;
      left: 0;
      width: 100%;
      padding: 0 24px;
      justify-content: space-between;
      pointer-events: none;
      z-index: 20;
    }

    .touch-cluster {
      display: flex;
      gap: 14px;
      pointer-events: auto;
    }

    .touch-btn {
      width: 64px;
      height: 64px;
      border-radius: 8px;
      background: rgba(14, 18, 26, 0.85);
      border: 1px solid var(--tech-orange);
      color: #fff;
      font-family: var(--font-mono);
      font-size: 22px;
      font-weight: 900;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6);
      touch-action: manipulation;
    }

    .touch-btn:active {
      background: rgba(255, 106, 0, 0.4);
      transform: scale(0.94);
    }

    .touch-btn-boost {
      border-color: var(--tech-orange);
      color: var(--tech-orange);
    }

    .touch-btn-drift {
      border-color: var(--tech-cyan);
      color: var(--tech-cyan);
    }

    @media (hover: none) and (pointer: coarse), (max-width: 800px) {
      #touch-controls {
        display: flex;
      }
      .hud-bottom-bar {
        margin-bottom: 85px;
      }
      .capacitor-panel {
        min-width: 200px;
      }
      .telemetry-value {
        font-size: 24px;
      }
    }

    /* MODAL PANELS */
    .modal-backdrop {
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      background: rgba(4, 6, 9, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 50;
      transition: opacity 0.3s ease;
    }

    .modal-backdrop.hidden {
      opacity: 0;
      pointer-events: none;
    }

    .modal-box {
      background: rgba(12, 15, 20, 0.95);
      border: 1px solid rgba(255, 106, 0, 0.5);
      border-top: 4px solid var(--tech-orange);
      box-shadow: 0 0 50px rgba(0, 0, 0, 0.8), 0 0 30px rgba(255, 106, 0, 0.2);
      border-radius: 6px;
      padding: 36px 44px;
      max-width: 550px;
      width: 90%;
      text-align: center;
      position: relative;
    }

    .game-title {
      font-family: var(--font-mono);
      font-size: 32px;
      font-weight: 900;
      letter-spacing: 5px;
      color: #fff;
      text-transform: uppercase;
      text-shadow: 0 0 20px rgba(255, 106, 0, 0.7);
      margin-bottom: 4px;
    }

    .game-subtitle {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 800;
      color: var(--tech-orange);
      letter-spacing: 4px;
      text-transform: uppercase;
      margin-bottom: 24px;
    }

    .instructions-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
      margin-bottom: 28px;
      text-align: left;
    }

    .instruction-item {
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-left: 3px solid var(--tech-cyan);
      border-radius: 4px;
      padding: 10px 14px;
    }

    .instruction-key {
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 800;
      color: #ffffff;
      letter-spacing: 1px;
      margin-bottom: 2px;
    }

    .instruction-desc {
      font-size: 12px;
      color: #8fa0af;
      line-height: 1.35;
    }

    .action-btn {
      background: linear-gradient(135deg, var(--tech-orange), #d04500);
      border: none;
      border-radius: 4px;
      color: #fff;
      font-family: var(--font-mono);
      font-size: 16px;
      font-weight: 900;
      letter-spacing: 3px;
      padding: 14px 44px;
      cursor: pointer;
      box-shadow: 0 0 25px rgba(255, 106, 0, 0.5);
      transition: all 0.2s ease;
      text-transform: uppercase;
    }

    .action-btn:hover {
      transform: scale(1.04);
      box-shadow: 0 0 35px var(--tech-orange);
    }

    .action-btn:active {
      transform: scale(0.97);
    }

    .gameover-stats {
      margin: 20px 0 28px;
      display: flex;
      justify-content: space-around;
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding: 16px 0;
    }

    .go-stat-val {
      font-family: var(--font-mono);
      font-size: 26px;
      font-weight: 900;
      color: var(--tech-orange);
    }

    .go-stat-lbl {
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 800;
      color: #6a7c8c;
      letter-spacing: 1.5px;
      text-transform: uppercase;
      margin-top: 4px;
    }
  </style>
  <script src="three.min.js"></script>
  <script src="postprocessing.bundle.js"></script>
</head>
<body>
  <div id="canvas-container"></div>

  <!-- FLOATING COMBAT & DRIFT POPUPS -->
  <div id="floating-popups"></div>

  <!-- AIRBRAKE DRIFTING INDICATOR -->
  <div id="drift-status-banner">⚡ AIRBRAKE DRIFT // MULTIPLIER +SPEED</div>

  <!-- TACTICAL AEROSPACE HUD -->
  <div id="hud-overlay">
    <div class="hud-top-bar">
      <div class="tech-panel">
        <div class="telemetry-label">TELEMETRY SCORE</div>
        <div class="telemetry-value" id="hud-score">000000</div>
        <div class="telemetry-sub" id="hud-highscore">RECORD // 000000</div>
      </div>

      <div class="top-right-cluster">
        <div class="drift-multiplier-box">
          <span class="drift-mult-label">G-FLOW</span>
          <span class="drift-mult-val" id="hud-multiplier">x1.0</span>
        </div>

        <div class="hud-btn-row">
          <button class="hud-btn" id="btn-audio-toggle">COMMS // LINKED</button>
          <button class="hud-btn" id="btn-bloom-toggle">OPTICS // HDR</button>
        </div>
      </div>
    </div>

    <div id="tactical-alert">AFTERBURNER ACTIVE</div>

    <div class="hud-bottom-bar">
      <div class="tech-panel capacitor-panel">
        <div class="capacitor-header">
          <span>ION AFTERBURNER</span>
          <span id="boost-status-text" style="color: var(--tech-orange);">READY [SHIFT]</span>
        </div>
        <div class="capacitor-track">
          <div class="capacitor-fill" id="boost-bar"></div>
        </div>
      </div>

      <div class="speedo-panel">
        <div class="speedo-val" id="hud-speed">180</div>
        <div class="speedo-unit">KM / H</div>
        <div class="gforce-val" id="hud-mach">MACH 0.35 // 1.2G</div>
      </div>

      <div class="tech-panel systems-panel">
        <div class="system-row">
          <div class="system-dot" id="shield-indicator"></div>
          <span>KINETIC DEFENSE: <b id="shield-status" style="color: #6a7c8c;">OFFLINE</b></span>
        </div>
        <div class="system-row">
          <div class="system-dot" id="airbrake-indicator" style="background-color: var(--tech-cyan); box-shadow: 0 0 6px var(--tech-cyan);"></div>
          <span>AIRBRAKE SYSTEM: <b id="airbrake-status" style="color: var(--tech-cyan);">ACTIVE</b></span>
        </div>
      </div>
    </div>
  </div>

  <!-- MOBILE VIRTUAL CONTROLS -->
  <div id="touch-controls">
    <div class="touch-cluster">
      <button class="touch-btn" id="btn-touch-left">◀</button>
      <button class="touch-btn" id="btn-touch-right">▶</button>
    </div>
    <div class="touch-cluster">
      <button class="touch-btn touch-btn-drift" id="btn-touch-drift">DRFT</button>
      <button class="touch-btn touch-btn-boost" id="btn-touch-boost">BOOST</button>
    </div>
  </div>

  <!-- LAUNCH MODAL -->
  <div class="modal-backdrop" id="start-modal">
    <div class="modal-box">
      <div class="game-title">WIPEOUT // OVERDRIVE</div>
      <div class="game-subtitle">ANTI-GRAVITY INDUSTRIAL LEAGUE</div>

      <div class="instructions-grid">
        <div class="instruction-item">
          <div class="instruction-key">A / D or ◀ / ▶</div>
          <div class="instruction-desc">Steer AG-Craft with Hydraulic Elevons</div>
        </div>
        <div class="instruction-item">
          <div class="instruction-key">S or ▼ or [DRFT]</div>
          <div class="instruction-desc">Airbrake Drift around corners for multiplier</div>
        </div>
        <div class="instruction-item">
          <div class="instruction-key">SPACE / ▲</div>
          <div class="instruction-desc">Supersonic Jump over Blast Doors</div>
        </div>
        <div class="instruction-item">
          <div class="instruction-key">SHIFT or [BOOST]</div>
          <div class="instruction-desc">Engage Ion Afterburner (Smash Barriers)</div>
        </div>
      </div>

      <button class="action-btn" id="btn-start">ENGAGE AG-ENGINE</button>
    </div>
  </div>

  <!-- CRITICAL IMPACT MODAL -->
  <div class="modal-backdrop hidden" id="gameover-modal">
    <div class="modal-box">
      <div class="game-title" style="color: var(--tech-red); text-shadow: 0 0 20px var(--tech-red);">HULL INTEGRITY COMPROMISED</div>
      <div class="game-subtitle">FLIGHT RECOVERY TERMINATED</div>

      <div class="gameover-stats">
        <div>
          <div class="go-stat-val" id="go-score">0</div>
          <div class="go-stat-lbl">Telemetry Score</div>
        </div>
        <div>
          <div class="go-stat-val" id="go-distance">0m</div>
          <div class="go-stat-lbl">Sector Cleared</div>
        </div>
        <div>
          <div class="go-stat-val" id="go-cubes">0</div>
          <div class="go-stat-lbl">Cores Harvested</div>
        </div>
      </div>

      <button class="action-btn" id="btn-restart">RELAUNCH CRAFT</button>
    </div>
  </div>

  <script>
    /* =========================================================================
       WIPEOUT // OVERDRIVE - INDUSTRIAL SCI-FI ANTI-GRAVITY RACING ENGINE
       ========================================================================= */

    // --- 1. PROCEDURAL INDUSTRIAL BREAKBEAT & HYDRAULIC AUDIO ENGINE ---
    class IndustrialAudioEngine {
      constructor() {
        this.ctx = null;
        this.isMuted = false;
        this.bgmPlaying = false;
        this.turbineOsc = null;
        this.subDroneOsc = null;
        this.engineGain = null;
        this.lastSpoken = 0;
      }

      init() {
        if (!this.ctx) {
          const AudioCtx = window.AudioContext || window.webkitAudioContext;
          this.ctx = new AudioCtx();
        }
        if (this.ctx.state === 'suspended') {
          this.ctx.resume();
        }
      }

      speak(text) {
        if (this.isMuted) return;
        const now = Date.now();
        if (now - this.lastSpoken < 1600) return;
        this.lastSpoken = now;

        if ('speechSynthesis' in window) {
          try {
            window.speechSynthesis.cancel();
            const utter = new SpeechSynthesisUtterance(text);
            utter.rate = 1.15;
            utter.pitch = 0.95;
            utter.volume = 0.9;
            const voices = window.speechSynthesis.getVoices();
            const aeroVoice = voices.find(v => v.lang.startsWith('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('David')));
            if (aeroVoice) utter.voice = aeroVoice;
            window.speechSynthesis.speak(utter);
          } catch(e) {}
        }
      }

      startBGM() {
        if (!this.ctx || this.bgmPlaying || this.isMuted) return;
        this.bgmPlaying = true;
        this.initEngineSound();
        this.startBreakbeatLoop();
      }

      stopBGM() {
        this.bgmPlaying = false;
        if (this.engineGain) {
          try {
            this.engineGain.gain.setValueAtTime(0, this.ctx.currentTime);
          } catch(e){}
        }
      }

      initEngineSound() {
        if (!this.ctx) return;
        try {
          const now = this.ctx.currentTime;
          this.turbineOsc = this.ctx.createOscillator();
          this.turbineOsc.type = 'sawtooth';
          this.turbineOsc.frequency.setValueAtTime(110, now);

          this.subDroneOsc = this.ctx.createOscillator();
          this.subDroneOsc.type = 'sine';
          this.subDroneOsc.frequency.setValueAtTime(55, now);

          const filter = this.ctx.createBiquadFilter();
          filter.type = 'lowpass';
          filter.frequency.setValueAtTime(450, now);

          this.engineGain = this.ctx.createGain();
          this.engineGain.gain.setValueAtTime(this.isMuted ? 0 : 0.08, now);

          this.turbineOsc.connect(filter);
          this.subDroneOsc.connect(filter);
          filter.connect(this.engineGain);
          this.engineGain.connect(this.ctx.destination);

          this.turbineOsc.start();
          this.subDroneOsc.start();
        } catch(e){}
      }

      updateEnginePitch(speedRatio, isBoosting, isDrifting) {
        if (!this.turbineOsc || !this.ctx || !this.bgmPlaying) return;
        const targetFreq = 110 + speedRatio * 220 + (isBoosting ? 120 : 0) + (isDrifting ? -30 : 0);
        this.turbineOsc.frequency.setTargetAtTime(targetFreq, this.ctx.currentTime, 0.08);
        this.subDroneOsc.frequency.setTargetAtTime(55 + speedRatio * 35, this.ctx.currentTime, 0.08);
      }

      startBreakbeatLoop() {
        if (!this.ctx) return;
        const bpm = 134;
        const stepTime = 60 / bpm / 4;
        let step = 0;
        const bassLine = [48, 48, 0, 48, 51, 0, 48, 0, 46, 46, 0, 53, 48, 0, 50, 48];

        const scheduleTick = () => {
          if (!this.bgmPlaying) return;
          const now = this.ctx.currentTime;

          if (step === 0 || step === 6 || step === 10) this.playIndustrialKick(now);
          if (step === 4 || step === 12) this.playHeavySnare(now);
          if (step % 2 === 1) this.playMetalHat(now, step % 4 === 1);

          const note = bassLine[step % bassLine.length];
          if (note > 0) this.playReeseBass(now, note);

          step = (step + 1) % 16;
          setTimeout(scheduleTick, stepTime * 1000);
        };

        scheduleTick();
      }

      playIndustrialKick(time) {
        if (this.isMuted || !this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.frequency.setValueAtTime(160, time);
        osc.frequency.exponentialRampToValueAtTime(32, time + 0.16);
        gain.gain.setValueAtTime(0.35, time);
        gain.gain.exponentialRampToValueAtTime(0.001, time + 0.2);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(time);
        osc.stop(time + 0.22);
      }

      playHeavySnare(time) {
        if (this.isMuted || !this.ctx) return;
        const bufferSize = this.ctx.sampleRate * 0.18;
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;
        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;

        const filter = this.ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(1200, time);
        filter.Q.setValueAtTime(3.0, time);

        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0.25, time);
        gain.gain.exponentialRampToValueAtTime(0.001, time + 0.16);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);
        noise.start(time);
        noise.stop(time + 0.18);
      }

      playMetalHat(time, open = false) {
        if (this.isMuted || !this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'square';
        osc.frequency.setValueAtTime(open ? 7500 : 9000, time);
        const dur = open ? 0.08 : 0.035;
        gain.gain.setValueAtTime(0.04, time);
        gain.gain.exponentialRampToValueAtTime(0.0001, time + dur);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(time);
        osc.stop(time + dur + 0.01);
      }

      playReeseBass(time, midiNote) {
        if (this.isMuted || !this.ctx) return;
        const freq = 440 * Math.pow(2, (midiNote - 69) / 12);
        const osc1 = this.ctx.createOscillator();
        const osc2 = this.ctx.createOscillator();
        const filter = this.ctx.createBiquadFilter();
        const gain = this.ctx.createGain();

        osc1.type = 'sawtooth';
        osc2.type = 'sawtooth';
        osc1.frequency.setValueAtTime(freq, time);
        osc2.frequency.setValueAtTime(freq * 1.015, time);

        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(600, time);
        filter.frequency.exponentialRampToValueAtTime(180, time + 0.15);

        gain.gain.setValueAtTime(0.2, time);
        gain.gain.exponentialRampToValueAtTime(0.001, time + 0.16);

        osc1.connect(filter);
        osc2.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);

        osc1.start(time);
        osc2.start(time);
        osc1.stop(time + 0.18);
        osc2.stop(time + 0.18);
      }

      playAirbrakeHiss() {
        if (this.isMuted || !this.ctx) return;
        const now = this.ctx.currentTime;
        const bufferSize = this.ctx.sampleRate * 0.12;
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const data = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) data[i] = Math.random() * 2 - 1;
        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;

        const filter = this.ctx.createBiquadFilter();
        filter.type = 'highpass';
        filter.frequency.setValueAtTime(2400, now);

        const gain = this.ctx.createGain();
        gain.gain.setValueAtTime(0.12, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.11);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.ctx.destination);
        noise.start(now);
        noise.stop(now + 0.12);
      }

      playSonicBoom() {
        if (this.isMuted || !this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(380, now);
        osc.frequency.exponentialRampToValueAtTime(30, now + 0.45);
        gain.gain.setValueAtTime(0.45, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.52);
      }

      playJump() {
        if (this.isMuted || !this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(240, now);
        osc.frequency.exponentialRampToValueAtTime(800, now + 0.24);
        gain.gain.setValueAtTime(0.28, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.24);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.26);
      }

      playCollect() {
        if (this.isMuted || !this.ctx) return;
        const now = this.ctx.currentTime;
        [440, 554.37, 659.25, 880].forEach((freq, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, now + idx * 0.035);
          gain.gain.setValueAtTime(0.18, now + idx * 0.035);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.035 + 0.16);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + idx * 0.035);
          osc.stop(now + idx * 0.035 + 0.18);
        });
      }

      playShieldBreak() {
        if (this.isMuted || !this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(650, now);
        osc.frequency.exponentialRampToValueAtTime(80, now + 0.35);
        gain.gain.setValueAtTime(0.4, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.4);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.42);
      }

      playCrash() {
        if (this.isMuted || !this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(140, now);
        osc.frequency.exponentialRampToValueAtTime(20, now + 0.65);
        gain.gain.setValueAtTime(0.55, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.7);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.75);
      }

      toggleMute() {
        this.isMuted = !this.isMuted;
        if (this.engineGain && this.ctx) {
          this.engineGain.gain.setValueAtTime(this.isMuted ? 0 : 0.08, this.ctx.currentTime);
        }
        return !this.isMuted;
      }
    }

    const sound = new IndustrialAudioEngine();

    // --- 2. CUSTOM POST-PROCESSING GLSL SHADER ---
    const WipeoutPostShader = {
      uniforms: {
        tDiffuse: { value: null },
        uTime: { value: 0 },
        uBoost: { value: 0 },
        uDrift: { value: 0 },
        uAberration: { value: 0 },
        uGlitch: { value: 0 },
        uResolution: { value: new THREE.Vector2(window.innerWidth, window.innerHeight) }
      },
      vertexShader: `
        varying vec2 vUv;
        void main() {
          vUv = uv;
          gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0);
        }
      `,
      fragmentShader: `
        uniform sampler2D tDiffuse;
        uniform float uTime;
        uniform float uBoost;
        uniform float uDrift;
        uniform float uAberration;
        uniform float uGlitch;
        uniform vec2 uResolution;
        varying vec2 vUv;

        float rand(vec2 co){
          return fract(sin(dot(co.xy ,vec2(12.9898,78.233))) * 43758.5453);
        }

        void main() {
          vec2 uv = vUv;

          if (uGlitch > 0.01) {
            float slice = step(0.95, sin(uv.y * 40.0 + uTime * 30.0));
            uv.x += (rand(vec2(uTime, uv.y)) - 0.5) * 0.03 * uGlitch * slice;
          }

          vec2 center = vec2(0.5, 0.5);
          vec2 dir = uv - center;
          float dist = length(dir);

          float edgeFalloff = pow(dist * 1.3, 2.4);
          float abAmount = (uAberration * 0.005 + uBoost * 0.004 + uDrift * 0.002) * edgeFalloff;

          vec2 redUv = uv + dir * abAmount;
          vec2 greenUv = uv;
          vec2 blueUv = uv - dir * abAmount;

          float r = texture2D(tDiffuse, redUv).r;
          float g = texture2D(tDiffuse, greenUv).g;
          float b = texture2D(tDiffuse, blueUv).b;

          vec3 color = vec3(r, g, b);

          float blurStrength = uBoost * 0.28 + uDrift * 0.14;
          if (blurStrength > 0.02) {
            vec3 blurCol = vec3(0.0);
            const int samples = 5;
            for (int i = 0; i < samples; i++) {
              float scale = 1.0 - (float(i) / float(samples)) * 0.035 * blurStrength;
              blurCol += texture2D(tDiffuse, center + dir * scale).rgb;
            }
            color = mix(color, blurCol / float(samples), blurStrength * 0.4);
          }

          float vignette = smoothstep(0.95, 0.45, dist);
          color *= vignette;

          float scanline = sin(uv.y * uResolution.y * 1.4) * 0.018;
          color -= scanline;

          gl_FragColor = vec4(color, 1.0);
        }
      `
    };

    // --- 3. PROCEDURAL PBR TEXTURES (TEXTURED WET ASPHALT HIGHWAY) ---
    function generateWetAsphaltTexture() {
      const canvas = document.createElement('canvas');
      canvas.width = 1024;
      canvas.height = 1024;
      const ctx = canvas.getContext('2d');

      ctx.fillStyle = '#0a0d12';
      ctx.fillRect(0, 0, 1024, 1024);

      const imgData = ctx.getImageData(0, 0, 1024, 1024);
      const data = imgData.data;
      for (let i = 0; i < data.length; i += 4) {
        const noise = (Math.random() - 0.5) * 22;
        data[i] = Math.max(0, Math.min(255, data[i] + noise));
        data[i + 1] = Math.max(0, Math.min(255, data[i + 1] + noise));
        data[i + 2] = Math.max(0, Math.min(255, data[i + 2] + noise));
      }
      ctx.putImageData(imgData, 0, 0);

      // Procedural worn damp dashed centerline
      ctx.fillStyle = 'rgba(255, 170, 0, 0.45)';
      for (let y = 0; y < 1024; y += 128) {
        ctx.fillRect(508, y + 16, 8, 80);
      }

      // Lateral white guide dashes
      ctx.fillStyle = 'rgba(255, 255, 255, 0.25)';
      for (let y = 0; y < 1024; y += 128) {
        ctx.fillRect(200, y + 20, 4, 70);
        ctx.fillRect(820, y + 20, 4, 70);
      }

      // Concrete expansion seams
      ctx.fillStyle = 'rgba(0, 0, 0, 0.75)';
      ctx.fillRect(0, 510, 1024, 4);

      const tex = new THREE.CanvasTexture(canvas);
      tex.wrapS = THREE.RepeatWrapping;
      tex.wrapT = THREE.RepeatWrapping;
      tex.repeat.set(1, 4);
      return tex;
    }

    function generateIndustrialSignTexture(title, code, color = '#ff6a00') {
      const canvas = document.createElement('canvas');
      canvas.width = 512;
      canvas.height = 128;
      const ctx = canvas.getContext('2d');

      ctx.fillStyle = '#080a0f';
      ctx.fillRect(0, 0, 512, 128);

      ctx.fillStyle = color;
      ctx.fillRect(6, 6, 12, 116);
      ctx.fillRect(494, 6, 12, 116);

      ctx.font = '900 28px monospace';
      ctx.fillStyle = color;
      ctx.shadowColor = color;
      ctx.shadowBlur = 10;
      ctx.fillText(title, 36, 52);

      ctx.font = '700 16px monospace';
      ctx.fillStyle = '#8a9ba8';
      ctx.shadowBlur = 0;
      ctx.fillText(code, 36, 92);

      const tex = new THREE.CanvasTexture(canvas);
      tex.needsUpdate = true;
      return tex;
    }

    const asphaltTex = generateWetAsphaltTexture();
    const gantrySignTex1 = generateIndustrialSignTexture('SECTOR 04 // MAG-ACCEL', 'CAUTION: HIGH VOLTAGE GRID', '#ff6a00');
    const gantrySignTex2 = generateIndustrialSignTexture('ORBITAL SKYWAY 09', 'MAX REC SPEED: 380 KM/H', '#00f0ff');
    const gantrySignTex3 = generateIndustrialSignTexture('HAZARD DETECTED', 'AUTOMATED BLAST SYSTEM', '#ff1e38');
    const gantrySignTextures = [gantrySignTex1, gantrySignTex2, gantrySignTex3];

    // --- 4. THREE.JS SCENE SETUP & EFFECT COMPOSER ---
    const container = document.getElementById('canvas-container');
    const scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x040608, 0.009);

    const camera = new THREE.PerspectiveCamera(65, window.innerWidth / window.innerHeight, 0.1, 700);
    camera.position.set(0, 3.8, 8.5);

    const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.2;
    container.appendChild(renderer.domElement);

    let useBloom = true;
    const composer = new THREE.EffectComposer(renderer);
    const renderPass = new THREE.RenderPass(scene, camera);
    composer.addPass(renderPass);

    const bloomPass = new THREE.UnrealBloomPass(
      new THREE.Vector2(window.innerWidth, window.innerHeight),
      0.75,
      0.35,
      0.82
    );
    composer.addPass(bloomPass);

    const wipeoutPass = new THREE.ShaderPass(WipeoutPostShader);
    wipeoutPass.renderToScreen = true;
    composer.addPass(wipeoutPass);

    // Symmetric Balanced Lighting (No unbalanced side flare)
    const ambientLight = new THREE.AmbientLight(0x18202a, 1.3);
    scene.add(ambientLight);

    const overheadLight = new THREE.DirectionalLight(0xffa255, 1.2);
    overheadLight.position.set(0, 35, 10);
    scene.add(overheadLight);

    const rimLightL = new THREE.DirectionalLight(0x00d0ff, 0.65);
    rimLightL.position.set(-22, 25, -35);
    scene.add(rimLightL);

    const rimLightR = new THREE.DirectionalLight(0xffa255, 0.65);
    rimLightR.position.set(22, 25, -35);
    scene.add(rimLightR);

    // High-Altitude Sky Conduits & Megastructure Towers
    function createAtmosphericMegastructure() {
      const megaGroup = new THREE.Group();
      for (let i = 0; i < 12; i++) {
        const h = 180;
        const towerGeo = new THREE.BoxGeometry(18, h, 24);
        const towerMat = new THREE.MeshStandardMaterial({
          color: 0x080a0e,
          roughness: 0.85,
          metalness: 0.25
        });
        const towerL = new THREE.Mesh(towerGeo, towerMat);
        towerL.position.set(-65 - (i % 3) * 15, h / 2 - 20, -i * 65);
        megaGroup.add(towerL);

        const towerR = new THREE.Mesh(towerGeo, towerMat);
        towerR.position.set(65 + (i % 3) * 15, h / 2 - 20, -i * 65);
        megaGroup.add(towerR);

        const beaconGeo = new THREE.SphereGeometry(0.6, 8, 8);
        const beaconMat = new THREE.MeshBasicMaterial({ color: 0xff1e38 });
        const beaconL = new THREE.Mesh(beaconGeo, beaconMat);
        beaconL.position.set(-65 - (i % 3) * 15, h - 20, -i * 65);
        megaGroup.add(beaconL);
      }
      scene.add(megaGroup);
    }
    createAtmosphericMegastructure();

    // Volumetric Rain & Atmosphere Mist
    const rainCount = 900;
    const rainGeo = new THREE.BufferGeometry();
    const rainPos = new Float32Array(rainCount * 3);
    for (let i = 0; i < rainCount * 3; i += 3) {
      rainPos[i] = (Math.random() - 0.5) * 80;
      rainPos[i + 1] = Math.random() * 25;
      rainPos[i + 2] = -Math.random() * 180;
    }
    rainGeo.setAttribute('position', new THREE.BufferAttribute(rainPos, 3));
    const rainMat = new THREE.PointsMaterial({ color: 0x8a9ba8, size: 0.32, transparent: true, opacity: 0.45 });
    const rainPoints = new THREE.Points(rainGeo, rainMat);
    scene.add(rainPoints);

    // --- 5. BESPOKE ANTI-GRAVITY RACING CRAFT WITH MECHANICAL AIRBRAKES ---
    function buildAGCraft() {
      const craft = new THREE.Group();

      const noseShape = new THREE.Shape();
      noseShape.moveTo(0, 2.4);
      noseShape.lineTo(0.7, 0.4);
      noseShape.lineTo(0.9, -1.8);
      noseShape.lineTo(-0.9, -1.8);
      noseShape.lineTo(-0.7, 0.4);
      noseShape.closePath();

      const hullSettings = { depth: 0.45, bevelEnabled: true, bevelSegments: 3, steps: 1, bevelSize: 0.08, bevelThickness: 0.08 };
      const hullGeo = new THREE.ExtrudeGeometry(noseShape, hullSettings);
      const hullMat = new THREE.MeshStandardMaterial({
        color: 0x141820,
        metalness: 0.92,
        roughness: 0.22,
      });
      const hull = new THREE.Mesh(hullGeo, hullMat);
      hull.rotation.x = Math.PI / 2;
      hull.position.y = 0.22;
      craft.add(hull);

      const stripeGeo = new THREE.BoxGeometry(0.35, 0.06, 3.2);
      const stripeMat = new THREE.MeshStandardMaterial({ color: 0xff6a00, roughness: 0.3, metalness: 0.8 });
      const stripe = new THREE.Mesh(stripeGeo, stripeMat);
      stripe.position.set(0, 0.48, -0.2);
      craft.add(stripe);

      const canopyGeo = new THREE.ConeGeometry(0.42, 2.2, 16);
      const canopyMat = new THREE.MeshStandardMaterial({
        color: 0x05080c,
        roughness: 0.05,
        metalness: 0.98,
      });
      const canopy = new THREE.Mesh(canopyGeo, canopyMat);
      canopy.rotation.x = -Math.PI / 2;
      canopy.scale.set(0.9, 0.45, 1.0);
      canopy.position.set(0, 0.52, -0.3);
      craft.add(canopy);

      const podGeo = new THREE.CylinderGeometry(0.32, 0.36, 2.6, 16);
      const podMat = new THREE.MeshStandardMaterial({
        color: 0x181e28,
        metalness: 0.95,
        roughness: 0.18
      });

      const rightPod = new THREE.Mesh(podGeo, podMat);
      rightPod.rotation.x = Math.PI / 2;
      rightPod.position.set(1.15, 0.25, 0.4);
      craft.add(rightPod);

      const leftPod = rightPod.clone();
      leftPod.position.x = -1.15;
      craft.add(leftPod);

      const pylonGeo = new THREE.BoxGeometry(0.65, 0.08, 1.2);
      const pylonR = new THREE.Mesh(pylonGeo, hullMat);
      pylonR.position.set(0.65, 0.25, 0.3);
      craft.add(pylonR);

      const pylonL = pylonR.clone();
      pylonL.position.x = -0.65;
      craft.add(pylonL);

      // Mecha-Grade Articulated Airbrakes
      function buildAirbrakeFlap() {
        const brakeGroup = new THREE.Group();

        const flapGeo = new THREE.BoxGeometry(0.42, 0.05, 0.75);
        const flapMat = new THREE.MeshStandardMaterial({
          color: 0x121620,
          metalness: 0.85,
          roughness: 0.3
        });
        const flap = new THREE.Mesh(flapGeo, flapMat);
        flap.position.set(0, 0, -0.35);
        brakeGroup.add(flap);

        const edgeGeo = new THREE.BoxGeometry(0.44, 0.06, 0.12);
        const edgeMat = new THREE.MeshStandardMaterial({ color: 0xff6a00, roughness: 0.4 });
        const edge = new THREE.Mesh(edgeGeo, edgeMat);
        edge.position.set(0, 0.01, -0.72);
        brakeGroup.add(edge);

        const pistonGeo = new THREE.CylinderGeometry(0.04, 0.04, 0.4, 8);
        const pistonMat = new THREE.MeshStandardMaterial({ color: 0xcccccc, metalness: 0.98, roughness: 0.1 });
        const piston = new THREE.Mesh(pistonGeo, pistonMat);
        piston.position.set(0, -0.15, -0.35);
        brakeGroup.add(piston);

        return brakeGroup;
      }

      const rightBrake = buildAirbrakeFlap();
      rightBrake.position.set(1.15, 0.52, 1.35);
      craft.add(rightBrake);
      craft.rightBrake = rightBrake;

      const leftBrake = buildAirbrakeFlap();
      leftBrake.position.set(-1.15, 0.52, 1.35);
      craft.add(leftBrake);
      craft.leftBrake = leftBrake;

      const nozzleGeo = new THREE.ConeGeometry(0.22, 0.85, 14);
      const nozzleMat = new THREE.MeshBasicMaterial({ color: 0xff6a00 });

      const flameR = new THREE.Mesh(nozzleGeo, nozzleMat);
      flameR.rotation.x = -Math.PI / 2;
      flameR.position.set(1.15, 0.25, 1.85);
      craft.add(flameR);
      craft.flameR = flameR;

      const flameL = flameR.clone();
      flameL.position.x = -1.15;
      craft.add(flameL);
      craft.flameL = flameL;

      const shieldGeo = new THREE.IcosahedronGeometry(2.4, 2);
      const shieldMat = new THREE.MeshBasicMaterial({
        color: 0x00f0ff,
        wireframe: true,
        transparent: true,
        opacity: 0.0
      });
      const shield = new THREE.Mesh(shieldGeo, shieldMat);
      craft.add(shield);
      craft.shieldMesh = shield;

      craft.position.set(0, 0.9, 0);
      return craft;
    }

    const player = buildAGCraft();
    scene.add(player);

    // Dual Engine Ion Trail Particles
    const sparkCount = 90;
    const sparkGeo = new THREE.BufferGeometry();
    const sparkPos = new Float32Array(sparkCount * 3);
    const sparkCol = new Float32Array(sparkCount * 3);
    for (let i = 0; i < sparkCount; i++) {
      sparkPos[i * 3] = (Math.random() - 0.5) * 2.2;
      sparkPos[i * 3 + 1] = 0.9 + (Math.random() - 0.5) * 0.3;
      sparkPos[i * 3 + 2] = 2 + Math.random() * 16;
      sparkCol[i * 3] = 1.0;
      sparkCol[i * 3 + 1] = 0.42;
      sparkCol[i * 3 + 2] = 0.0;
    }
    sparkGeo.setAttribute('position', new THREE.BufferAttribute(sparkPos, 3));
    sparkGeo.setAttribute('color', new THREE.BufferAttribute(sparkCol, 3));
    const sparkMat = new THREE.PointsMaterial({ size: 0.32, vertexColors: true, transparent: true, opacity: 0.85 });
    const thrusterSparks = new THREE.Points(sparkGeo, sparkMat);
    scene.add(thrusterSparks);

    // Drift Lateral Sparks System
    const driftSparkCount = 60;
    const driftSparkGeo = new THREE.BufferGeometry();
    const driftSparkPos = new Float32Array(driftSparkCount * 3);
    for (let i = 0; i < driftSparkCount * 3; i++) driftSparkPos[i] = 999;
    driftSparkGeo.setAttribute('position', new THREE.BufferAttribute(driftSparkPos, 3));
    const driftSparkMat = new THREE.PointsMaterial({ color: 0x00f0ff, size: 0.4, transparent: true, opacity: 0.9 });
    const driftSparks = new THREE.Points(driftSparkGeo, driftSparkMat);
    scene.add(driftSparks);

    // --- 6. INDUSTRIAL HIGHWAY TRACK & OVERHEAD GANTRIES ---
    const ROAD_WIDTH = 15;
    const SEGMENT_LENGTH = 36;
    const TOTAL_SEGMENTS = 14;
    const trackSegments = [];
    const activeObstacles = [];
    const activeCollectibles = [];

    function createSegment(zPos, segmentIndex) {
      const group = new THREE.Group();

      const roadGeo = new THREE.BoxGeometry(ROAD_WIDTH, 0.45, SEGMENT_LENGTH);
      const roadMat = new THREE.MeshStandardMaterial({
        color: 0x12171f,
        map: asphaltTex,
        roughness: 0.48, // Balanced PBR roughness
        metalness: 0.50
      });
      const road = new THREE.Mesh(roadGeo, roadMat);
      road.position.y = -0.22;
      group.add(road);

      const railGeo = new THREE.BoxGeometry(0.45, 0.65, SEGMENT_LENGTH);
      const railMat = new THREE.MeshStandardMaterial({ color: 0x1f2633, metalness: 0.7, roughness: 0.4 });

      const railL = new THREE.Mesh(railGeo, railMat);
      railL.position.set(-ROAD_WIDTH / 2, 0.32, 0);
      group.add(railL);

      const railR = new THREE.Mesh(railGeo, railMat);
      railR.position.set(ROAD_WIDTH / 2, 0.32, 0);
      group.add(railR);

      const stripGeo = new THREE.BoxGeometry(0.08, 0.08, SEGMENT_LENGTH);
      const stripMat = new THREE.MeshBasicMaterial({ color: 0xffaa00 });
      const stripL = new THREE.Mesh(stripGeo, stripMat);
      stripL.position.set(-ROAD_WIDTH / 2 + 0.2, 0.65, 0);
      group.add(stripL);

      const stripR = new THREE.Mesh(stripGeo, stripMat);
      stripR.position.set(ROAD_WIDTH / 2 - 0.2, 0.65, 0);
      group.add(stripR);

      if (segmentIndex % 4 === 0) {
        const gantry = new THREE.Group();
        const archGeo = new THREE.BoxGeometry(ROAD_WIDTH + 4, 0.6, 1.0);
        const archMat = new THREE.MeshStandardMaterial({ color: 0x161c24, metalness: 0.9, roughness: 0.3 });
        const arch = new THREE.Mesh(archGeo, archMat);
        arch.position.y = 7.8;
        gantry.add(arch);

        const pylonGeo = new THREE.CylinderGeometry(0.3, 0.38, 7.8, 8);
        const p1 = new THREE.Mesh(pylonGeo, archMat);
        p1.position.set(-ROAD_WIDTH / 2 - 1.8, 3.9, 0);
        gantry.add(p1);

        const p2 = new THREE.Mesh(pylonGeo, archMat);
        p2.position.set(ROAD_WIDTH / 2 + 1.8, 3.9, 0);
        gantry.add(p2);

        const signGeo = new THREE.PlaneGeometry(10, 2.5);
        const signTex = gantrySignTextures[(segmentIndex / 4) % gantrySignTextures.length];
        const signMat = new THREE.MeshBasicMaterial({ map: signTex, side: THREE.DoubleSide });
        const sign = new THREE.Mesh(signGeo, signMat);
        sign.position.set(0, 7.8, 0.55);
        gantry.add(sign);

        group.add(gantry);
      }

      const subPylonGeo = new THREE.CylinderGeometry(1.6, 2.2, 35, 8);
      const subPylonMat = new THREE.MeshStandardMaterial({ color: 0x0a0c10, roughness: 0.9 });
      const subPylon = new THREE.Mesh(subPylonGeo, subPylonMat);
      subPylon.position.set(0, -17.5, 0);
      group.add(subPylon);

      group.position.z = zPos;
      scene.add(group);
      return group;
    }

    for (let i = 0; i < TOTAL_SEGMENTS; i++) {
      trackSegments.push(createSegment(-i * SEGMENT_LENGTH, i));
    }

    // --- 7. INDUSTRIAL TRACK HAZARDS & ACCEL PADS ---
    function spawnObstacle(z) {
      const lanes = [-4.5, 0, 4.5];
      const lane = lanes[Math.floor(Math.random() * lanes.length)];
      const rand = Math.random();
      const group = new THREE.Group();
      group.lane = lane;
      group.passed = false;

      if (rand < 0.35) {
        group.obstacleType = 'blast_door';
        const doorGeo = new THREE.BoxGeometry(3.6, 1.6, 0.8);
        const doorMat = new THREE.MeshStandardMaterial({
          color: 0x1f242e,
          metalness: 0.85,
          roughness: 0.25
        });
        const door = new THREE.Mesh(doorGeo, doorMat);
        door.position.y = 0.8;
        group.add(door);

        const chevGeo = new THREE.BoxGeometry(3.7, 0.3, 0.85);
        const chevMat = new THREE.MeshBasicMaterial({ color: 0xffaa00 });
        const chev = new THREE.Mesh(chevGeo, chevMat);
        chev.position.y = 0.8;
        group.add(chev);

        const beaconGeo = new THREE.SphereGeometry(0.2, 8, 8);
        const beaconMat = new THREE.MeshBasicMaterial({ color: 0xff1e38 });
        const b = new THREE.Mesh(beaconGeo, beaconMat);
        b.position.set(0, 1.7, 0);
        group.add(b);

        group.hitbox = { w: 3.6, h: 1.6, d: 0.9 };
      } else if (rand < 0.65) {
        group.obstacleType = 'em_arc';
        const pylonGeo = new THREE.CylinderGeometry(0.22, 0.28, 3.8, 8);
        const pylonMat = new THREE.MeshStandardMaterial({ color: 0x161b24, metalness: 0.9 });

        const p1 = new THREE.Mesh(pylonGeo, pylonMat);
        p1.position.set(-1.8, 1.9, 0);
        group.add(p1);

        const p2 = new THREE.Mesh(pylonGeo, pylonMat);
        p2.position.set(1.8, 1.9, 0);
        group.add(p2);

        const arcGeo = new THREE.CylinderGeometry(0.12, 0.12, 3.6, 8);
        const arcMat = new THREE.MeshBasicMaterial({ color: 0x00f0ff });
        const arc = new THREE.Mesh(arcGeo, arcMat);
        arc.rotation.z = Math.PI / 2;
        arc.position.y = 1.9;
        group.add(arc);
        group.arc = arc;

        group.hitbox = { w: 3.6, h: 1.3, d: 0.6, yOffset: 1.9 };
      } else {
        group.obstacleType = 'hauler';
        const haulerGeo = new THREE.BoxGeometry(3.0, 2.4, 6.2);
        const haulerMat = new THREE.MeshStandardMaterial({ color: 0x181e28, metalness: 0.88, roughness: 0.2 });
        const hauler = new THREE.Mesh(haulerGeo, haulerMat);
        hauler.position.y = 1.2;
        group.add(hauler);

        const brakeGeo = new THREE.BoxGeometry(2.6, 0.25, 0.2);
        const brakeMat = new THREE.MeshBasicMaterial({ color: 0xff1e38 });
        const brakeMesh = new THREE.Mesh(brakeGeo, brakeMat);
        brakeMesh.position.set(0, 1.2, 3.15);
        group.add(brakeMesh);

        group.truckSpeed = 24;
        group.hitbox = { w: 3.0, h: 2.4, d: 6.2 };
      }

      group.position.set(lane, 0, z);
      scene.add(group);
      activeObstacles.push(group);
    }

    function spawnAccelPad(z) {
      const lanes = [-4.5, 0, 4.5];
      const lane = lanes[Math.floor(Math.random() * lanes.length)];
      const padGroup = new THREE.Group();
      padGroup.itemType = 'accel_pad';

      const padGeo = new THREE.PlaneGeometry(3.2, 4.2);
      const padMat = new THREE.MeshBasicMaterial({ color: 0xff6a00, side: THREE.DoubleSide });
      const pad = new THREE.Mesh(padGeo, padMat);
      pad.rotation.x = -Math.PI / 2;
      pad.position.y = 0.02;
      padGroup.add(pad);

      padGroup.position.set(lane, 0, z);
      scene.add(padGroup);
      activeCollectibles.push(padGroup);
    }

    function spawnCollectible(z) {
      if (Math.random() < 0.28) {
        spawnAccelPad(z);
        return;
      }

      const lanes = [-4.5, 0, 4.5];
      const lane = lanes[Math.floor(Math.random() * lanes.length)];
      const itemGroup = new THREE.Group();
      const rand = Math.random();

      if (rand < 0.75) {
        itemGroup.itemType = 'cell';
        const geo = new THREE.OctahedronGeometry(0.75, 0);
        const mat = new THREE.MeshStandardMaterial({ color: 0xff6a00, emissive: 0xff4400, emissiveIntensity: 0.9, metalness: 0.8 });
        const core = new THREE.Mesh(geo, mat);
        core.position.y = 1.15;
        itemGroup.add(core);

        const ringGeo = new THREE.TorusGeometry(0.95, 0.06, 8, 24);
        const ringMat = new THREE.MeshBasicMaterial({ color: 0xffaa00 });
        const ring = new THREE.Mesh(ringGeo, ringMat);
        ring.position.y = 1.15;
        itemGroup.add(ring);
        itemGroup.rotator = core;
        itemGroup.ring = ring;
      } else {
        itemGroup.itemType = 'shield';
        const geo = new THREE.IcosahedronGeometry(0.8, 1);
        const mat = new THREE.MeshBasicMaterial({ color: 0x00f0ff, wireframe: true });
        const orb = new THREE.Mesh(geo, mat);
        orb.position.y = 1.25;
        itemGroup.add(orb);
        itemGroup.rotator = orb;
      }

      itemGroup.position.set(lane, 0, z);
      scene.add(itemGroup);
      activeCollectibles.push(itemGroup);
    }

    // --- 8. RACING PHYSICS, DRIFT ENGINE & TELEMETRY ---
    const STATE_MENU = 0;
    const STATE_PLAYING = 1;
    const STATE_GAMEOVER = 2;
    let gameState = STATE_MENU;

    let score = 0;
    let distance = 0;
    let highscore = parseInt(localStorage.getItem('wipeout_overdrive_record') || '0', 10);
    let coresHarvested = 0;
    let baseSpeed = 55;
    let currentSpeed = baseSpeed;
    let targetX = 0;
    let craftX = 0;
    let playerY = 0.9;
    let velocityY = 0;
    let isJumping = false;
    let boostEnergy = 50;
    let isBoosting = false;
    let boostTimer = 0;
    let isDrifting = false;
    let driftFactor = 0;
    let hasShield = false;
    let comboMultiplier = 1.0;
    let comboResetTimer = 0;
    let cameraShake = 0;

    const keys = { left: false, right: false, jump: false, boost: false, drift: false };

    const hudScore = document.getElementById('hud-score');
    const hudHighScore = document.getElementById('hud-highscore');
    const hudMultiplier = document.getElementById('hud-multiplier');
    const hudSpeed = document.getElementById('hud-speed');
    const hudMach = document.getElementById('hud-mach');
    const boostBar = document.getElementById('boost-bar');
    const boostStatusText = document.getElementById('boost-status-text');
    const shieldStatus = document.getElementById('shield-status');
    const shieldIndicator = document.getElementById('shield-indicator');
    const airbrakeStatus = document.getElementById('airbrake-status');
    const airbrakeIndicator = document.getElementById('airbrake-indicator');
    const tacticalAlert = document.getElementById('tactical-alert');
    const driftStatusBanner = document.getElementById('drift-status-banner');
    const floatingPopups = document.getElementById('floating-popups');
    const startModal = document.getElementById('start-modal');
    const gameoverModal = document.getElementById('gameover-modal');

    hudHighScore.textContent = `RECORD // ${String(highscore).padStart(6, '0')}`;

    function showTacticalAlert(text, color = '#ff6a00') {
      tacticalAlert.textContent = text;
      tacticalAlert.style.color = color;
      tacticalAlert.classList.add('show');
      setTimeout(() => tacticalAlert.classList.remove('show'), 900);
    }

    function createCombatPopup(text, color = '#ff6a00', x = window.innerWidth / 2, y = window.innerHeight * 0.45) {
      const el = document.createElement('div');
      el.className = 'combat-text';
      el.textContent = text;
      el.style.color = color;
      el.style.left = `${x}px`;
      el.style.top = `${y}px`;
      floatingPopups.appendChild(el);
      setTimeout(() => el.remove(), 1100);
    }

    const btnAudio = document.getElementById('btn-audio-toggle');
    btnAudio.addEventListener('click', () => {
      const active = sound.toggleMute();
      btnAudio.textContent = active ? 'COMMS // LINKED' : 'COMMS // MUTED';
    });

    const btnBloom = document.getElementById('btn-bloom-toggle');
    btnBloom.addEventListener('click', () => {
      useBloom = !useBloom;
      bloomPass.enabled = useBloom;
      btnBloom.textContent = useBloom ? 'OPTICS // HDR' : 'OPTICS // SDR';
    });

    window.addEventListener('keydown', (e) => {
      sound.init();
      if (e.code === 'KeyA' || e.code === 'ArrowLeft') keys.left = true;
      if (e.code === 'KeyD' || e.code === 'ArrowRight') keys.right = true;
      if (e.code === 'Space' || e.code === 'ArrowUp' || e.code === 'KeyW') {
        keys.jump = true;
        if (gameState === STATE_PLAYING && !isJumping) doJump();
      }
      if (e.code === 'ShiftLeft' || e.code === 'ShiftRight' || e.code === 'KeyE') {
        keys.boost = true;
        triggerBoost();
      }
      if (e.code === 'KeyS' || e.code === 'ArrowDown') keys.drift = true;
    });

    window.addEventListener('keyup', (e) => {
      if (e.code === 'KeyA' || e.code === 'ArrowLeft') keys.left = false;
      if (e.code === 'KeyD' || e.code === 'ArrowRight') keys.right = false;
      if (e.code === 'Space' || e.code === 'ArrowUp' || e.code === 'KeyW') keys.jump = false;
      if (e.code === 'ShiftLeft' || e.code === 'ShiftRight' || e.code === 'KeyE') keys.boost = false;
      if (e.code === 'KeyS' || e.code === 'ArrowDown') keys.drift = false;
    });

    const btnTouchL = document.getElementById('btn-touch-left');
    const btnTouchR = document.getElementById('btn-touch-right');
    const btnTouchDrift = document.getElementById('btn-touch-drift');
    const btnTouchBoost = document.getElementById('btn-touch-boost');

    const bindTouch = (elem, pressFn, releaseFn) => {
      elem.addEventListener('touchstart', (e) => { e.preventDefault(); pressFn(); }, { passive: false });
      elem.addEventListener('touchend', (e) => { e.preventDefault(); releaseFn(); }, { passive: false });
    };

    bindTouch(btnTouchL, () => keys.left = true, () => keys.left = false);
    bindTouch(btnTouchR, () => keys.right = true, () => keys.right = false);
    bindTouch(btnTouchDrift, () => keys.drift = true, () => keys.drift = false);
    bindTouch(btnTouchBoost, () => triggerBoost(), () => keys.boost = false);

    function doJump() {
      if (isJumping) return;
      isJumping = true;
      velocityY = 17.5;
      sound.playJump();
    }

    function triggerBoost() {
      if (isBoosting || boostEnergy < 25) return;
      isBoosting = true;
      boostTimer = 3.5;
      sound.playSonicBoom();
      sound.speak("Afterburner active");
      showTacticalAlert('AFTERBURNER ENGAGED', '#ff6a00');
      wipeoutPass.uniforms.uAberration.value = 0.5;
      cameraShake = 0.45;
    }

    function startGame() {
      sound.init();
      sound.startBGM();
      sound.speak("Systems engaged. Anti-gravity active.");
      gameState = STATE_PLAYING;
      startModal.classList.add('hidden');
      gameoverModal.classList.add('hidden');
      resetGameStats();
    }

    function resetGameStats() {
      score = 0;
      distance = 0;
      coresHarvested = 0;
      currentSpeed = baseSpeed;
      targetX = 0;
      craftX = 0;
      player.position.set(0, 0.9, 0);
      playerY = 0.9;
      velocityY = 0;
      isJumping = false;
      boostEnergy = 50;
      isBoosting = false;
      isDrifting = false;
      hasShield = false;
      comboMultiplier = 1.0;
      player.shieldMesh.material.opacity = 0;
      shieldStatus.textContent = 'OFFLINE';
      shieldStatus.style.color = '#6a7c8c';
      shieldIndicator.style.backgroundColor = '#555';
      shieldIndicator.style.boxShadow = 'none';

      for (const obs of activeObstacles) scene.remove(obs);
      for (const item of activeCollectibles) scene.remove(item);
      activeObstacles.length = 0;
      activeCollectibles.length = 0;

      for (let z = -70; z > -380; z -= 40) {
        if (Math.random() < 0.68) spawnObstacle(z);
        if (Math.random() < 0.6) spawnCollectible(z - 18);
      }
    }

    function gameOver() {
      gameState = STATE_GAMEOVER;
      sound.stopBGM();
      sound.playCrash();
      sound.speak("Critical impact. Flight terminated.");

      cameraShake = 1.3;
      wipeoutPass.uniforms.uGlitch.value = 0.9;
      wipeoutPass.uniforms.uAberration.value = 0.8;

      if (score > highscore) {
        highscore = Math.floor(score);
        localStorage.setItem('wipeout_overdrive_record', highscore);
        hudHighScore.textContent = `RECORD // ${String(highscore).padStart(6, '0')}`;
      }

      document.getElementById('go-score').textContent = Math.floor(score);
      document.getElementById('go-distance').textContent = `${Math.floor(distance)}m`;
      document.getElementById('go-cubes').textContent = coresHarvested;

      setTimeout(() => {
        gameoverModal.classList.remove('hidden');
      }, 750);
    }

    document.getElementById('btn-start').addEventListener('click', startGame);
    document.getElementById('btn-restart').addEventListener('click', startGame);

    // --- 9. MAIN GAME LOOP ---
    const clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);

      const delta = Math.min(clock.getDelta(), 0.05);
      const elapsedTime = clock.getElapsedTime();

      wipeoutPass.uniforms.uTime.value = elapsedTime;
      wipeoutPass.uniforms.uAberration.value = Math.max(0, wipeoutPass.uniforms.uAberration.value - delta * 2.5);
      wipeoutPass.uniforms.uGlitch.value = Math.max(0, wipeoutPass.uniforms.uGlitch.value - delta * 3.0);

      const rainPosArr = rainPoints.geometry.attributes.position.array;
      for (let i = 0; i < rainCount; i++) {
        rainPosArr[i * 3 + 2] += (currentSpeed + 45) * delta;
        if (rainPosArr[i * 3 + 2] > 10) {
          rainPosArr[i * 3 + 2] = -180;
        }
      }
      rainPoints.geometry.attributes.position.needsUpdate = true;

      if (gameState === STATE_PLAYING) {
        const steering = (keys.right ? 1 : 0) - (keys.left ? 1 : 0);
        const driftEngaged = keys.drift && Math.abs(steering) > 0;

        if (driftEngaged && !isDrifting) {
          sound.playAirbrakeHiss();
          isDrifting = true;
          driftStatusBanner.classList.add('active');
        } else if (!driftEngaged && isDrifting) {
          isDrifting = false;
          driftStatusBanner.classList.remove('active');
        }

        driftFactor = THREE.MathUtils.lerp(driftFactor, isDrifting ? 1.0 : 0.0, delta * 8);
        wipeoutPass.uniforms.uDrift.value = driftFactor;

        let speedMult = 1.0;
        if (isBoosting) {
          speedMult = 2.0;
          boostTimer -= delta;
          boostEnergy = Math.max(0, boostEnergy - delta * 25);
          if (boostTimer <= 0 || boostEnergy <= 0) {
            isBoosting = false;
          }
        } else {
          boostEnergy = Math.min(100, boostEnergy + delta * (isDrifting ? 9 : 4.5));
          if (isDrifting) speedMult = 1.15;
        }

        wipeoutPass.uniforms.uBoost.value = THREE.MathUtils.lerp(
          wipeoutPass.uniforms.uBoost.value,
          isBoosting ? 1.0 : 0.0,
          delta * 8
        );

        distance += currentSpeed * speedMult * delta * 0.48;
        baseSpeed = 55 + Math.min(distance * 0.024, 60);
        currentSpeed = baseSpeed * speedMult;

        sound.updateEnginePitch(currentSpeed / 100, isBoosting, isDrifting);

        const currentMultiplier = comboMultiplier * (isDrifting ? 1.8 : 1.0);
        score += currentSpeed * delta * currentMultiplier * (isBoosting ? 2.5 : 1.0);

        if (isDrifting) {
          comboMultiplier = Math.min(5.0, comboMultiplier + delta * 0.45);
          comboResetTimer = 3.5;
        } else if (comboMultiplier > 1.0) {
          comboResetTimer -= delta;
          if (comboResetTimer <= 0) {
            comboMultiplier = Math.max(1.0, comboMultiplier - 0.5);
            comboResetTimer = 2.8;
          }
        }

        const steerSpeed = isDrifting ? 25.0 : 18.0;
        if (keys.left) targetX -= steerSpeed * delta;
        if (keys.right) targetX += steerSpeed * delta;
        targetX = Math.max(-ROAD_WIDTH / 2 + 1.8, Math.min(ROAD_WIDTH / 2 - 1.8, targetX));

        craftX += (targetX - craftX) * (delta * (isDrifting ? 9 : 14));
        player.position.x = craftX;

        const bankAngle = -(targetX - craftX) * (isDrifting ? 0.55 : 0.42);
        player.rotation.z = bankAngle;
        player.rotation.y = bankAngle * 0.35;

        // Realistic Piston Airbrake Deployment (Flap angles upward)
        if (player.leftBrake && player.rightBrake) {
          const leftTarget = (keys.left || isDrifting) ? 0.55 : 0;
          const rightTarget = (keys.right || isDrifting) ? 0.55 : 0;
          player.leftBrake.rotation.x = THREE.MathUtils.lerp(player.leftBrake.rotation.x, leftTarget, delta * 15);
          player.rightBrake.rotation.x = THREE.MathUtils.lerp(player.rightBrake.rotation.x, rightTarget, delta * 15);
        }

        if (isJumping) {
          velocityY -= 44 * delta;
          playerY += velocityY * delta;
          if (playerY <= 0.9) {
            playerY = 0.9;
            isJumping = false;
            velocityY = 0;
            cameraShake = 0.22;
          }
        } else {
          playerY = 0.9 + Math.sin(elapsedTime * 10) * 0.08;
        }
        player.position.y = playerY;

        const flameScaleZ = isBoosting ? 1.8 : (1.0 + Math.sin(elapsedTime * 20) * 0.15);
        player.flameR.scale.y = flameScaleZ;
        player.flameL.scale.y = flameScaleZ;

        const roadMove = currentSpeed * delta;
        for (const seg of trackSegments) {
          seg.position.z += roadMove;
          if (seg.position.z > 25) {
            let minZ = 0;
            for (const s of trackSegments) if (s.position.z < minZ) minZ = s.position.z;
            seg.position.z = minZ - SEGMENT_LENGTH;

            if (Math.random() < 0.7) spawnObstacle(seg.position.z + (Math.random() - 0.5) * 12);
            if (Math.random() < 0.6) spawnCollectible(seg.position.z - 16);
          }
        }

        for (let i = activeObstacles.length - 1; i >= 0; i--) {
          const obs = activeObstacles[i];
          let actualMove = roadMove;
          if (obs.obstacleType === 'hauler') {
            actualMove = (currentSpeed - obs.truckSpeed) * delta;
          }
          obs.position.z += actualMove;

          if (obs.obstacleType === 'em_arc') {
            const flicker = (Math.sin(elapsedTime * 22) + 1) * 0.5;
            obs.arc.material.color.setHex(flicker > 0.3 ? 0x00f0ff : 0xffffff);
          }

          const distZ = Math.abs(obs.position.z - player.position.z);
          const distX = Math.abs(obs.position.x - player.position.x);

          if (!obs.passed && obs.position.z > player.position.z) {
            obs.passed = true;
            if (distX > 1.2 && distX < 3.4 && distZ < 3.2) {
              comboMultiplier = Math.min(5.0, comboMultiplier + 0.5);
              comboResetTimer = 4.0;
              const bonus = Math.round(350 * comboMultiplier);
              score += bonus;
              showTacticalAlert(`NEAR MISS // +${bonus}`, '#00f0ff');
              createCombatPopup(`+${bonus} NEAR MISS`, '#00f0ff');
              wipeoutPass.uniforms.uAberration.value = 0.3;
            }
          }

          if (distZ < 1.5 && distX < (obs.hitbox.w / 2 + 0.5)) {
            let hit = true;
            if (obs.obstacleType === 'blast_door' && player.position.y > 1.8) hit = false;
            if (obs.obstacleType === 'em_arc' && (player.position.y < 0.75 || player.position.y > 2.8)) hit = false;

            if (hit) {
              if (isBoosting) {
                scene.remove(obs);
                activeObstacles.splice(i, 1);
                score += 700;
                createCombatPopup('+700 BLASTED', '#ffaa00');
                cameraShake = 0.45;
                wipeoutPass.uniforms.uAberration.value = 0.45;
                continue;
              }

              if (hasShield) {
                hasShield = false;
                player.shieldMesh.material.opacity = 0;
                shieldStatus.textContent = 'OFFLINE';
                shieldStatus.style.color = '#6a7c8c';
                shieldIndicator.style.backgroundColor = '#555';
                shieldIndicator.style.boxShadow = 'none';
                sound.playShieldBreak();
                sound.speak("Shield compromised");
                showTacticalAlert('SHIELD DEFLECTED IMPACT', '#00f0ff');
                createCombatPopup('SHIELD DEFLECTED', '#00f0ff');
                cameraShake = 0.7;
                wipeoutPass.uniforms.uGlitch.value = 0.5;
                scene.remove(obs);
                activeObstacles.splice(i, 1);
                continue;
              }

              gameOver();
              break;
            }
          }

          if (obs.position.z > 22) {
            scene.remove(obs);
            activeObstacles.splice(i, 1);
          }
        }

        for (let i = activeCollectibles.length - 1; i >= 0; i--) {
          const item = activeCollectibles[i];
          item.position.z += roadMove;

          if (item.rotator) {
            item.rotator.rotation.y += delta * 3.5;
            item.rotator.rotation.x += delta * 1.8;
          }
          if (item.ring) {
            item.ring.rotation.x += delta * 2.2;
            item.ring.rotation.z += delta * 2.8;
          }

          if (item.itemType === 'accel_pad') {
            const distPad = Math.abs(item.position.z - player.position.z);
            const distX = Math.abs(item.position.x - player.position.x);
            if (distPad < 1.8 && distX < 1.6 && player.position.y < 1.4) {
              sound.playSonicBoom();
              sound.speak("Mag-accel launch");
              isBoosting = true;
              boostTimer = 3.0;
              boostEnergy = Math.min(100, boostEnergy + 35);
              score += 600 * comboMultiplier;
              showTacticalAlert('MAG-ACCEL LAUNCH // +600', '#ff6a00');
              createCombatPopup('+600 MAG-ACCEL', '#ff6a00');
              wipeoutPass.uniforms.uAberration.value = 0.6;
              cameraShake = 0.45;
              scene.remove(item);
              activeCollectibles.splice(i, 1);
              continue;
            }
          } else {
            const dist = item.position.distanceTo(player.position);
            if (dist < 2.2) {
              if (item.itemType === 'cell') {
                coresHarvested++;
                const bonus = Math.round(300 * comboMultiplier);
                score += bonus;
                boostEnergy = Math.min(100, boostEnergy + 20);
                sound.playCollect();
                createCombatPopup(`+${bonus} ION CORE`, '#ffaa00');
              } else if (item.itemType === 'shield') {
                hasShield = true;
                player.shieldMesh.material.opacity = 0.45;
                shieldStatus.textContent = 'ONLINE [ACTIVE]';
                shieldStatus.style.color = '#00f0ff';
                shieldIndicator.style.backgroundColor = '#00f0ff';
                shieldIndicator.style.boxShadow = '0 0 8px #00f0ff';
                sound.playCollect();
                sound.speak("Kinetic defense active");
                showTacticalAlert('KINETIC SHIELD ONLINE', '#00f0ff');
                createCombatPopup('SHIELD ONLINE', '#00f0ff');
              }

              scene.remove(item);
              activeCollectibles.splice(i, 1);
              continue;
            }
          }

          if (item.position.z > 22) {
            scene.remove(item);
            activeCollectibles.splice(i, 1);
          }
        }

        const sparkArr = thrusterSparks.geometry.attributes.position.array;
        for (let i = 0; i < sparkCount; i++) {
          sparkArr[i * 3 + 2] += (currentSpeed + 35) * delta;
          if (sparkArr[i * 3 + 2] > 20) {
            const side = Math.random() > 0.5 ? 1.15 : -1.15;
            sparkArr[i * 3] = player.position.x + side + (Math.random() - 0.5) * 0.15;
            sparkArr[i * 3 + 1] = player.position.y + 0.25 + (Math.random() - 0.5) * 0.15;
            sparkArr[i * 3 + 2] = player.position.z + 1.85;
          }
        }
        thrusterSparks.geometry.attributes.position.needsUpdate = true;

        const driftArr = driftSparks.geometry.attributes.position.array;
        if (isDrifting) {
          for (let i = 0; i < driftSparkCount; i++) {
            if (driftArr[i * 3 + 2] > 15 || driftArr[i * 3] > 800) {
              const side = keys.right ? -1.3 : 1.3;
              driftArr[i * 3] = player.position.x + side + (Math.random() - 0.5) * 0.3;
              driftArr[i * 3 + 1] = 0.05 + Math.random() * 0.15;
              driftArr[i * 3 + 2] = player.position.z + 1.2 + Math.random() * 2.0;
            } else {
              driftArr[i * 3 + 2] += currentSpeed * delta * 1.5;
            }
          }
        } else {
          for (let i = 0; i < driftSparkCount * 3; i++) driftArr[i] = 999;
        }
        driftSparks.geometry.attributes.position.needsUpdate = true;

        if (hasShield) {
          player.shieldMesh.rotation.y += delta * 2.0;
          player.shieldMesh.rotation.x += delta * 1.4;
        }

        const kmh = Math.floor(currentSpeed * 3.1);
        const gForce = (1.0 + Math.abs(bankAngle) * 2.5 + (isBoosting ? 1.8 : 0)).toFixed(1);
        hudScore.textContent = String(Math.floor(score)).padStart(6, '0');
        hudMultiplier.textContent = `x${comboMultiplier.toFixed(1)}`;
        hudSpeed.textContent = kmh;
        hudMach.textContent = `MACH ${(kmh / 1235).toFixed(2)} // ${gForce}G`;
        boostBar.style.width = `${boostEnergy}%`;

        if (isBoosting) {
          boostStatusText.textContent = 'AFTERBURNER ACTIVE';
          boostStatusText.style.color = '#ff6a00';
        } else if (boostEnergy >= 25) {
          boostStatusText.textContent = 'READY [SHIFT]';
          boostStatusText.style.color = '#00f0ff';
        } else {
          boostStatusText.textContent = 'RECHARGING...';
          boostStatusText.style.color = '#6a7c8c';
        }

        // PERFECT THIRD-PERSON CHASE CAMERA WITH G-FORCE CENTRIFUGAL ROLL
        const targetCamX = player.position.x * 0.75;
        camera.position.x += (targetCamX - camera.position.x) * (delta * 9);
        camera.position.y = player.position.y + 2.6;
        camera.position.z = player.position.z + 7.6;

        // Centrifugal camera roll tilt
        const rollAngle = -bankAngle * 0.32;
        camera.up.set(Math.sin(rollAngle), Math.cos(rollAngle), 0);
        camera.lookAt(player.position.x * 0.4, player.position.y + 0.4, player.position.z - 12);

        const targetFOV = isBoosting ? 84 : (65 + Math.min(distance * 0.006, 12));
        camera.fov += (targetFOV - camera.fov) * (delta * 6);
        camera.updateProjectionMatrix();

      } else {
        const t = elapsedTime * 0.4;
        camera.up.set(0, 1, 0);
        camera.position.x = Math.sin(t) * 4.5;
        camera.position.y = 3.8 + Math.cos(t * 0.6) * 0.4;
        camera.position.z = 8.5;
        camera.lookAt(0, 1.0, -18);
      }

      if (cameraShake > 0) {
        camera.position.x += (Math.random() - 0.5) * cameraShake;
        camera.position.y += (Math.random() - 0.5) * cameraShake;
        cameraShake = Math.max(0, cameraShake - delta * 3.8);
      }

      if (useBloom) {
        composer.render();
      } else {
        renderer.render(scene, camera);
      }
    }

    window.addEventListener('resize', () => {
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(window.innerWidth, window.innerHeight);
      composer.setSize(window.innerWidth, window.innerHeight);
      bloomPass.setSize(window.innerWidth, window.innerHeight);
      wipeoutPass.uniforms.uResolution.value.set(window.innerWidth, window.innerHeight);
    });

    animate();
  </script>
</body>
</html>
"""

with open('/home/hatch/workspace/3d-games/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated polished WipEout Edition index.html with {len(html_content)} characters.")
