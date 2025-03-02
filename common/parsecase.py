from common.Data import Case
from common.KeywordTools import KeywordTools


def parsecase(caselist:list)->list:
    caseparselist=[]
    for item in caselist:
        onecase=str(item).split("&")
        casesetlist=[]
        for items in onecase:
            caseset=items.split("=>")
            caseset_=Case(connet=caseset[-1],acction=caseset[0])
            casesetlist.append(caseset_)
        caseone={item,casesetlist}
        print("case解析后")
        print(caseone)
        caseparselist.append(caseone)
    return caseparselist

def execset(casesetlist:list,device):
    for set in casesetlist:
        print("开始执行case的步骤")
        print(set)
        KeywordTools(device=device,typed=set.acction,connect=set.connet)
def run(device,caselist):
    print("开始解析case。。。。。。")
    caseparselist=parsecase(caselist)
    print("解析后的case")
    print(caseparselist)
    print("开始执行case")
    execset(caseparselist,device)
    print("执行case结束")