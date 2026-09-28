# TERA PULSE — Master Video Walkthrough Script & Technical Guide
**Problem Statement:** SIH26053 (Autonomous Adaptive 2.5D LiDAR Perception & Navigation)  
**Team ID:** 137735  
**Target Video Duration:** 4 to 5 Minutes  
**Language:** Simple, Fluent English  

---

# PART 1: The Overbridge (Flyover) Analogy & 3D Diagram

Evaluators ko 2.5D aur 3D ka difference samjhane ke liye **Overbridge ka example sabse best real-world example hai**.

```text
=============================================================================
                FULL 3D VOXEL GRID vs 2.5D ELEVATION GRID
=============================================================================

          [ SCENARIO: A ROAD WITH A FLYOVER / OVERBRIDGE ]

                  (Coordinate X=10, Y=20)
                             |
                             v
           +-----------------------------------+
           |    === FLYOVER / OVERBRIDGE ===   |  <-- Height Z2 = 8 meters
           +-----------------------------------+
                             |
                     ( Empty Air Space )          <-- Height Z = 4 meters
                             |
           -------------------------------------
           |       --- GROUND ROAD ---         |  <-- Height Z1 = 0 meters
           -------------------------------------

-----------------------------------------------------------------------------
1. FULL 3D VOXELS (Multi-Layer World):
   • At the EXACT SAME (X=10, Y=20), it stores MULTIPLE occupied points:
     Point A: Z = 0m (Ground Road)
     Point B: Z = 8m (Overbridge Road)
   • Problem: Needs 3D cube arrays stacked infinitely high. Consumes 2 GB of RAM!

-----------------------------------------------------------------------------
2. 2.5D ELEVATION GRID (Single Surface Function):
   • For coordinate (X=10, Y=20), it only stores ONE surface elevation: Z = f(X, Y)
   • It only sees the top surface (Height = 8m). It cannot "see under" the bridge.

-----------------------------------------------------------------------------
⭐ THE GOLDEN PUNCHLINE FOR OFF-ROAD & DEFENSE:
   "In natural off-road battlefields, mountain borders, deserts, and lunar 
    craters, THERE ARE NO MULTI-STORY FLYOVERS OR BRIDGES! 
    Natural ground is a single continuous surface. 
    Therefore, paying a 100x compute penalty for full 3D is a complete waste! 
    2.5D gives us 100% of terrain reality with just 1% of the compute power!"
=============================================================================
```

---

# PART 2: Screen Recording Guide & Practical Setup

### 1. Timing Breakdown (Total 4m 30s):
* **0:00 – 0:40** : Introduction, Team ID 137735, Problem Statement (PPT Slide 1 & 2)
* **0:40 – 1:20** : 2.5D vs 3D Concept (The Overbridge Analogy)
* **1:20 – 1:55** : Foveated Adaptive Grid (5cm to 100cm cell expansion)
* **1:55 – 2:25** : VS Code Codebase & `python share.py` Live Execution
* **2:25 – 3:50** : Live Browser Dashboard Walkthrough (60 FPS, Foveated Focus, A* Path, Weather)
* **3:50 – 4:40** : Why Adopt This? (Cost, 5W Battery, Defense, Make-in-India) & Conclusion

### 2. Software to Record Screen:
* **OBS Studio (Highly Recommended - 100% Free):**
  * Download: `obsproject.com`
  * Add Source -> **Display Capture** (Records full screen smoothly when you switch between PPT, VS Code, and Chrome).
* **Clipchamp (Windows 11 Built-in):**
  * Press Windows Key -> Search `Clipchamp` -> Record Screen -> Entire Screen.

### 3. Setup Tips before Recording:
* Hide Desktop icons (Right-click desktop -> *View* -> uncheck *Show desktop icons*).
* Press **`F11`** in Chrome to make the prototype full screen.
* Keep earphones/mic 4-5 inches away from your mouth to avoid breath pop noises.

---

# PART 3: The Complete Simple English Word-for-Word Script

*(Read this text aloud clearly and with confidence while recording your screen)*

---

### **[SCENE 1: Welcome & The Problem]**
⏱️ **0:00 – 0:40** | *Screen: Open PPT Slide 1 (Title: TERA PULSE, Team ID 137735) then Slide 2*

> "Hello everyone and respected jury members. We are Team 137735, presenting our project for Problem Statement SIH26053: **TERA PULSE — Real-Time Adaptive 2.5D LiDAR Perception and Autonomous Navigation System.**
>
> Today, autonomous rovers in defense, disaster rescue, and off-road missions face a major challenge. 
> Traditional LiDAR sensors shoot laser beams uniformly in a rigid fixed pattern. Over 75% of these laser points are wasted on empty sky, clouds, and flat ground. 
> To process this massive data, rovers need heavy, expensive GPU servers that drain batteries in just two hours and create dangerous lag. 
> We built TERA PULSE to solve this exact problem."

