import base64

if __name__ == '__main__':

    # Original data
    data = "SGVsbG8sIFdvcmxkIQ=="

    decoded_data = base64.b64decode(data).decode()

    print(decoded_data)
