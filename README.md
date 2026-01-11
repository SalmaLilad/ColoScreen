# ColoScreen: AI-Powered Triage & Morphological Analysis for GI Health

**ColoScreen** is a medical AI research project designed to detect and classify blood on toilet paper using computer vision. By leveraging a hybrid pipeline of physical data acquisition, digital compositing, and generative synthetic data, the model accounts for variances in substrate texture, lighting, and blood morphology to provide accurate triage considerations.

---

##  Phase 1: Data Acquisition (Dual Stream)

Data collection is divided into two distinct workflows: capturing isolated "ingredients" for compositing, and capturing "reference" scenes for model calibration.

Dual workflow captures of substrates, blood/stool mimics, and reference scenes.

→ **[Toilet Paper Substrate Selection & Stratification (45 brands)](./Data%20Acquisition/TP_Selection.md)** – Why these specific substrates were chosen




### Workflow A: Component Capture (The Ingredients)
These high-fidelity isolated elements serve as the raw materials for the compositing pipeline.
* **Substrates (Backgrounds):**
     **45 Toilet Paper Types:** Captured against an **18% Neutral Gray Board** to ensure accurate color balance and easy segmentation. Toilet Paper are segmented into three Tiers
    
    *  **Tier 1:** Core, all-encompassing baseline (20 TPs covers major brands, ply, type and texture).
    *	**Tier 2:** Expanded material/texture/color coverage beyond Tier 1.
    * **Tier 3:** Edge cases, poor quality toilet papers.
 
 * **Biological Agents (Foregrounds):**
    * **Blood Variants (96 Profiles):** Captured against a **White PVC Mask** and processed via **Alpha Masking** to extract transparent overlays.
    * **Stool Variants (20 Types):** Classified by **Bristol Stool Scale (Types 1–5)** to simulate bio-noise.

### Workflow B: Reference Capture (The Ground Truth)
These images represent real-world "completed" scenes and serve as the style reference for the Generative AI (LoRA) training.
* **Subject:** Toilet Paper + Blood + Stool (Physical interaction).
* **Environment:** Captured against **18% Gray MDF** under 3 lighting conditions (Studio LED, Warm Tungsten, Mixed).
* **Volume:** **1,600 RAW Images**.
* **Processing:**
    1.  **Auto-Bracketing:** 3 exposures per scene.
    2.  **Laplacian Variance:** Automated sharpness selection to discard blurry frames.
    3.  **Mertens Fusion:** Merged into high-fidelity HDR texture maps.

---

##  Phase 2: Synthesis & Scaling (500k Dataset)

We utilize a **Hybrid Infrastructure** to scale the dataset. The first **10,000 images** are generated locally for validation; the remaining **490,000** are computed via the proposed AWS Cloud pipeline.

### 1. Compositing & Generation (300k Images)
We utilize a **Stratified Random Sampling** strategy to combine ingredients into **300,000 unique scenes**.
* **Core Model:** **Juggernaut XL** (Stable Diffusion XL).
* **Style Transfer:** A **LoRA** (Low-Rank Adaptation) trained on the 1,600 reference images enforces realistic fiber absorption and wicking.
* **Guidance:** **ControlNet** uses the alpha masks to guide precise blood placement and morphology.

### 2. Augmentation Pipeline (200k Images)
To harden the model against hardware limitations and edge cases, we generate an additional **200,000 images** using `Albumentations`.
* **Set A: Sensor Simulation (100k):** Mimics low-quality phone sensors (Gaussian Blur, Gamma Correction, Color Jitter).
* **Set B: Edge Cases (100k):** Hardens against poor lighting (CLAHE for faint stains, Hue/Saturation shifts).

---

##  Proposed AWS Architecture (Mass Scaling)

To scale from the local pilot to the full 500k dataset, the following cloud architecture is proposed. It utilizes **AWS Batch** for cost-effective orchestration of GPU resources.

