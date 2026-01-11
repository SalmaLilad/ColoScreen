
# 🗂️ File Naming Architecture & Taxonomy

## 1. Overview & Mandate
To ensure programmatic parsability across the **25,920+** images in the ColoScreen dataset, a strict "Zero-Ambiguity" naming convention is enforced.

Every filename acts as a self-contained metadata packet. A Python script must be able to derive **Sensor**, **Lighting**, **Geometry**, and **Exposure** solely from the string, without opening the file.

> **⚠️ Rule:** All filenames are **Case Sensitive**. Separators are always underscores `_`.

---

## 2. Universal Schema (Backgrounds)
This schema applies to all "Digital Twin" substrate captures (Phase 1). Data such as **Timestamp**, **ISO**, and **Aperture** are omitted from the filename as they are preserved in the file's **EXIF metadata**.

### 2.1 The Formula
```text
[SessionID]_[SensorID]_[SubstrateCode]_[Lighting]_[Geometry]_[GridLoc]_[Bracket]_[Counter].dng
```
---
### 2.2 Visual Decoder

| Segment | Example Value | Description |
| :--- | :--- | :--- |
| **1. Session** | `S01` | Incremental session number (e.g., Session 1). |
| **2. Date** | `20260109` | Capture date from EXIF metadata (YYYYMMDD). |
| **3. Time** | `091522` | Capture time from EXIF metadata (HHMMSS). |
| **4. SensorID** | `IP16` | Uniquely identifies the capture hardware (e.g., iPhone 16e). |
| **5. SubstrateCode**| `CHRM_SFT_2` | **Brand_Type_Ply** (Derived from Master Sheet). |
| **6. Lighting** | `Day` | The dominant color temperature (5600K). |
| **7. Geometry** | `Geo3` | The physical fold/crumple topology. |
| **8. GridLoc** | `R2C2` | Row 2, Column 3 on the capture board. |
| **9. Bracket** | `0EV` | The exposure value relative to meter. |
| **10. Counter** | `0042` | Unique sequence identifier. |

**Full Example:**
`S01_20260109_091522_IP16_CHRM_SFT_2_Day_Geo3_R2C2_0EV_0042.dng`

---
## 3. Component Breakdown (Taxonomy)

### 📸 3.1 Sensor ID Dictionary
These codes identify the specific device used for capture.

| Sensor ID | Device Model | Sensor Category | Description / Rationale |
| :--- | :--- | :--- | :--- |
| **D750** | **Nikon D750** | **Reference** | **Ground Truth.** Full-frame DSLR, high dynamic range. |
| **SS10** | **Samsung S10** | Legacy Flagship | Variable mechanical aperture tests (f/1.5 vs f/2.4). |
| **SS24** | **Samsung S24** | Modern High-Res | 200MP binning and distinct "warm" color science. |
| **SA03** | **Samsung A03** | Budget Tier | Low-end sensor with high noise floor. |
| **IP16** | **iPhone 16e** | Modern Standard | Smart HDR and local tone mapping typical of iOS devices. |
| **GPX6** | **Pixel 6** | Compute AI (Old) | Baseline for heavy Google computational photography. |
| **GP10** | **Pixel 10 Pro** | Compute AI (New) | Next-gen sensor with advanced AI-driven image pipelines. |
| **MOTS** | **Moto G Stylus** | Mid-Range | Limited dynamic range; simulates "blown highlights". |


### 🧻 3.2 Substrate ID Dictionary (Master List)
Codes are structured as `[Brand]_[Type]_[Ply]`.

