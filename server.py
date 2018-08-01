from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound,ServerError,InvalidUsage
app = Sanic()

@app.exception(NotFound)
async def not_found(request,exception):
    return json({
        "code":404,
        "message":"not found"
    },status=404)

@app.exception(InvalidUsage)
async def invalid_usage(request,exception):
    return json({
        "code":400,
        "message":"method not allowed"
    },status=400)

@app.exception(ServerError)
async def service_error(request,exception):
    return json({
        "code":500,
        "message":"service error"
    },status=500)

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/login',methods=['POST','GET'])
async def login(request):
    return json({})

if __name__ == '__main__':
    app.run(host='0.0.0.0', 
    port=8000,
    debug=False,
    access_log=False,
    workers=4)