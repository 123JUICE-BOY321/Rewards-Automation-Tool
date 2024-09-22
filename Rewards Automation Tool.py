import pyautogui,random,os
alphabets="abcdefghijklmnopqrstuvwxyz"
x=850  #X position of search box.
y=185  #Y position of search box.
n=10  #Adjust according to number of searches (points/3).
sleep=8  #Adjust according to speed of internet and device.
os.system('start msedge --profile-directory="Profile 1" https://www.bing.com/search?q=bing')
pyautogui.sleep(sleep)
for i in range(n):
    pyautogui.moveTo(x, y)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    word=random.choice(alphabets)+random.choice(alphabets)+random.choice(alphabets)
    pyautogui.typewrite(word)
    pyautogui.press('enter')
    pyautogui.sleep(sleep)
os.system('start msedge --profile-directory="Profile 1" https://rewards.bing.com/')
print("Daily PC search completed.")
