sample_input='abc'
def add_ing(sample_input):
    num = len(sample_input)
    if num  >= 3:
        sample_input+='ing'
    else:

        sample_input+='ly'

    return sample_input


print(add_ing(sample_input))