def normalize_signal(data):
    if len(data) == 0:
        raise ValueError("Empty input")
    
    mean = sum(data) / len(data)
    return [x - mean for x in data]