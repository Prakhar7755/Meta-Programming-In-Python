# Introduced in version

http_status = 500

match http_status:
    case 200 | 210:
        print("SUCCESS")
    case 400:
        print("BAD REQUEST")
    case 500 | 510:
        print("SERVER ERROR")
    case _:
        print('Unknown')
