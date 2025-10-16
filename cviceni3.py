def my_range(start, stop, step=1):
    result = []
    while start < stop:
        result.append(start)
        start += step
    return result
    
def while_enumerate(text, start=1):
    index = start - 1
    result = []
    while index < len(text):
        result.append((index + 1, text[index]))
        index += 1
    return result

if __name__ == "__main__":
    text = "abcdef"
    print(list(enumerate(text, 1)))
    print(list(while_enumerate(text, 1)))



    #print(list(range(1, 20, 2)))
    #print(list(my_range(1, 20, 2)))