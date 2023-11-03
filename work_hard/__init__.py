def add_ing(sample_input):
    num = len(sample_input)
    if num >= 3:
        sample_input += 'ing'
    else:

        sample_input += 'ly'

    return sample_input



def add_ly(sample_input):
    num= len(sample_input)
    if num > 3:
        sample_input+='ly'
    else:
        sample_input+='ing'
    return sample_input

def add_it(sample_input):
    num=len(sample_input)
    if num < 3:
        sample_input +=''
    else:
        sample_input+='it'
    return sample_input

