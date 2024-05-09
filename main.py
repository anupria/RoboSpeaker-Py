import pyttsx3

def robo_speaker(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    #engine.setProperty('rate', 150)  # Speed of speech
    #engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Convert text to speech
    engine.say(text)

    # Wait for speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome to Robo Speaker!")

    while True:
        # Prompt user for input
        text = input("Enter the text you want the Robo Speaker to say (type 'exit' to quit): ")

        # Check if user wants to exit
        if text.lower() == 'exit':
            print("Exiting Robo Speaker.")
            break

        # Speak the provided text
        robo_speaker(text)

# import pyttsx3
# def robo_speaker(text):
#      engine = pyttsx3.init()
#
#      engine.say(text)
#      engine.runAndWait()
#
# if __name__ == "__main__":
#     print("Hello, Welcome to RoboSpeaker!")
#
#     while True:
#         text = (input("Enter the text you want RoboSpeaker to say (type 'exit' to quit: "))
#         if text.lower() == 'exit':
#              print("Exiting Robo Speaker")
#              break
#         robo_speaker(text)









