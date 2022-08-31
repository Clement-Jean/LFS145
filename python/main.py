import sys
import proto.account_pb2 as account_pb
import proto.user_pb2 as user_pb

def account():
    return account_pb.Account(
        id = 42,
        name = "linus_torvalds",
        is_verified = True,
        follow_ids = [0, 1]
    )

def user():
    message = user_pb.User()
    message.id = 42
    message.name = "Linus Torvalds"
    message.follows.add(id=0, name="Linux Foundation")
    message.follows.add(id=1, name="Clement Jean")
    return message

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: main.py [account]")
        exit()

    switcher = {
        "account": account,
        "user": user,
    }
    fn = switcher.get(sys.argv[1], None)

    if not fn:
        print(f"Unknown function: \"{sys.argv[1]}\"")
        exit()

    print(fn())
