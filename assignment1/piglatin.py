def pig_latin(text):
    try:
        # Convert to lowercase and split into words
        words = text.lower().split()
        result = []
        vowels = 'aeiou'
        
        for word in words:
            if not word:  # Skip empty strings
                continue
                
            # Rule 1: If word starts with vowel
            if word[0] in vowels:
                result.append(word + "ay")
                
            # Rule 2 & 3: Handle consonants and 'qu' special case
            else:
                # Handle 'qu' special case
                if word.startswith('qu'):
                    result.append(word[2:] + 'quay')
                elif len(word) > 2 and word[1] == 'u' and word[0] != 'q':
                    # Handle consonant + u case (but not qu)
                    result.append(word[1:] + word[0] + 'ay')
                else:
                    # Find the index of the first vowel
                    vowel_index = 0
                    for i, char in enumerate(word):
                        if char in vowels:
                            vowel_index = i
                            break
                    # Move consonants to end and add 'ay'
                    result.append(word[vowel_index:] + word[:vowel_index] + 'ay')
                    
        return " ".join(result)
        
    except AttributeError:
        return "Invalid input: Input must be a string"
