# Name:     Pacopac,Ace M.
# Section:  IV-BSIT A




PASSING_AVERAGE = 75   


def compute_average(grades):
    return sum(grades) / len(grades)


def get_status(average, passing=PASSING_AVERAGE):
    return "PASSED" if average >= passing else "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)



if __name__ == "__main__":
    sample = [80, 90, 70]
    print("Testing student_utils with", sample)
    print("Average:", compute_average(sample))   # 80.0
    print("Status: ", get_status(74.5))          # bagsak to
    print("Highest:", get_highest(sample))       # 90
    print("Lowest: ", get_lowest(sample))        # 70