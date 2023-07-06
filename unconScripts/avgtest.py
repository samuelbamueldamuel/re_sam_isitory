def shooter(three, mid, standShot, moveShot):
    average = (int(three) + int(mid) + int(standShot) + int(moveShot)) / 4
    return average

print(shooter(50, 50, 50, 50))
