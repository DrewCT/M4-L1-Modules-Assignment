def mood_response(mood):
    mood = mood.lower()  
    if mood == "happy":
        return "That's great to hear!! Keep smiling"
    elif mood == "sad":
        return "I'm sorry to hear that... Keep your head up, It'll get better"
    elif mood == "excited":
        return "W energy! Today will be a great day"
    elif mood == "angry":
        return "What happened? Try to stay calm and think clearly before you continue with your day"
    elif mood == "tired":
        return "Get some rest!"
    else:
        return "Hmm, not sure what you mean. But I hope you're doing alright!"