| Tier | Substrate Code | Brand / Product | Ply | Key Feature |
| :--- | :--- | :--- | :--- | :--- |
| **1** | **CHRM_ESS_1** | Charmin Essentials Strong | 1 | Budget 1-Ply Baseline |
| **1** | **COTN_CLN_1** | Cottonelle Ultra Clean | 1 | Thin Embossed Texture |
| **1** | **SCOT_STR_1** | Scott 1000 Long Lasting | 1 | Minimum Thickness / Translucent |
| **1** | **CABO_BAM_2** | Caboose Bamboo | 2 | Bamboo Texture Variation |
| **1** | **CHRM_SFT_2** | Charmin Ultra Soft | 2 | Cloud/Fluffy Quilted |
| **1** | **CHRM_STR_2** | Charmin Ultra Strong | 2 | Deep Diamond Emboss Pockets |
| **1** | **COTN_CMF_2** | Cottonelle Ultra Comfort | 2 | Rippled Wave Geometry |
| **1** | **DOLR_SNS_2** | Dollar Store Soft & Strong | 2 | Low Quality Baseline |
| **1** | **EVSP_REC_2** | Ever Spring 100% Recycled | 2 | Natural Brown / Eco Texture |
| **1** | **T365_REC_2** | 365 Ultra Resistant Recycled | 2 | Tan Recycled / House Brand |
| **1** | **WGAC_SNS_2** | Who Gives a Crap S&S | 2 | Premium Eco / Tan-Natural |
| **1** | **QNOR_PLU_3** | Quilted Northern Ultra Plush | 3 | Maximum Thickness / Quilted |
| **1** | **REEL_BAM_3** | Reel Paper Premium Bamboo | 3 | Natural White Fiber |
| **1** | **QNYA_UNB_4** | Qing Ya 4-Ply Unbleached | 4 | Extreme Thickness / Unbleached |
| **2** | **ARIA_REC_3** | ARIA 100% Recycled | 3 | Visible Fiber Fragments |
| **2** | **ALDI_STR_1** | Aldi Willow 1000 | 1 | Extreme Budget Thin |
| **2** | **SCOT_CMF_1** | Scott Comfort Plus | 1 | 1-Ply Comfort Variant |
| **2** | **UPUP_STR_1** | Up & Up 1000 | 1 | Target Economy |
| **2** | **AMZN_STR_2** | Amazon Presto Ultra Strong | 2 | E-Commerce Brand Strong |
| **2** | **CHRM_ESS_2** | Charmin Essentials Soft | 2 | Mid-Range Quilting |
| **2** | **CHRM_GNT_2** | Charmin Ultra Gentle | 2 | Lotion Finish / Surface Tension |
| **2** | **HDXX_SNS_2** | HDX Soft & Strong | 2 | Hardware Store Brand |
| **2** | **KIRK_SNS_2** | Kirkland Soft & Strong | 2 | Warehouse Club Quality |
| **2** | **MMBR_SNS_2** | Member's Mark Soft & Strong | 2 | Sam's Club Bulk |
| **2** | **QNOR_SNS_2** | Quilted Northern Soft & Strong | 2 | Dense Quilted Pattern |
| **2** | **T365_SUS_2** | 365 Sustainably Soft | 2 | Whole Foods House Brand |
| **2** | **TJOS_ULT_2** | Trader Joe's Bath Tissue | 2 | Grocery Economy Variant |
| **2** | **UPUP_STR_2** | Up & Up Premium Ultra Strong | 2 | Target Premium |
| **2** | **WLGN_SUP_2** | Walgreens Super Soft | 2 | Butterfly Emboss |
| **2** | **WMGV_SNS_2** | Great Value Soft & Strong | 2 | Walmart Best Seller |
| **3** | **CVSH_BAS_1** | CVS Just the Basics | 1 | Drugstore Budget |
| **3** | **WLGN_ULT_1** | Walgreens Big Roll | 1 | Extended Length Format |
| **3** | **ALDI_SNS_2** | Aldi Willow Ultra Soft & Strong | 2 | Mass Market Quality |
| **3** | **ALDI_STR_2** | Aldi Willow Ultra Strong | 2 | Discount Strong Emboss |
| **3** | **AMZN_SFT_2** | Amazon Presto Ultra Soft | 2 | Online-Only Quality |
| **3** | **ANGL_SNS_2** | Angel Soft Soft & Strong | 2 | Mid-Range Soft |
| **3** | **BLKW_ULT_2** | Black and White | 2 | Minimal Processing |
| **3** | **CVSH_SFT_2** | CVS Total Home Ultra Soft | 2 | Drugstore Soft |
| **3** | **CVSH_STR_2** | CVS Total Home Ultra Strong | 2 | Drugstore Emboss |
| **3** | **DEAL_ULT_2** | Deal Worthy | 2 | Low-End Texture |
| **3** | **MOXE_SFT_2** | Moxie Ultra Soft | 2 | Alternative Soft Texture |
| **3** | **SGEN_REC_2** | Seventh Generation Recycled | 2 | Tan Unbleached / Rough |
| **3** | **TJOS_SFT_2** | Trader Joe's Super Soft | 2 | Unique Texture |
| **3** | **WLGN_SFT_2** | Walgreens Soft | 2 | Drugstore Quality |
| **3** | **DOLR_BAS_1** | Dollar Store 1000 Sheets | 1 | Ultra-Budget / Low-End |


