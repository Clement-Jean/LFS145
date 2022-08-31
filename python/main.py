import sys
import proto.account_pb2 as account_pb
import proto.user_pb2 as user_pb
import proto.product_pb2 as product_pb

def account():
    return account_pb.Account(
        id=42,
        name="linus_torvalds",
        is_verified=True,
        follow_ids=[0, 1]
    )

def user():
    message = user_pb.User()
    message.id = 42
    message.name = "Linus Torvalds"
    message.follows.add(id=0, name="Linux Foundation")
    message.follows.add(id=1, name="Clement Jean")
    return message

def user2():
    return user_pb.User(
        id=42,
        name="Linus Torvalds",
        follows=[
            user_pb.User(id=0, name="Linux Foundation"),
            user_pb.User(id=1, name="Clement Jean"),
        ]
    )

def product():
    return product_pb.Product(
        id=42,
        product_type=product_pb.ProductType.PANTS # 1
    )

if __name__ == "__main__":
    fns = {
        "account": account,
        "user": user,
        "user2": user2,
        "product": product
    }

    if len(sys.argv) != 2:
        print(f"Usage: main.py [{'|'.join(fns)}]")
        sys.exit()

    fn = fns.get(sys.argv[1], None)

    if not fn:
        print(f"Unknown function: \"{sys.argv[1]}\"")
        sys.exit()

    print(fn())
