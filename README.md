# 🪙Rewards-Automation-Tool

A simple Python script that automates Bing searches using Microsoft Edge. This can help accumulate Microsoft Rewards points through PC search activity.

## ⚠️ Disclaimer

> This script automates user interactions and may violate Microsoft Rewards' [Terms of Service](https://www.microsoft.com/en-us/rewards/terms). Use at your own risk. This is intended for educational purposes only.

---

## 🔧 Requirements

- Windows OS (uses `os.system('start ...')` to launch Edge)
- Microsoft Edge browser
- Python 3.x
- `pyautogui` module

Install dependencies with:

```bash
pip install pyautogui
```

---

## 🚀 How It Works

1. Opens Microsoft Edge with Bing search.
2. Randomly types and searches short character strings.
3. Repeats this process multiple times to simulate user activity.
4. Opens the Bing Rewards page when done.

---

## 📄 Script Configuration

```python
x = 850       # X-coordinate of the Bing search box
y = 185       # Y-coordinate of the Bing search box
n = 10        # Number of searches (1 search = ~3 points)
sleep = 8     # Delay in seconds between actions (adjust for internet speed)
```

- **Coordinates (`x`, `y`)** may need adjusting based on your screen resolution and browser layout.
- `n` determines how many searches are performed.
- `sleep` helps avoid premature typing before the page loads.

---

## 💡 Example Use

```bash
python rewards_automation_tool.py
```

The script will:
- Open Edge to Bing
- Perform `n` searches using random 3-letter strings
- Open your Microsoft Rewards page at the end

---

## 🧠 Notes

- You must be logged into your Microsoft account in Edge's **Default profile**.
- Ensure Edge is not already open when running the script.
- Use at moderate frequency to avoid detection or bans.

---

## 📬 Output

```text
Daily PC search completed.
```

