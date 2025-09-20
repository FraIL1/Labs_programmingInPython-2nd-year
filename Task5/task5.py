import math
def safe_apply(func, data):
    results = []
    errors = []

    for item in data:
        try:
            results.append(func(item))
        except Exception as e:
            errors.append((item, type(e).__name__))

    return results, errors


func = lambda x: math.sqrt(float(x))
data = ['4', '16', 'text', '-25', '9.0']

results, errors = safe_apply(func, data)

print(results)
print(errors)
