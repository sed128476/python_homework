# Write your code here.
print("--------------Task1-----------------------------------")
def hello():
    return f"Hello!" 
    
print(hello())

print("------------------------Task2--------------------")
def greet(name):
    return f"Hello, {name}!" 
  
print(greet("katty"))

print("-------------------------------Task3----------------------------------------")
def calc(a, b, operation="multiply"):
    try:
        operation = operation.lower()
        if operation == "add":
               return a + b
        elif operation == "subtract":
                return a - b
        elif operation == "multiply":
                return a * b
        elif operation == "divide":
                return a / b
        elif operation == "modulo":
                return a % b
        elif operation == "int_divide":
                return a // b
        elif operation == "power":
                return a ** b
        else:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't {operation} those values!"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Test cases
print(calc(10, 5))  # Uses default "multiply" operation
print(calc(10, 2, "divide"))
print(calc(10, 0, "divide"))  # Tests division by zero
print(calc("hello", 2, "multiply"))  # Tests type error
print(calc(2, 3, "power"))
print(calc(10, 3, "modulo"))
print(calc(10, 3, "int_divide"))
print(calc(5, 2, "add"))
print(calc(10, 4, "subtract"))
print(calc("u" , 4, "subtract"))  # Test invalid number

print("-------------------Task 4-------------------")

def data_type_conversion(value, target_type):
    try:
        target_type = target_type.lower()
        if target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        elif target_type == "int":
            return int(value)
        else:
            return "Invalid type. Use 'float', 'str', or 'int'"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {target_type}."



# Test cases
print("\nTest 1:")
print(data_type_conversion("123", "int"))
print("\nTest 2:")
print(data_type_conversion(123, "str"))
print("\nTest 3:")
print(data_type_conversion("123.45", "float"))
print("\nTest 4:")
print(data_type_conversion("hello", "int"))
print("\nTest 5:")
print(data_type_conversion("abc", "float"))

print("-------------------Task 5-------------------")

def grade(*args):
    try:
        if not args:  # Check if any arguments were provided
            return "No grades provided"
        
        # Calculate average
        average = int(sum(args) / len(args))
        
        # Determine letter grade
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
            
    except (TypeError, ValueError):
        return "Invalid data was provided."


# Test cases
print("\nGrade Tests:")
print(grade(85, 90, 95))          # Should be A
print(grade(80, 82, 85))          # Should be B
print(grade(75, 78, 71))          # Should be C
print(grade(60, 65, 68))          # Should be D
print(grade(50, 55, 58))          # Should be F
print(grade())                    # Test with no arguments
print(grade(85, "90", 95))        # Test with invalid input
print(grade(85, -90, 95))         # Test with negative numbers

print("-------------------Task 6-------------------")

def repeat(string, count):
    try:
        if count <= 0:
            raise ValueError("Count must be a positive number")
            
        result = ""
        for i in range(count):
            result += string
        return result
    except TypeError:
        return "Invalid input: Both string and count must be valid types"
    except ValueError as e:
        return str(e)

# Test cases
print("\nRepeat Tests:")
print(repeat("hello ", 3))      # Should print: hello hello hello 
print(repeat("*", 5))          # Should print: *****
print(repeat("abc ", 2))       # Should print: abc abc 
print(repeat("hi", 0))         # Should print: Count must be a positive number
print(repeat("test", -1))      # Should print: Count must be a positive number
print(repeat(123, 2))          # Should print error message
print(repeat("word", "2"))     # Should print error message

print("-------------------Task 7-------------------")

def student_scores(operation, **kwargs):
    try:
        if not operation or not kwargs:
            raise ValueError("No operation or scores provided")
            
        if operation.lower() == "best":
            # Find student with highest score
            highest_score = max(kwargs.values())
            # Find the name(s) of students with the highest score
            best_students = [name for name, score in kwargs.items() if score == highest_score]
            return best_students[0]  # Return first student with highest score
            
        elif operation.lower() == "mean":
            # Calculate average score
            return int(sum(kwargs.values()) / len(kwargs))
            
        else:
            return "Invalid operation. Use 'best' or 'mean'"
            
    except (TypeError, ValueError):
        return "Invalid scores provided"

