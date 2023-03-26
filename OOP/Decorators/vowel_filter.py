def vowel_filter(function):

    def wrapper():

        vowel_list = ['a','e','o','u','y','i']
        return [x for x in function() if x in vowel_list]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
