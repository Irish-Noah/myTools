import time
import keyboard
from pycaw.pycaw import AudioUtilities
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.utils import AudioSession
from pycaw.pycaw import IAudioEndpointVolume

def toggle_chrome_mute():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        if session.Process and "chrome.exe" in session.Process.name().lower():
            volume = session.SimpleAudioVolume
            current_state = volume.GetMute()
            volume.SetMute(not current_state, None)
            print(f"{'Muted' if not current_state else 'Unmuted'} Chrome")

print("Press Ctrl+Alt+M to toggle mute for Chrome. Press Ctrl+Alt+Q to quit.")

keyboard.add_hotkey(";", toggle_chrome_mute)
keyboard.wait("ctrl+c")
