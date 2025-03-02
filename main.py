from common.AiRequest import requestAi
from common.parsecase import run
from config import device


'''
1.这里是演示的demo
  需要注册阿里云的大模型的接口，生成用例通过阿里云来生成
2.demo只支持单设备运行，需要自己开发多设备并且的
3.只是演示在UI上面去封装的方法， 利用点击，输入操作，Android  harmony进行简单封装
4.可以去开发支持不同的系统的

'''
case = "打开flutterapp,点击登陆，点击用户名输入159，点击密码输入123456，点击登陆，判断出现首页。"

def main():
    global case
    prompt="你是一个测试工程师，你可以把自然语言编写成测试用例，用例的关键字：start： 启动,打开，tap：点击，assert：断言，input：输入。参考转换例子：启动qq，点击登陆,断言登陆  转换成：start=qq|tap=登陆|assert=登陆，请根据上面的要求设计下面的用例：%s 返回json格式数:[{'set':'start=qq|tap=登陆'}]，只返回转换后的测试用例"%case

    case=requestAi(prompt)
    try:
        caselist=[]
        caselistpase=eval(str(case).split("```")[1].split("\n")[1])
        for case in caselistpase:
            caselist.append(case['set'])
        print(caselistpase)
        run(device=device,caselist=caselist)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