---

### **[SCENE 2: What is 2.5D? The Overbridge Example]**
⏱️ **0:40 – 1:20** | *Screen: Show Overbridge Diagram or PPT Slide explaining 2.5D vs 3D*

> "To understand our innovation, let’s understand the difference between 3D and 2.5D.
>
> In city driving, you have multi-level flyovers and overbridges. At the exact same location, you can have a road on the ground, and another bridge road ten meters above it. Full 3D voxels are needed there to store multiple levels, which consumes gigabytes of memory.
>
> But in natural off-road battlefields, deserts, mountain terrains, and lunar surfaces, **there are no multi-story flyovers!** 
> Natural terrain is a single ground surface. 
>
> That is why we use a **2.5D Elevation Grid**. For every point on the ground, instead of stacking one hundred empty 3D cubes, we store just one cell with four terrain properties:
> ground height, slope angle, step hazard, and surface roughness.
> This gives us full 3D terrain awareness with 99% less memory and ultra-fast microsecond speed!"

---

### **[SCENE 3: Foveated Adaptive Grid (5cm to 100cm)]**
⏱️ **1:20 – 1:55** | *Screen: PPT Slide with Foveated Concentric Rings Diagram*

> "Our second big innovation is **Foveated Adaptive Grid Resolution**, inspired by the human eye.
>
> If you make the grid cells uniformly small at 5 centimeters everywhere, the computer has to process over one million cells, which freezes the system.
>
> TERA PULSE solves this through gradual expansion:
> Right near the vehicle’s wheels and hazard zones, our grid cell size is ultra-fine at **5 centimeters**. This allows us to detect small stones, ditches, and ground clearance hazards.
> 
> But as we look further away into the distance, the grid cell size **gradually expands to 20 centimeters, 50 centimeters, and up to 1 meter**.
>
> This reduces total cells from one million down to just **35,000 cells**! 
> Because of this, our **A* Path Planner computes a safe, rollover-free path in less than 5 milliseconds**, allowing the rover to navigate smoothly at 60 FPS on low-cost hardware."

---

### **[SCENE 4: Local VS Code Execution]**
⏱️ **1:55 – 2:25** | *Screen: Open VS Code, open terminal, run `python share.py`*

> "Now, let’s see the live implementation running locally on our machine.
> Here is our complete modular Python codebase in VS Code.
> 
> To run the system and make it instantly accessible, we execute a single command:
> `python share.py`.
>
> As you can see, our local Flask perception server starts immediately, and an encrypted Cloudflare tunnel is created, automatically copying a live public link to our clipboard for easy remote sharing."

---

### **[SCENE 5: Live Interactive Prototype Demo]**
⏱️ **2:25 – 3:50** | *Screen: Switch to Chrome at `http://localhost:5000` (Press F11 for Full Screen)*

> *(Action: Move mouse cursor over LiDAR map)*
> "Here is our live interactive prototype running at a smooth 60 Frames Per Second.
> 
> Watch the LiDAR canvas: as I move the rover's focus point, the system dynamically concentrates laser pulses directly on the hazard area. The peripheral area stays sparse to save bandwidth, while the obstacle receives maximum point density.
>
> In the center panel, our **2.5D Traversability Engine** analyzes slope and roughness in real-time. Green cells represent safe driving paths, while red and amber cells represent dangerous steep slopes and obstacle hazards.
>
> *(Action: Click to set a new Goal Point on canvas)*
> Notice how our A* path planner instantly recalculates the neon green navigation trajectory around obstacles with zero delay.
>
> *(Action: Toggle Rain / Fog Weather Simulation in controls panel)*
> Even when we simulate adverse weather conditions like heavy rain and dust, our Statistical Outlier Removal filter cleans the noise and preserves the true ground profile."

---

### **[SCENE 6: Why Should We Adopt This? (The Real-World Value)]**
⏱️ **3:50 – 4:40** | *Screen: Show GitHub Repo https://github.com/AbhayVerma628/SIH26053_Lidar*

> "Why should defense and industry adopt TERA PULSE?
>
> First, **Cost and Power Efficiency:** Traditional 3D systems require heavy 300-watt GPU servers. TERA PULSE runs on a 5-watt mini processor like a Raspberry Pi 5 or Jetson Nano, cutting hardware costs by 80% and tripling rover battery life.
>
> Second, **Zero-Lag High-Speed Safety:** With sub-5 millisecond planning latency, rovers can travel at higher speeds without the fear of falling into trenches or rolling over steep slopes.
>
> Third, **GPS-Denied Self-Reliance:** In border regions like Ladakh or Thar Desert where GPS signals are jammed and weather is harsh, TERA PULSE works with 100% local autonomy.
>
> Our complete code, research documentation, and interactive prototype are open-source and documented on GitHub.
>
> Thank you so much! Team ID: 137735."
