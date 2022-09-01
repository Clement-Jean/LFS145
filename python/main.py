import sys
import proto.account_pb2 as account_pb
import proto.user_pb2 as user_pb
import proto.product_pb2 as product_pb
import proto.phone_book_pb2 as phone_book_pb
import proto.login_pb2 as login_pb
import google.protobuf.any_pb2 as any_pb

def account():
    return account_pb.Account(
        id=42,
        name='linus_torvalds',
        is_verified=True,
        follow_ids=[0, 1]
    )

def user():
    return user_pb.User(
        id=42,
        name='Linus Torvalds',
        follows=[
            user_pb.User(id=0, name='Linux Foundation'),
            user_pb.User(id=1, name='Clement Jean'),
        ]
    )

def user2():
    message = user_pb.User()
    message.id = 42
    message.name = 'Linus Torvalds'
    message.follows.add(id=0, name='Linux Foundation')
    message.follows.add(id=1, name='Clement Jean')
    return message

def product():
    return product_pb.Product(
        id=42,
        product_type=product_pb.ProductType.PANTS # 1
    )

def phone_book():
    return phone_book_pb.PhoneBook(
        phones={
            'Linus Torvald': '11111111',
            'Clement Jean': '22222222'
        }
    )

def phone_book2():
    book = phone_book_pb.PhoneBook()
    book.phones['Linus Torvald'] = '11111111'
    book.phones['Clement Jean'] = '22222222'
    return book

def login_error():
    result = login_pb.LoginResult()
    result.error = 'The username or password are not correct'
    return result

def login_success():
    return login_pb.LoginResult(
        token = login_pb.Token()
    )

def any_value():
    num = 7

    return [
        any_pb.Any(value=num.to_bytes(2, byteorder='big')),
        any_pb.Any(value=num.to_bytes(2, byteorder='little')),
        any_pb.Any(value=bytes('test', 'utf-8'))
    ]

if __name__ == '__main__':
    fns = {
        'account': account,
        'user': user,
        'user2': user2,
        'product': product,
        'phone': phone_book,
        'phone2': phone_book2,
        'logine': login_error,
        'logins': login_success,
        'any': any_value
    }

    if len(sys.argv) != 2:
        print(f'Usage: main.py [{"|".join(fns)}]')
        sys.exit()

    fn = fns.get(sys.argv[1], None)

    if not fn:
        print(f'Unknown function: \'{sys.argv[1]}\'')
        sys.exit()

    print(fn())
