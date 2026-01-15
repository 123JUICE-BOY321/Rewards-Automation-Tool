# 🪙Rewards-Automation-Tool
A simple Python script that automates Bing searches using Microsoft Edge to help accumulate Microsoft Rewards points through PC search activity.
<br/><br/>

> [!WARNING]
> This script automates user interactions and may violate Microsoft Rewards' [Terms of Service](https://www.microsoft.com/en-us/rewards/terms). Use at your own risk. This is intended for educational purposes only.
<br/>

## 📋 Prerequisites
- Windows OS
- Microsoft Edge browser
- Python 3.x
<br/><br/>

## 📦 Installation
- ### Clone the Repository
  ``` bash
  git clone https://github.com/123JUICE-BOY321/Rewards-Automation-Tool.git
  cd Rewards-Automation-Tool
  ```
- ### Install Requirements
  ``` bash
  pip install pyautogui
  ```
<br/><br/>

## ⚙️ Configuration
```python
x = 850       # X-coordinate of the Bing search box
y = 185       # Y-coordinate of the Bing search box
n = 10        # Number of searches (1 search = ~3 points)
sleep = 8     # Delay in seconds between actions (adjust for internet speed)
```
<br/><br/>

## ▶️ Usage
  ```bash
  python rewards_automation_tool.py
  ```
1. Opens Microsoft Edge with Bing search.
2. Perform `n` searches using random 3-letter strings.
3. Opens the Microsoft Rewards page when done.
<br/><br/>

## 📜 License
🛡️ [**GNU General Public License v3.0 (GPLv3)**](LICENSE)
