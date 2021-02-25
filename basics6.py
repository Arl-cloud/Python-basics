def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results =  []

while True: #while loops work on a conditional basis
    user_input = input("Say something: ")
    if user_input == "\end": 
        break
    else:
        results.append(sentence_maker(user_input)) #call function with input as "user_input"
        #stores output of sentence maker in results list
print(" ".join(results)) #space in string to leave a space as joined