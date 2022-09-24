while True:
    p_range = [0, 11]
    fair = True
    try:
        guess, response = '', ''
        while response != 'right on':
            guess, response = int(input()), input()
            if response == 'too high':
                if guess <= p_range[0]:
                    fair = False
                else: 
                    p_range[1] = min(p_range[1], guess)
            elif response == 'too low':
                if guess >= p_range[1]:
                    fair = False
                else:
                    p_range[0] = max(p_range[0], guess)

    except EOFError:
        break
    if fair and guess > p_range[0] and guess < p_range[1]:
        print("Stan may be honest")
    else:    
        print("Stan is dishonest")
