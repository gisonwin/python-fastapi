import collections

from google.protobuf import json_format

import tst_devs_param_pb2
import SZDFH_public_pb2
import search_pb2
import tst_devs_cmd_pb2

# search_request = search_pb2.SearchRequest()
# search_request.query = "a query string"
# search_request.page_number = 1
# search_request.result_per_page = 9
# #
# print(search_request.SerializeToString())

resp = search_pb2.SearchResponse()
result = search_pb2.Result()
result.url = "https://www.google.com"
result.title = "How to learn Google AGI"

snippets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# 列表用extend添加  单个元素用append
result.snippets.extend(snippets)
result.snippets.append('TTTTTTTTTTTTTTTTTTTT')
# print(result.SerializeToString())
resp.results.append(result)


adict = {"key_a": "value_a"}

print("search_response", resp.SerializeToString())
#
# sr2 = search_pb2.SearchRequest()
# sr2.ParseFromString(search_request.SerializeToString())
# print(json_format.MessageToDict(search_request, True))
#
# print(json_format.MessageToJson(search_request, True))

############
# message Request
# {
#   string  strDevCode = 1;  //设备code.
#   string  strParamCode = 2;  //属性code.
#
#   //附加
#   bytes  keyTcpLink = 3;    //tcp link socke句柄
#   string    water_id = 4;//业务流水号(确保全局唯一，建议GUID字符串)
# }


# param_request = tst_devs_param_pb2.Request()
#
# param_request.strDevCode = "LS1TM1"
# param_request.strParamCode = "TMBin"
# param_request.water_id = "F0000Q987664"
#
# param_str = param_request.SerializeToString()
# print(param_str)

# param_response = tst_devs_param_pb2.Respond()
# param_response._Respond.fields
# param_response.strDevCode = "LS1TM1"
# param_response.strParamCode = "TMBin"
# param_response.iParamRet = 0
# # SZDFH_public_pb2.PUB_EDevState.LOAD.value = 0
# param_response.PUB_EDevState.LOAD.value = 1
# param_response.water_id = "F0000Q987664"
# param = SZDFH_public_pb2.Param()
# pub_e_datatype = SZDFH_public_pb2.Param.PUB_EDataType()
# pub_e_datatype.t_int32 = 1
# param.PUB_EDataType.
# print(param_response)


# dev_cmd_request = tst_devs_cmd_pb2.Request()
# dev_cmd_request.strDevCode = "LS1TC1"
# dev_cmd_request.strCmdCode = "Voltage"
# dev_cmd_request.strChannel = "1.1"
# map_param = SZDFH_public_pb2.MapParam()
# param = SZDFH_public_pb2.Param()
# param.nDataKind = SZDFH_public_pb2.PUB_EDataType.t_int32
# param.v_int32 = 334
# # which_one_of = param.WhichOneof('value')
# # print(which_one_of)
# # dv = getattr(param, which_one_of).value
# # print(dv)
# print(param)
# # map_param.mapParam['TMBin'].CopyFrom(param)
# adic = {"tmBin": param}
# print(type(adic))
# print(type(adic["tmBin"]))
# print(type(map_param.mapParam))
# new_dic = map_param.mapParam.update(adic)
# print("new_dic", new_dic)
#
# # dic1 = {"TMBin": param}
# # map_param.mapParam = var1
#
# print(map_param.SerializeToString())
# # dev_cmd_request.mapParam = map_param
# # map_param.nDataKind = data_type
# print(dev_cmd_request.SerializeToString())
