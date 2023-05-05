# 1)1 - 5000 - Zion National Park - camping - PP - 1 - HO - Zion National Park - 2
#
# 2)2 - 500 - 5000 - Bryce Canyon National Park - wildlife - BA - Zion National Park - trails - 2

print("Hello and welcome to the National Park Searcher!")
print("Here, you can get information about three national parks: ")
print("Zion National Park, Bryce Canyon National Park, and Grand Canyon National Park")

user_input = input("Choose 1 to login and 2 to signup: ")

if user_input == "1":
    username = input("Enter your username: ")
    print("Password should have a minimum of 8 letters, 4 numbers, one special symbol, and an uppercase letter")
    password = input("Enter your password: ")
elif user_input == "2":
    fname = input("Your first name: ")
    lname = input("Your last name: ")
    username = input("Create your username: ")
    print("Password should have a minimum of 8 letters, 4 numbers, one special symbol, and an uppercase letter")
    password = input("Create your password: ")

enter = input("Enter a four digit verification code: ")
while enter != "5000":
    print("Invalid code. Please try again.")
    enter = input("Enter a four digit verification code: ")
print("Verified")

print("\n")

print("National Park Searcher")
print("National Parks: Zion National Park, Bryce Canyon National Park, Grand Canyon National Park")

user_give = input("Choose any national park from the ones listed above: ")

if user_give == "Zion National Park":
    user_say = input("Choose camping, wildlife, or trails: ")
    if user_say == "camping":
        print("Total campgrounds: 3")
        print("Names: Lava Point Campground, South Campground, and Watchman Campground")
        print("Lava Point Campground: No internet, ice or laundry. Only trash collection and staff")
        print("South Campground: Laundry, gas, and groceries available within one mile")
        print("Watchman Campground: Flush toilets, firewood, and laundry available within one mile")
    elif user_say == "wildlife":
        print("Zion National Park has a lot of wildlife to view and is a beautiful place for nature lovers!")
        print("Wildlife: Desert Bighorn Sheep, Mountain Lion, Mule Deer, Ringtail Cat, Rock Squirrel, Beaver, Bobcat, "
              "Porcupine, Coyote, Gray Fox, Bats, Western Rattlesnake, Common Chuckwalla, Desert Tortoise, "
              "Mexican Spotted Owl, California Condor, Cooper's Hawk, and many more!")
    elif user_say == "trails":
        print("Zion National Park has lots of trails to walk!")
        print("Here's a few of them: ")
        print("Angels Landing Trail, Riverside Walk, West Rim Trail, Emerald Pools Trial, Watchman Trail, Zion Canyon "
              "Overlook Trail, Lower Emerald Pool Trail, Parus Trail, East Mest Trail, Kayenta Trail")
    else:
        print("You entered something wrong!")

elif user_give == "Bryce Canyon National Park":
    user_say = input("Choose camping, wildlife, or trails: ")
    if user_say == "camping":
        print("Total campgrounds: 2")
        print("Names: North Campground and Sunset Campground")
        print("North Campground: Seasonal laundry, firewood, and ice for sale. No internet or food storage lockers")
        print("Sunset Campground: Seasonal firewood, camp store, and dump station. No internet or food storage lockers")
    elif user_say == "wildlife":
        print("Bryce Canyon National Park has a lot of wildlife to view and is a beautiful place for nature lovers!")
        print("Wildlife: Squirrels, Prarrie Dogs, Proghorn Sheep, Coyotes, Gray Foxes, Mice, Bats, Elk, Badger, "
              "Ringtail, Peregrine Falcon, Uinta chipmunk, Great Basin Rattlesnake, Raccoon, Mountain Lion, "
              "Black Bear and many more!")
    elif user_say == "trails":
        print("Bryce Canyon National Park has lots of trails to walk!")
        print("Here's a few of them: ")
        print("Navajo Loop Trail, Queens Garden Trail, Fairyland Loop Trail, Peekaboo Loop Trail Rim Trail, "
              "Mossy Cave Trail, Under-the_Rim Trail")
    else:
        print("You entered something wrong!")