### Architectural Components
1.  **Storage (Amazon S3):**
    * **Input Bucket:** Stores the "Ingredients" (45 TP backgrounds, 96 Blood Alpha masks).
    * **Output Bucket:** Stores the generated 500k synthetic dataset and metadata logs.
2.  **Container Registry (Amazon ECR):**
    * Hosts the custom Docker container with the verified environment (PyTorch, Diffusers, ControlNet weights, Custom LoRA).
3.  **Orchestration (AWS Batch):**
    * **Job Queue:** Manages the 50 distinct "jobs" (each generating 10k images) to prevent timeouts.
    * **Compute Environment:** Provisioned with **g5.xlarge** instances (NVIDIA A10G GPUs). Configured to use **Spot Instances** to reduce compute costs by ~70%.

---

##  Data Dictionary & Stratification

### Stratification Matrix (N=300,000 Base Images)
The dataset is weighted by market prevalence (Tier 1) while ensuring statistical significance for edge cases (Tier 3).

| Substrate Tier | Allocation % | Image Count | Description |
| :--- | :--- | :--- | :--- |
| **Tier 1** | 60% | **180,000** | Core, all-encompassing baseline (20 TPs covers major brands, ply, type and texture) |
| **Tier 2** | 30% | **90,000** | Expanded material/texture/color coverage beyond Tier 1 |
| **Tier 3** | 10% | **30,000** | Edge cases, poor quality toilet papers. |

### Component Dictionary
* **Blood Variants (96 Types):** Matrix of [6 Colors] × [4 Viscosities] × [4 Morphologies].
* **Stool Variants (20 Types):** Bristol Scale Types 1–5 (4 visual variations each).

---

##  Phase 3: Classifier & Triage

The final stage involves interpreting the CNN's feature maps to provide actionable medical intelligence.

* **Model:** Convolutional Neural Network (CNN) backbone.
* **Head:** **Bayesian Classification Layer**.
* **Output:** Probability distribution for triage categories.
* **Safety:** The Bayesian layer quantifies **Epistemic Uncertainty**. If the model is "unsure" (e.g., due to extreme lighting conditions), it flags the image for human review rather than forcing a prediction.

---

##  Tech Stack

| Domain | Tools & Technologies |
| :--- | :--- |
| **Hardware** | X-Rite ColorChecker, Sekonic L858-D-U Light meter,  Nubee  NUB8380 Infrared Thermometer, Neewer 150W Continious light x2, C-Stand with weight bags, Multi-Sensor Arrays, NVIDIA RTX 5050 and RTX 5080 GPUs |
| **Cloud** | **AWS Batch**, **S3**, **EC2 (g5.xlarge)**, ECR |
| **GenAI** | **Juggernaut XL**, **ControlNet**, **LoRA** (Low-Rank Adaptation) |
| **CV / Image** | **OpenCV** (Laplacian, Mertens), **Albumentations** |
| **Core Logic** | Python, PyTorch, Bayesian Inference |

---

##  Author

**Saanvi ([@SalmaLilad](https://github.com/SalmaLilad))**  
Applied AI & Computing Portfolio — Generative AI & Machine Learning Project  
Developed to explore **AI’s role in real-world diagnostic modeling**, with a focus on accuracy, ethics, and reproducibility.  

---

##  AI Assistance Disclosure

This README was prepared with the assistance of an AI agent to enhance structure, clarity, and technical documentation quality. All project code, architecture, and experimental results were implemented, and verified by me without any AI use. I provided the outline, structure and content for this ReadME and the AI assistant was used exclusively for documentation, drafting, formatting, and summarization purposes.

---

## ⚠️ License & Disclaimer

This repository is for **educational and research use only**.  
It is **not intended for clinical or diagnostic purposes**, and results should not be interpreted as medical advice.  
Researchers and students are encouraged to **fork, extend, or analyze** this work for non-commercial academic use.

---
