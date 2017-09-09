friends = input("Friends? ")
friendNum = int(friends)

if friendNum < 500:
    friendNum = friendNum // 100 * 10
elif friendNum > 500:
    friendNum = friendNum // 500 * 5 + 25

print(friendNum)