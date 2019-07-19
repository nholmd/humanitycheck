import random as rand

num_tests = 5

def test_humanity():
    test = rand.randrange(0, num_tests, 1)
    # test = 4
    if test == 0:
        # Wordy Math
        nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        ind1 = rand.randrange(0, 9, 1)
        ind2 = rand.randrange(0, 9, 1)
        dif = (ind1 + 1) - (ind2 + 1)
        print("What is " + nums[ind1] + " minus " + nums[ind2] + "?")
        print("(Respond with a number)")
        response = input()
        if (int(response) != dif):
            return False
        else:
            return True
    elif test == 1:
        # Odd-one-out
        colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white", "black"]
        animals = ["cat", "dog", "mouse", "chicken", "duck", "squirrel", "giraffe", "monkey", "tiger", "zebra"]
        nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
        emotions = ["happy", "sad", "angry", "frustrated", "scared", "confused", "tired", "bored", "inspired", "hungry"]

        # Select list 1
        rd = rand.randrange(0,3,1)
        if rd == 0:
            lst1 = colors
        elif rd == 1:
            lst1 = animals
        elif rd == 2:
            lst1 = nums
        elif rd == 3:
            lst1 == emotions
        
        # Select list 2
        while True:
            rv = rand.randrange(0,3,1)
            if rd != rv:
                break
        if rv == 0:
            lst2 = colors
        elif rv == 1:
            lst2 = animals
        elif rv == 2:
            lst2 = nums
        elif rv == 3:
            lst2 == emotions

        result = ""
        odd = ""
        odd_ind = rand.randrange(0, 3, 1)
        for i in range(4):
            if odd_ind == i:
                odd = lst1[rand.randrange(0, len(lst1) - 1, 1)]
                result += odd + " "
            else:
                result += lst2[rand.randrange(0, len(lst2) - 1, 1)] + " "
        print("Choose the odd-one-out")
        print(result)
        response = input()
        if response == odd:
            return True
        else:
            return False
    elif test == 2:
        lst1 = ["hot", "small", "happy", "short", "fast", "dangerous", "easy", "dark", "end", "alive", "night", "false", "empty"]
        lst2 = ["cold", "big", "sad", "tall", "slow", "safe", "difficult", "light", "begin", "dead", "day", "true", "full"]
        size = len(lst1)

        ind = rand.randrange(0, size, 1)
        ty = rand.randrange(0, 1, 1)
        if ty == 0:
            tmp = lst1
            lst1 = lst2
            lst2 = tmp

        print("What is the opposite of " + lst1[ind] + "?")
        response = input()
        if response == lst2[ind]:
            return True
        else:
            return False
    elif test == 3:
        lst1 = ["The Earth is the closest planet to the sun.", "Ice is cold.", "The sun is cold.", "four minus three is one.", "Ten plus two is five", "Cats usually walk on only two legs.", "Ants are smaller than tigers."]
        lst2 = ["false", "true", "false", "true", "false", "false", "true"]

        ind = rand.randrange(0, len(lst1), 1)

        print("Respond with true or false")
        print(lst1[ind])
        response = input()
        if response == lst2[ind]:
            return True
        else:
            return False
    elif test == 4:
        lst1 = ["cow", "fight", "sustain", "build", "smile", "dog", "god", "green", "blue", "plant", "planet", "happy", "sad", "innocent"]

        print("Please type this word in reverse:")
        ind = rand.randrange(0, len(lst1), 1)
        print(lst1[ind])
        response = input()
        if response[::-1] == lst1[ind]:
            return True
        else:
            return False





#  Code
pas = True
tests = 3
while tests > 0:
    tests -= 1
    if not test_humanity():
        pas = False
    print("")

if pas:
    print("You are human")
else:
    print("You are not human")