from sanic import Sanic
from sanic.response import json
from sanic.exceptions import NotFound,ServerError,InvalidUsage
from sanic_openapi import doc,swagger_blueprint, openapi_blueprint
app = Sanic()
app.config.API_CONTACT_EMAIL = 'oliyo@qq.com'
app.blueprint(openapi_blueprint)
app.blueprint(swagger_blueprint)

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
@doc.summary("Default router by test")
@doc.produces({ "user": { "name": str, "id": int } })
async def test(request):
    return json({'hello': 'world'})

@app.route('/login',methods=['POST','GET'])
async def login(request):
    return json({})

@app.websocket('/feed')
async def feed(request, ws):
    while True:
        data = 'hello!'
        print('Sending: ' + data)
        await ws.send(data)
        data = await ws.recv()
        print('Received: ' + data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', 
    port=8080,
    debug=True,
    access_log=True,
    workers=4)