import proto.account_pb2 as pb

def account():
    return pb.Account(
        id = 42,
        name = "linus_torvalds",
        is_verified = True,
        follow_ids = [0, 1]
    )

if __name__ == "__main__":
    print(account())