### 💡 3.3 Lighting ID

| Lighting ID | Condition | Color Temp (K) | Description |
| :--- | :--- | :--- | :--- |
| **Day** | Daylight | 5600K | Neutral white, standard commercial/restroom LED. |
| **Warm** | Tungsten | 3200K | Residential "soft white" bulbs (yellow cast). |
| **Mix** | Mixed | ~4500K | Combination of Window light + Interior bulb mix. |

### 📐 3.4 Geometry ID

| Geometry ID | Description | Visual Characteristics |
| :--- | :--- | :--- |
| **Geo1** | **Flat** | Reference state; perfectly smooth single sheet. |
| **Geo2** | **Double Folded** | Folded once (2 layers); clean edge. |
| **Geo3** | **Quad Folded** | Folded twice (4 layers); standard user preparation. |
| **Geo4** | **Irregular Fold** | Asymmetric/Haphazard folding; random crease lines. |
| **Geo5** | **Balled** | Tight sphere; compressed density. |
| **Geo6** | **Crumpled** | Loose texture stress; high peaks and deep shadows. |
| **Geo7** | **Torn** | Ripped edges; frayed fibers and irregular boundaries. |
| **Geo8** | **Wet** | Pre-saturated substrate; translucency and fiber collapse artifacts. |

### 📍 3.5 Grid Location ID

| GridLoc ID | Description | Usage |
| :--- | :--- | :--- |
| **R[1-4]C[1-4]** | Row X, Col Y | E.g., `R2C3`. Used for spatial mapping. |
| **Center** | Center Placement | Used for single-subject focus stacking. |

### ☀️ 3.6 Bracket ID (Exposure)

| Bracket ID | Value | Purpose |
| :--- | :--- | :--- |
| **-1EV** | Underexposed | Preserves highlight detail (e.g., wet glare). |
| **0EV** | Mettered | Standard exposure (18% Gray = RGB 119). |
| **+1EV** | Overexposed | Preserves shadow detail (e.g., deep clots). |

## 4. Foreground Naming Schema (Pathology)
The pathology assets (blood/stool) use a slightly different schema because they are captured in **Duplicate Sets** for quality assurance.

### 4.1 The Formula
```text
FG_[Class]_[Variant]_[Temp]_[GridLoc]_[Bracket]_[SetID]_[Counter].nef
```


### 4.2 Visual Decoder

| Segment | Example | Notes |
| :--- | :--- | :--- |
| **Prefix** | `FG` | Hardcoded "Foreground" designator. |
| **Class** | `Arterial` | The biological mimic type (see below). |
| **Variant** | `Bright01` | Specific batch/viscosity mix. |
| **Temp** | `24C` | Surface temp at capture (critical for viscosity). |
| **GridLoc** | `R2C3` | Position on the white PVC board. |
| **Bracket** | `0EV` | Exposure step. |
| **SetID** | `SetA` | Used for Laplacian sharpness comparison vs `SetB`. |

### 🩸 4.3 Pathology Classes

| Class ID | Mimic Type | Visual Characteristic |
| :--- | :--- | :--- |
| **Arterial** | Lower GI Bleed | Bright Red, Oxygenated, Thin viscosity. |
| **Venous** | Upper/Mid GI Bleed | Dark Red, Deoxygenated, Thicker viscosity. |
| **Clot** | Thrombosis | Solid/Gelatinous chunks, High contrast. |
| **StoolT3** | Healthy Stool | Bristol Scale Type 3 (Normal/Brown). |
| **Melena** | Upper GI Hemorrhage | Black/Tarry, sticky texture. |


