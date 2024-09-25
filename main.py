#for task 1
import mood_responses

mood = input("How are you feeling today? ")
print(mood_responses.mood_response(mood))

#for task 2
import text_utils as txt 

input_string = input("Enter a string: ")

reversed_string = txt.reverse_string(input_string)
capitalized_string = txt.capitalize_string(input_string)

print(f"Reversed string: {reversed_string}")
print(f"Capitalized string: {capitalized_string}")