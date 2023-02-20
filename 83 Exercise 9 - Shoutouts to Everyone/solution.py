import win32com.client

def pronounce_names(names):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for name in names:
        speaker.Speak("Shoutout to " + name)

# Test the function with the given list of names
l = ["Varaliya", "Mohd", "Taha", "Pranjal"]
pronounce_names(l)
