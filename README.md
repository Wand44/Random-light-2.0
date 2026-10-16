
# Relit 2.0

A Blender addon to quickly generate randomized lighting setups around a selected object. Ideal for fast blocking of rim lights or creating chaotic, colorful environments without manual placement.

## 🚀 Features
- **Randomized Placement:** Generates lights within a configurable spread around the active object.
- **Light Types:** Supports both **Point** and **Area** lights.
- **Smart Targeting:** Area lights automatically include a `Track To` constraint, ensuring they always face the target object.
- **Full Control:**
    - **Count:** Set exactly how many lights to spawn.
    - **Energy & Size:** Global control over light intensity and radius/size.
    - **Spread & Height:** Adjust how far the lights scatter and their vertical offset.
    - **Color Randomization:** Toggle between pure white lights or completely random colors.
- **One-Click Cleanup:** Dedicated "Delete" button to wipe all generated lights instantly.

## 🛠️ How to Use
1. **Select** your target object in the 3D View.
2. Open the **N-Panel** $\rightarrow$ **Random Light** tab.
3. Adjust your settings in the **Config** sub-panel.
4. Click **Generate**.
5. Click **Delete** to clear the scene and start over.

## 📦 Installation
1. Download the `.py` file.
2. In Blender: `Edit` $\rightarrow$ `Preferences` $\rightarrow$ `Add-ons` $\rightarrow$ `Install...`
3. Select the file and enable the checkbox.

## 💻 Technical Details
- **Language:** Python
- **API:** `bpy` (Blender Python API)
- **Version:** 2.0.0
- **Blender Compatibility:** 5.1.0+
