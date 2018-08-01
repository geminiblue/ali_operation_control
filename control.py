import aliyunsdkcore.request

from services.aliyun.ecs import *
from services.aliyun.oss import *

aliyunsdkcore.request.set_default_protocol_type("https")
print(aliyunsdkcore.request)
