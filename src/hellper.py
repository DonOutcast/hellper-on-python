import pyautogui
import speech_recognition
import pyaudio
def record_voluem():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone(device_index= 1) as source:
        print('Слушаю...')
        audio = r.listen(source)
    query = r.recognize_google(audio, language= 'ru-RU')
    print(f'Вы сказали: {query.lower()}')

record_voluem()

# pyautogui.FAILSAFE = True
# pyautogui.PAUSE = 2
# search = pyautogui.prompt("Enter a name for search video")
# pyautogui.hotkey('winleft')
# pyautogui.typewrite("chrome\n", 0.3)
# pyautogui.typewrite("www.youtube.com\n", 0.3)
# pyautogui.hotkey('winleft', 'up')
# pyautogui.click(625, 145)
# pyautogui.typewrite(search, 0.3)
# pyautogui.click(1342, 142)
