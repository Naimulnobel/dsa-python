class StarCookie:

    def __init__(self,flavor, toppings, price, weight):
        self.flavor = flavor
        self.toppings = toppings
        self.price = price
        self.weight = weight
       


star_cookie = StarCookie("vanilla",["chocolate", "caramel"],2.0,0.5)

print(star_cookie)


class YouTube:
    def __init__(self, username, subscribers=0,subscription=0):
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription

    def subscribe(self,user):
        self.subscription += 1
        user.subscribers += 1


user1 = YouTube("John")
user2 = YouTube("Jane")

user1.subscribe(user2)

print(f'{user1.username} has {user1.subscribers} subscribers and {user1.subscription} subscriptions') #prints John has 1 subscribers and 1 subscriptions (user1.subscription)

print(f'{user2.username} has {user2.subscribers} subscribers and {user2.subscription} subscriptions') #prints Jane has 1 subscribers and 1 subscriptions (user2.subscription)