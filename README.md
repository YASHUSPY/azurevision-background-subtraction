# AzureVision: Background Subtraction 🎥🧠

This project demonstrates **background subtraction** using OpenCV to isolate a person from a static background, simulating effects commonly used in virtual conferencing and AI vision systems.

## 🔧 How It Works
- First, capture the background without any person using `save_background.py`.
- Then, run `background_subtraction.py` and stand in the frame.
- The code subtracts background and shows you only!

## 📂 Files
- `save_background.py` – Saves background frame.
- `background_subtraction.py` – Runs live background subtraction.
- `background.jpg` – Captured background image.

## 🧠 Built With
- Python
- OpenCV
- NumPy

## ✅ How to Run
1. Run: `python save_background.py`
2. After 5 seconds, stand away. Background is saved.
3. Run: `python background_subtraction.py`
4. Stand in frame and watch background get removed!

## 📸 Sample Output
*(Insert sample image here after uploading)*

## 🏷️ Tags
`Computer Vision` `OpenCV` `Azure AI` `Background Removal`

## 🧾 License
MIT License
