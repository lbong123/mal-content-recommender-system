with open("userList.txt", 'r') as userList:
    users = userList.readlines()
    uniqueUsers = set(users)

    with open("uniqueUserList.txt", "w") as uniqueUserList:
        uniqueUserList.writelines(uniqueUsers)

