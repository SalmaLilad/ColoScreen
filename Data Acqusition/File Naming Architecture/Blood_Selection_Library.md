# 🩸 Blood Mimic Selection & Morphology Taxonomy

## 1. Methodology Overview
The **ColoScreen** Phase 2 dataset utilizes a combinatorial library of **96 distinct blood variations**. This diversity ensures the CNN (Convolutional Neural Network) is robust against the full clinical spectrum of gastrointestinal pathology—from fresh lower-GI hemorrhaging to digested upper-GI melena. 

## 2. Procured Mimic Inventory
We utilize industry-standard theatrical fluids selected for their specific chemical behavior, opacity, and "drying" profiles.

| Brand | Product | Function |
| :--- | :--- | :--- |
| **Reel Blood** | Original, Aged, Old Dried, Thick (Fresh/Aged) | Maintains high-gloss surface tension and varied ages. |
| **PPI Fleet St.** | Drying Blood (Fresh, Dark) | Simulates the transition from liquid to oxidized states. |
| **Mehron** | Stage Blood, Coagulated Gel, Blood Splatter | Provides high-viscosity "clot" geometry and micro-droplets. |

---

## 3. The 6-Stage Blood Chromatic Scale (B1–B6)
To bridge the gap between theatrical mimics and clinical reality, we utilize **Activated Charcoal** as a primary pigment and texture modifier to simulate blood degradation.

| ID | Profile | Clinical Equivalence | Additive |
| :--- | :--- | :--- | :--- |
| **B1** | Bright Arterial | Acute Lower-GI Bleed (Active) | None |
| **B2** | Deep Venous | Standard Internal Bleed | None |
| **B3** | Oxidized / Dark | Stagnant or Older Blood | Trace Charcoal |
| **B4** | Dull Maroon | Partially Digested Blood | Light Charcoal |
| **B5** | Dark Chocolate | Mid/High-GI Bleed / Transition | Medium Charcoal |
| **B6** | **Tarry Black** | **Melena (Upper-GI Bleed)** | Heavy Charcoal |



---

## 4. Application Methodology & Tools
Blood is applied to the Phase 1 substrates using three primary tools to replicate real-world transfer morphologies.

| Tool | Resulting Morphology | Clinical Significance |
| :--- | :--- | :--- |
| **Precision Dropper** | **Pooling & Saturation** | Simulates heavy localized bleeding or drop-in events. |
| **Sea Sponge** | **Streaking & Wiping** | Replicates the "wipe" motion; tests low-density smear detection. |
| **Stipple Sponge** | **Clotting & Texture** | Creates granular, 3D patterns typical of coagulated tissue. |



---

## 5. Known Confounders (Explicitly Modeled)
To ensure the model decouples "paper noise" from "blood signal," the following variables are strictly controlled:
* **Specular Highlights:** Glossy formulas (Reel/Mehron) create white "hot spots" that the CNN must not confuse with the substrate.
* **Substrate Albedo Interaction:** The shift in blood hue when applied to **unbleached/tan** paper vs. **bleached/white** paper.
* **Tarry Viscosity:** Activated charcoal increases the "grit" and thickness of B6, simulating the sticky, viscous nature of clinical melena.

---

## 6. Preparation & Capture Protocol
1. **Charcoal Titration:** Charcoal is measured by weight (mg) and folded into the blood base to ensure repeatable B4–B6 opacity.
2. **Standardization:** All variations are initially photographed against an 18% Neutral Gray card under D5600 (Daylight) lighting to establish a chromatic ground truth.
3. **Hygiene:** Tools are cleaned thoroughly between color stages (B1 to B6) to prevent cross-contamination of pigments.

---
## 7. Digital Isolation & Alpha Masking
To prepare the blood mimics for synthetic overlay, the physical captures undergo a multi-stage digital pipeline:

1. **Automated Splitting:** A Python script slices the 18-capture board into individual image assets.
2. **Background Extraction:** The White PVC background is subtracted using a thresholding algorithm.
3. **Alpha Mask Generation:** A per-pixel transparency map (Alpha Channel) is created for each blood sample. This ensures that when the blood is "laid over" a toilet paper image, the underlying paper texture remains visible through the semi-transparent "wicked" edges of the blood.

---

## 8. Blood Capture Naming Convention
Isolated assets are labeled using a 4-segment taxonomy to facilitate the GAN overlay process.

**Format:** `[ColorID]_[ToolID]_[Viscosity]_[Counter].ext`

| Segment | Options | Description |
| :--- | :--- | :--- |
| **ColorID** | `B1` - `B6` | Chromatic level (Arterial to Melena). |
| **ToolID** | `DRP`, `SEA`, `STP`, `SPL` | Dropper, Sea Sponge, Stipple, Splatter. |
| **Viscosity** | `LIQ`, `GEL`, `THK`, `DRY` | Liquid, Gel, Thick/Coagulated, Dried. |
| **Counter** | `001` - `999` | Unique capture sequence. |

**Example:** `B6_STP_THK_042.png`  
*(Melena-color, Stipple Sponge, Thick formula, sequence 42 with Alpha Channel)*

---

## 9. Ground Truth & Validation Strategy
The **Ground Truth Dataset** consists of the 96 primary physical captures. While the Stable Diffusion engine coupled with Albumentations generate over 500,000 synthetic variations for feature generalization, the classifier's terminal performance is audited against these 96 ground truth images.

* **Primary Training Role:** These images serve as the "Anchor Points" for the CNN, providing the model with the most high-fidelity, un-distorted examples of blood morphology.
* **Validation:** They are the critical benchmark for the Bayesian layer’s triage considerations, ensuring that the model's highest-confidence detections are rooted in physical reality.

---

##  AI Assistance Disclosure
  
This README was prepared with the assistance of an AI agent to enhance structure, clarity, and technical documentation quality. All project code, architecture, and experimental results were implemented and verified independently, with the AI used exclusively for documentation, drafting, formatting, and summarization.








