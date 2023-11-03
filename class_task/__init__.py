def string_occurrences(sample):

    word = sample[0]

    sample = sample.replace(word, '$')

    return word + sample[1:]
