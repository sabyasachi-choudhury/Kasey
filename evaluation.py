import random
import main as mn

chars = 'qwertyuiopasdfghjklzxcvbnm     '


def test(epochs):
    probs = []
    correct_detections = []
    for x in range(epochs):
        word = ""
        for y in range(random.randint(8, 25)):
            word += random.choice(chars)
        prediction = mn.classify(word)
        if prediction:
            probs.append(prediction[0][1])
            # print(word)
        else:
            correct_detections.append(word)
    avg = sum(probs)/len(probs) * 100
    print(avg)
    print(len(correct_detections))
    return avg


averages = []
for x in range(10):
    print("Epoch:", x+1)
    averages.append(test(1000))

print("Big avg:", sum(averages)/len(averages))