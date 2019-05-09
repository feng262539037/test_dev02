from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import json


# Create your views here.


def testcase_manage(request):
    return render(request, 'testcase.html', {'type': 'debug'})


def testcase_debug(request):
    """
    测试用例的调试
    """
    if request.method == "POST":
        url = request.POST.get("url", "")
        method = request.POST.get("method", "")
        header = request.POST.get("header", "")
        type_ = request.POST.get("type", "")
        parameter = request.POST.get("parameter", "")
        print("url是:", url)
        print("method是:", method)
        print("前端传入的header是:", header,'类型是:', type(header))
        print("type_是:", type_)
        # parameter类型是str
        print("前端传入的parameter是:", parameter, '类型是:', type(parameter))

        # 前端传入的header:把单引号替换为双引号
        json_header = header.replace("\'", "\"")
        # 需要把header的类型从str转成dict
        try:
            header = json.loads(json_header)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "header类型错误"})
        print('最终的header是:', header, '类型是:', type(header))

        # 前端传入的parameter:把单引号替换为双引号
        json_par = parameter.replace("\'", "\"")
        # 需要把parameter的类型从str转成dict
        try:
            payload = json.loads(json_par)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result": "参数类型错误"})
        print('最终的payload是:', payload, '类型是:', type(payload))

        # # 需要把parameter的类型从str转成dict
        # payload = json.loads(json_par)
        # print('payload是:', payload, '类型是:', type(payload))

        if method == 'get':
            if header == '':
                # params要字典！！！
                r = requests.get(url, params=payload)
                print('get请求,在cmd控制台打印返回结果是:', r.json())
            else:
                r = requests.get(url, params=payload,headers=header)
                print('get请求,在cmd控制台打印返回结果是:', r.json())

        elif method == 'post':
            if type_ == 'form':
                if header == '':
                    r = requests.post(url, data=payload)
                    print('post请求,类型是form,在cmd控制台打印返回结果是:', r.json())
                else:
                    r = requests.post(url, data=payload,headers=header)
                    print('post请求,类型是form,在cmd控制台打印返回结果是:', r.json())
            elif type_ == 'json':
                if header == '':
                    r = requests.post(url, json=payload)
                    print('post请求,类型是json,在cmd控制台打印返回结果是:', r.json())
                else:
                    r = requests.post(url, data=payload, headers=header)
                    print('post请求,类型是form,在cmd控制台打印返回结果是:', r.json())
        # 把返回的结果，以文本的格式返回给前端
        return JsonResponse({'result': r.text})
    else:
        return JsonResponse({'result': '请求方法错误'})

def testcase_assert(request):
    '''
    测试用例的断言
    '''
    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")
        print('接口返回结果是:', result_text, '类型是:', type(result_text))
        print('断言的文本是:', assert_text, '类型是:', type(assert_text))
        print('断言类型是:', assert_type)

        if result_text == '' or assert_text == '':
            return JsonResponse({'result': '断言的文本不能为空'})

        if assert_type == 'contains':
            if assert_text not in result_text:
                return JsonResponse({'result': '断言失败'})
            else:
                return JsonResponse({'result': '断言成功'})
        elif assert_type == 'matches':
            if assert_text != result_text:
                return JsonResponse({'result': '断言失败'})
            else:
                return JsonResponse({'result': '断言成功'})

    else:
        return JsonResponse({'result': '请求方法错误'})
















