def main(array, sequence):
    place = 0
    for value in array:
        if place == len(sequence):
            break
        if sequence[place] == value:
            place += 1

    
    print(place == len(sequence))
    return place == len(sequence)

if __name__ == '__main__':
    #correct
    main([5,1,22,25,6,-1,8,10],[5,1,6,22])
    #wrong order
    main([5,1,22,25,6,-1,8,10],[5,1,22,6])
    #repeated sequence
    main([5,1,22,25,6,-1,8,10],[5,1,22,22,6])