# Test cases
print("\nStudent Scores Tests:")
print(student_scores("best", John=85, Alice=90, Bob=75))        # Should print: Alice
print(student_scores("mean", John=85, Alice=90, Bob=75))        # Should print: 83
print(student_scores("best"))                                   # Should print: No scores provided
print(student_scores("mean", John=85, Alice="90", Bob=75))     # Should print: Invalid scores provided
print(student_scores("invalid", John=85, Alice=90, Bob=75))    # Should print: Invalid operation
print(student_scores("best", John=90, Alice=90, Bob=75))       # Should print: John (first student with highest score)





print("-------------------Task 8-------------------")

def titleize(text):
    try:
        # List of words that shouldn't be capitalized (unless first or last)
        little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
        
        # Split the text into words
        words = text.lower().split()
        
        if not words:  # Handle empty string
            return ""
            
        # Process each word
        for i, word in enumerate(words):
            # Capitalize if it's first word, last word, or not a little word
            if (i == 0 or                     # First word
                i == len(words) - 1 or        # Last word
                word not in little_words):     # Not a little word
                words[i] = word.capitalize()
                
        # Join the words back together
        return " ".join(words)
        
    except AttributeError:
        return "Invalid input: Input must be a string"

# Test cases
print("\nTitleize Tests:")
print(titleize("the quick brown fox"))                    # The Quick Brown Fox
print(titleize("a tale of two cities"))                   # A Tale of Two Cities
print(titleize("the lord of the rings"))                  # The Lord of the Rings
print(titleize(""))                                       # Empty string
print(titleize("in"))                                     # In
print(titleize("the end"))                                # The End
print(titleize("a brief history of time"))                # A Brief History of Time
print(titleize("to kill a mockingbird"))                  # To Kill a Mockingbird
print(titleize(123))                                      # Invalid input message



print("-------------------Task 9-------------------")

def hangman(secret, guess):
    try:
      
        result = ""
        # Convert both strings to lowercase for case-insensitive comparison
        secret = secret.lower()
        guess = guess.lower()
        
        # Process each character in the secret word
        for char in secret:
            if char in guess:
                result += char  # Add the actual letter if it was guessed
            else:
                result += "_"  # Add underscore for unguessed letters
                
        return result
        
    except AttributeError:
        return "Invalid input: Both inputs must be strings"

# Test cases
print("\nHangman Tests:")
print(hangman("alphabet", "ab"))          # Secret length: 8, Guess length: 2
print(hangman("Hello", "el"))            # Secret length: 5, Guess length: 2
print(hangman("Python", "xyz"))          # Secret length: 6, Guess length: 3
print(hangman("Programming", "grm"))     # Secret length: 11, Guess length: 3
print(hangman("", "abc"))               # Secret length: 0, Guess length: 3
print(hangman("Test", ""))              # Secret length: 4, Guess length: 0
print(hangman("UPPER", "per"))          # Secret length: 5, Guess length: 3
print(hangman(123, "abc"))              # Error message

print("-------------------Task 10-------------------")
def pig_latin(text):
    try:
        # Convert to lowercase and split into words
        words = text.lower().split()
        result = []
        vowels = 'aeiou'
        
        for word in words:
            if not word:  # Skip empty strings
                continue
                
            # Rule 1: If the word starts with a vowel
            if word[0] in vowels:
                result.append(word + "ay")
                
            # Rule 2 & 3: Handle consonants and 'qu' special case
            else:
                # Handle 'qu' special case, whether at the beginning or within a consonant cluster
                if 'qu' in word:
                    qu_index = word.index('qu')
                    result.append(word[qu_index + 2:] + word[:qu_index + 2] + 'ay')
                else:
                    # Find the index of the first vowel
                    vowel_index = -1
                    for i, char in enumerate(word):
                        if char in vowels:
                            vowel_index = i
                            break
                    
                    # If no vowels are found (rare case)
                    if vowel_index == -1:
                        result.append(word + "ay")
                    else:
                        # Move consonants to end and add 'ay'
                        result.append(word[vowel_index:] + word[:vowel_index] + 'ay')
                    
        return " ".join(result)
        
    except AttributeError:
        return "Invalid input: Input must be a string"


# Test cases
print("\nPig Latin Tests:")
print(pig_latin("pig"))              # igpay
print(pig_latin("latin"))            # atinlay
print(pig_latin("apple"))            # appleay
print(pig_latin("quick"))            # ickquay
print(pig_latin("the quick brown"))  # ethay ickquay ownbray
print(pig_latin("quiet"))            # ietquay
print(pig_latin(""))                 # empty string
print(pig_latin("eat pie"))          # eatay iepay
print(pig_latin("string"))           # ingstray
print(pig_latin(123))                # Invalid input message
