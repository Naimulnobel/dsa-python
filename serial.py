import datetime
import random

def CreateSerial(serialsToMake, boardVariant):
    month = str(datetime.date.today().month)
    year = str(datetime.date.today().year)
    year2digit = year[2:4]
    monthandyear = int(year2digit)*12 + int(month)
    threedigit_base_rand = random.randint(0,999) #Need to add one to this as we loop to 999
    usedOffsets = []

    for x in range(serialsToMake):
        twodigit_end_rand = random.randint(0, 99)  # Need to add one to this as we loop to 999
        threedigitbase_rand_paddedstring = str(threedigit_base_rand).zfill(3)
        produnitno = threedigitbase_rand_paddedstring + str(twodigit_end_rand).zfill(2)
        print("monthandyear:",monthandyear)
        print("produnitno:",produnitno)
        serialNo = str(monthandyear) + produnitno + str(boardVariant)
        print(str(x) + " - " + serialNo)
        threedigit_base_rand = threedigit_base_rand - 1
        if (threedigit_base_rand < 0):
            #print ("threedigit_base_rand < 0 " + str(threedigit_base_rand))
            newOffset = False
            threedigit_offset_rand = 0
            while newOffset == False:
                threedigit_offset_rand = random.randint(0, 999)
                if (threedigit_offset_rand not in usedOffsets):
                    newOffset = True
                usedOffsets.append(threedigit_offset_rand)
            threedigit_base_rand = threedigit_offset_rand



CreateSerial(2000,"1")