### 5 & 6. Validation and Final Output
This includes the regex pattern and the final synthetic file naming structure.

```markdown
---

## 5. Automated Validation (Regex)
Use this Regular Expression pattern to validate filenames in your Python pipelines. This ensures that every image contains the required EXIF-derived timestamps and session data.

**Python Regex Pattern:**
```python
import re

# Universal Substrate Validator
# Matches: S01_20260109_091522_IP16_CHRM_SFT_2_Day_Geo3_R2C2_0EV_0042.dng
bg_pattern = re.compile(
    r"^S\d{2}_"                                    # 1. Session (e.g., S01)                     
    r"(D750|SS10|SS24|SA03|IP16|GPX6|GP10|MOTS)_"  # 4. Sensor ID
    r"([A-Z0-9]{4}_[A-Z]{3}_\d)_"                  # 5. Substrate Code (e.g. CHRM_SFT_2)
    r"(Day|Warm|Mix)_"                             # 6. Lighting
    r"(Geo[1-8])_"                                 # 7. Geometry (Geo1=Flat, Geo8=Wet)
    r"(R[1-4]C[1-4]|Center)_"                      # 8. GridLoc
    r"(-1EV|0EV|\+1EV)_"                           # 9. Bracket
    r"(\d{4})\.(dng|nef|cr3)$"                     # 10. Broader extensions + Counter no _

# Example Usage:
# if bg_pattern.match(filename):
#     print("Filename is valid.")

)
```


## 6. Synthetic Composition Schema (Final Output)
When the "Digital Twin" substrate (TP) is programmatically combined with a pathology mimic (Blood/Stool), the resulting image filename follows a strict **6-tier hierarchy**.

### 6.1 The Formula
```text
SYN_[SensorID]_[SubstrateCode]_[Lighting]_[Bracket]_[BloodClass]_[StoolClass]_[Geometry]_[UUID].jpg
```

### 6.2 Hierarchy Decoder (Priority Order)

| Priority | Component | Example | Notes |
| :--- | :--- | :--- | :--- |
| **1** | **Sensor** | `IP16` | The camera hardware personality. |
| **2** | **Toilet Paper** | `CHRM_SFT_2` | The background substrate brand/ply. |
| **3** | **Lighting** | `Day` | The environmental color temperature. |
| **4** | **Bracket** | `0EV` | The exposure level used (or `HDR` if fused). |
| **5** | **Blood Type** | `Arterial` | **Primary Pathology.** (`NA` if no blood). |
| **6** | **Stool Type** | `StoolT3` | **Secondary Pathology.** (`NA` if no stool). |
| **7** | **Geometry** | `Geo3` | The fold/crumple topology. |
| **8** | **UUID** | `8f9a2b` | Unique hash for collision avoidance. |


### 6.3 Visual Examples

**Scenario A: Blood Only (Standard)**
> *Sensor: iPhone 16e | TP: Charmin Soft | Light: Day | Exp: 0EV | Blood: Arterial | Stool: None*
>
> `SYN_IP16_CHRM_SFT_2_Day_0EV_Arterial_NA_Geo3_8f9a2b.jpg`

**Scenario B: Stool Only**
> *Sensor: Samsung S24 | TP: Scott 1000 | Light: Warm | Exp: +1EV | Blood: None | Stool: Type 3*
>
> `SYN_SS24_SCOT_STR_1_Warm_+1EV_NA_StoolT3_Geo1_7c2d1a.jpg`

**Scenario C: Complex Case (Blood + Stool)**
> *Sensor: Pixel 10 Pro | TP: Kirkland | Light: Mix | Exp: HDR | Blood: Melena | Stool: Type 6*
>
> `SYN_GP10_KIRK_SNS_2_Mix_HDR_Melena_StoolT6_Geo6_3b4e5f.jpg`
>
 ---
 ##  AI Assistance Disclosure

This README was prepared with the assistance of an AI agent to enhance structure, clarity, and technical documentation quality. All project code, architecture, and experimental results were implemented, and verified by me without any AI use. I provided the outline, structure and content for this ReadME and the AI assistant was used exclusively for documentation, drafting, formatting, and summarization purposes.
