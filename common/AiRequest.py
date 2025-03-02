import requests

from config import api_key


def requestAi(prompt):
    baseurl='https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions'

    headers={
        "Authorization":"Bearer %s"%api_key,
        "Content-Type":"application/json"
    }
    data={
        "model": "qwen-plus",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    return requests.post(baseurl, json=data, headers=headers).json()['choices'][0]["message"]['content']


if __name__=="__main__":
    print(requestAi("你是一个测试工程师，你可以把自然语言编写成测试用例，用例的关键字：start： 启动,打开，tap：点击，assert：断言，input：输入。"
                    "参考转换例子：启动qq，点击登陆,断言登陆  转换成：start=qq|tap=登陆|assert=登陆，请根据上面的要求设计下面的用例：打开flutterapp,点击登陆，点击用户名输入159，点击密码输入123456，点击登陆，判断出现首页。"
                    "返回json格式数:[{'set':'start=qq|tap=登陆'}]，只返回转换后的测试用例"))