while True:
    user_choice = input("Enter BA for searching back a national park, PP for reading the privacy policy, and HO for "
                        "knowing any hotels around a national park:")

    if user_choice == "BA":
        print("National Park Searcher")
        print("National Parks: Zion National Park, Bryce Canyon National Park, Grand Canyon National Park")
        user_give = input("Choose any national park from the ones listed above: ")
        if user_give == "Zion National Park":
            user_say = input("Choose camping, wildlife, or trails: ")
            if user_say == "camping":
                print("Total campgrounds: 3")
                print("Names: Lava Point Campground, South Campground, and Watchman Campground")
                print("Lava Point Campground: No internet, ice or laundry. Only trash collection and staff")
                print("South Campground: Laundry, gas, and groceries available within one mile")
                print("Watchman Campground: Flush toilets, firewood, and laundry available within one mile")
            elif user_say == "wildlife":
                print("Zion National Park has a lot of wildlife to view and is a beautiful place for nature lovers!")
                print(
                    "Wildlife: Desert Bighorn Sheep, Mountain Lion, Mule Deer, Ringtail Cat, Rock Squirrel, Beaver, "
                    "Bobcat, Porcupine, Coyote, Gray Fox, Bats, Western Rattlesnake, Common Chuckwalla, "
                    "Desert Tortoise, Mexican Spotted Owl, California Condor, Cooper's Hawk, and many more!")
            elif user_say == "trails":
                print("Zion National Park has lots of trails to walk!")
                print("Here's a few of them: ")
                print(
                    "Angels Landing Trail, Riverside Walk, West Rim Trail, Emerald Pools Trial, Watchman Trail, "
                    "Zion Canyon Overlook Trail, Lower Emerald Pool Trail, Parus Trail, East Mest Trail, Kayenta Trail")
            else:
                print("You entered something wrong!")

        elif user_give == "Bryce Canyon National Park":
            user_say = input("Choose camping, wildlife, or trails: ")
            if user_say == "camping":
                print("Total campgrounds: 2")
                print("Names: North Campground and Sunset Campground")
                print(
                    "North Campground: Seasonal laundry, firewood, and ice for sale. No internet or food storage lockers")
                print(
                    "Sunset Campground: Seasonal firewood, camp store, and dump station. No internet or food storage lockers")
            elif user_say == "wildlife":
                print(
                    "Bryce Canyon National Park has a lot of wildlife to view and is a beautiful place for nature lovers!")
                print(
                    "Wildlife: Squirrels, Prarrie Dogs, Proghorn Sheep, Coyotes, Gray Foxes, Mice, Bats, Elk, Badger, "
                    "Ringtail, Peregrine Falcon, Uinta chipmunk, Great Basin Rattlesnake, Raccoon, Mountain Lion, "
                    "Black Bear and many more!")
            elif user_say == "trails":
                print("Bryce Canyon National Park has lots of trails to walk!")
                print("Here's a few of them: ")
                print("Navajo Loop Trail, Queens Garden Trail, Fairyland Loop Trail, Peekaboo Loop Trail Rim Trail, "
                      "Mossy Cave Trail, Under-the_Rim Trail")
            else:
                print("You entered something wrong!")

        user_tell = input("Choose 1 to enter your choice or 2 to break: ")
        if user_tell == "1":
            continue
        elif user_tell == "2":
            break

    elif user_choice == "PP":
        print("Privacy Policy: This app will take your personal information to get an advanced plan. Your name, "
              "email address, and phone number maybe required to share the location of this app. This app would "
              "disassociate all the private data after 48 hours after the location has been shared with others. This "
              "app will collect information using cookies and try preventing the spread of the information to "
              "third-party websites. Try not to share any private information on a non-trusted website. This website "
              "is secure and well built to prevent security attacks. ")
        user_tell = input("Choose 1 to enter your choice or 2 to break: ")
        if user_tell == "1":
            continue
        elif user_tell == "2":
            break
    elif user_choice == "HO":
        user_bolo = input("Choose a national park to know the hotels around the national park: ")

        if user_bolo == "Zion National Park":
            print("There are many hotels around Zion National park but here's a list of them")
            print("Zion Lodge, Majestic View Lodge, Cliffrose Lodge & Gardens, Cable Mountain Lodge, Driftwood Lodge, "
                  "Zion Canyon Campground & RV Resort, Desert Pearl Inn, Pioneer Lodge, Zion Mountain Ranch, "
                  "Under Canvas Zion. ")
        elif user_bolo == "Bryce Canyon National Park":
            print("There are many hotels around Bryce Canyon National park but here's a list of them")
            print("Bryce Canyon Lodge, Best Western Plus Ruby's Inn, Bryce View Lodge, The Lodge at Bryce Canyon, "
                  "Stone Canyon Inn, Bryce Canyon Inn, Bryce Canyon Grand Hotel, Burffalo Sage Bed & Breakfast, "
                  "Bryce Pioneer Village, Bryce Trails Bed & Breakfast ")
        else:
            print("You entered something wrong!")

        user_tell = input("Choose 1 to enter your choice or 2 to break: ")
        if user_tell == "1":
            continue
        elif user_tell == "2":
            break
    else:
        print("Invalid choice. Please enter BA, PP, or HO.")
        continue

print("Thanks for using our app!")
