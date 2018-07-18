# platPos = platform position at a pulse index
# pulseNumber = the index of the pulse
# rangeBin = the range bin being called repeatedly, iterated
# iterate = the value used to calculate sum
def matrix(numRangeBins, pulses):
    matrix = np.array(ndim=3)
    for a in range(numRangeBins): #set scene pixels
        finalMatrix =  pulses[a]# the final value
        referencePulse = 0
        rangeBinOrig = 0 # range bin original, the range bin of the point being measured, at the first index
        for i in range(100):
            finalMatrix += rangeDelay(pulses[i])
       # matrix['''gps location''']['''a'''] = np.amax(abs(finalMatrix))
    return matrix
    
    def rangeDelay(platPosX, platPosY, platPosZ):
# calculates the range delay for a row using platPos and RangeBinOrig
# previous formula  return(np.subtract(np.sqrt(np.add(np.square(platPos), np.square(RangeBinOrig))), RangeBinOrig))
   return np.sqrt(np.add(np.square(np.subtract(platPosX, pixelPosX)), np.square(np.subtract(platPosY, pixelPosY)), np.square(np.subtract(platPosZ, pixelPosZ))))
def intensity(pulseNumber, rangeBin):
   # has to read the intensity with pulse number and the range bin
   return None
def platform(pulseNumber):
   # has to read the platform position with the pulse number
   return None 
def pixelBrightness(rangeBinOrig, pixelPosX, pixelPosY, pixelPosZ):
    # calculates the brigtness of a pixel
    final = 0
    for pulseNumber in range(100): # substitute 0 with number of rows
        #pulseNumber+= 1
        iterate = intensity(pulseNumber, rangeBinOrig + rangeDelay(platform(pulseNumber)))
        # might be rangeBinOrig - rangeDelay(platform(pulseNumber), have to test if plus or minus
        final+= iterate
    return final
