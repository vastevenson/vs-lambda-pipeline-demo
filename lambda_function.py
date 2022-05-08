from ops import add,multiply,subtract,divide

def lambda_handler(event, context):
    # get the parameters from the API call, typecast appropriately
    x = int(event['queryStringParameters']['x'])
    y = int(event['queryStringParameters']['y'])
    op = str(event['queryStringParameters']['op'])

    # log the inputs
    print(f"Parsed inputs x:{x}, y:{y}, op:{op}")

    # prep the response body
    res_body = {}
    res_body['x'] = x
    res_body['y'] = y
    res_body['op'] = op
    res_body = prep_res_ans(res_body)

    # prep the http response
    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'application/json'
    http_res['body'] = res_body

def prep_res_ans(res_body):
    op = res_body['op']
    x = res_body['x']
    y = res_body['y']

    match op:
        case 'add':
            res_body['ans'] = add(x, y)
        case 'subtract':
            res_body['ans'] = subtract(x,y)
        case 'divide':
            res_body['ans'] = divide(x,y)
        case 'multiply':
            res_body['ans'] = multiply(x, y)
        case default:
            res_body['ans'] = 'Invalid input'

    return res_body