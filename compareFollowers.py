from InstagramAPI import InstagramAPI

#add you username and password
api = InstagramAPI("", "")

def getTotalFollowers(api, username):
    api.searchUsername(username)
    response = api.LastJson
    user_id = response['user']['pk']

    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return followers

def getTotalFollowing(api, username):
    api.searchUsername(username)
    response = api.LastJson
    user_id = response['user']['pk']

    following = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowings(user_id, maxid=next_max_id)
        following.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
    return following

if (api.login()):
    #first person
    personOne = ""
    #second person
    personTwo = ""

    print("Processing Following")
    personOneFollowing = getTotalFollowing(api, personOne)
    personTwoFollowing = getTotalFollowing(api, personTwo)

    print("Processing Followers")
    personOneFollowers = getTotalFollowers(api, personOne)
    personTwoFollowers = getTotalFollowers(api, personTwo)

    bothFollowing = []
    bothFollowers = []


    for following in personOneFollowing:
        bothFollowing.append(following['username'])

    for following in personTwoFollowing:
        bothFollowing.append(following['username'])


    for follower in personOneFollowers:
        bothFollowers.append(follower['username'])

    for follower in personTwoFollowers:
        bothFollowers.append(follower['username'])

    duplicateFollowing = set([x for x in bothFollowing if bothFollowing.count(x) > 1])
    duplicateFollowers = set([x for x in bothFollowing if bothFollowing.count(x) > 1])

    print("duplicateFollowing: " + str(duplicateFollowing))
    print("duplicateFollowers: " + str(duplicateFollowers))


else:
    print("Can't login!")
