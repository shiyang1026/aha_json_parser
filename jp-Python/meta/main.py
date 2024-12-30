import json

def main():
    # Dictionary
    py_dict = {
        "name": "AlexShi",
        "age": 22,
        "city": "ShenZhen"
    }
    print(type(py_dict))

    # dumps(): Dictionary -> JSON string
    json.dumps(py_dict)
    print(type(json.dumps(py_dict)))
    print(json.dumps(py_dict))

    # dump(): Dictionary -> JSON file
    with open('data.json', 'w') as f:
        json.dump(py_dict, f)

    # loads(): JSON string -> Dictionary
    json_str = '{"name": "AlexShi", "age": 22, "city": "ShenZhen"}'
    print(type(json_str))
    print(json.loads(json_str))

    # load(): JSON file -> Dictionary
    with open('data.json', 'r') as f:
        print(json.load(f))

if __name__ == '__main__':
    main()