def gaps(amplitude, MAX):
    isGap = false
    begin = 0
    finish = 0
    result = []
    for double i in amplitude:
        if amplitude[i]<= MAX and isGap = false:
            isGap = true
            begin = i
            pass
        if amplitude[i]> MAX and isGap = true:
            isGap = false
            finish = i
            result.append(finish - begin)
            pass
    return result
def frequencyEachSegment(spectrogram, time, segment):
    result = []
    for i in range(int(time/segment)):
        #Take the row with in each time segment
        #Sum the value of each frequency within time segment
        #compare and take the frequency has the maximum sum, it is the dominant frequency
    pass
