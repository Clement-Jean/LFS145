import sys
import datetime
import proto.account_pb2 as account_pb
import proto.user_pb2 as user_pb
import proto.product_pb2 as product_pb
import proto.phone_book_pb2 as phone_book_pb
import proto.login_pb2 as login_pb
import google.protobuf.any_pb2 as any_pb
import google.protobuf.duration_pb2 as duration_pb
import google.protobuf.timestamp_pb2 as timestamp_pb
import google.protobuf.field_mask_pb2 as field_mask_pb
import google.protobuf.struct_pb2 as struct_pb
import google.protobuf.wrappers_pb2 as wrappers_pb
from google.protobuf import json_format

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
        type=product_pb.ProductType.PANTS # 1
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

def duration():
    return duration_pb.Duration(
        seconds=3,
        nanos=0,
    )

def duration2():
    td = datetime.timedelta(days=3, minutes=10, microseconds=15)
    d = duration_pb.Duration()
    d.FromTimedelta(td)
    return d

def timestamp():
    t = timestamp_pb.Timestamp()
    t.GetCurrentTime()
    return t

def field_mask():
    acc = account()
    print(acc)
    fm = field_mask_pb.FieldMask(
        paths=[
            'id',
            'is_verified'
        ]
    )
    iiv = account_pb.Account()
    fm.MergeMessage(acc, iiv)
    return iiv

def field_mask2():
    mask = field_mask_pb.FieldMask()
    mask.FromJsonString('id,name')
    mask2 = field_mask_pb.FieldMask()
    mask2.FromJsonString('id,isVerified')
    mask3 = field_mask_pb.FieldMask()
    mask3.Union(mask, mask2)
    acc = account()
    print(acc)
    iniv = account_pb.Account()
    mask3.MergeMessage(acc, iniv)
    return iniv

def struct():
    return struct_pb.Struct(
        fields={
            'id': struct_pb.Value(number_value=42.0),
            'name': struct_pb.Value(string_value='Linus Torvalds'),
            'is_verified': struct_pb.Value(bool_value=True),
            'follow_ids': struct_pb.Value(list_value=struct_pb.ListValue(
                values=[
                    struct_pb.Value(number_value=float(0)),
                    struct_pb.Value(number_value=float(1)),
                ]
            )),
        }
    )

def struct2():
    s = struct()

    return s['name']

def wrapper():
    return [
        wrappers_pb.BoolValue(value=True),
        wrappers_pb.BytesValue(value=b'these are bytes'),
        wrappers_pb.FloatValue(value=42.0),
        # etc...
    ]

def to_json(message):
	return json_format.MessageToJson(
		message,
		indent=None,
		# preserving_proto_field_name=True
	)

def from_json(json_str, type):
	return json_format.Parse(
		json_str,
		type(),
		ignore_unknown_fields=True
	)

def file():
    acc = account()
    path = 'simple.bin'

    print('--Write to file--')
    print(acc)
    with open(path, 'wb') as f:
        bytes_as_str = acc.SerializeToString()
        f.write(bytes_as_str)

    print('--Read from file--')
    with open(path, 'rb') as f:
        t = type(acc)
        acc = t().FromString(f.read())

    print(acc)

def json():
    acc = account()
    json_str = to_json(acc)
    print(json_str)
    print('-------------------')
    print(from_json(json_str, account_pb.Account))
    print('--------------')
    print(from_json('{"id": 42, "unknown": "test"}', account_pb.Account))

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
        'any': any_value,
        'duration': duration,
        'duration2': duration2,
        'time': timestamp,
        'fm': field_mask,
        'fm2': field_mask2,
        'struct': struct,
        'struct2': struct2,
        'wrapper': wrapper,
        'file': file,
        'json': json,
    }

    if len(sys.argv) != 2:
        print(f'Usage: main.py [{"|".join(fns)}]')
        sys.exit()

    fn = fns.get(sys.argv[1], None)

    if not fn:
        print(f'Unknown function: \"{sys.argv[1]}\"proto')
        sys.exit()

    print(fn())
