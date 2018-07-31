from services.aliyun.ecs import *
from services.aliyun.oss import *
import aliyunsdkcore.request
aliyunsdkcore.request.set_default_protocol_type("https")