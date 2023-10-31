# http_status_code = 400

http_status_code = input("Enter http status code: ")
http_status_code = int(http_status_code)

match http_status_code:
    case 100 | 101:
        print("Informational")
    case 200 | 201 | 202 | 204:
        print("Successful")
    case 301 | 302:
        print("Redirection")
    case 400 | 401 | 403 | 404 | 405:
        print("Client Error")
    case 500 | 502 | 503:
        print("Sever Error")
    case _:
        print("Unknown")
