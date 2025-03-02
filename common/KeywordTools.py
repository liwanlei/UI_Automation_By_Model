from common.exectionFunction import Exection


def KeywordTools(device,typed,connect):
    exection=Exection(device)
    if typed=="start" or typed=='open':
        return  exection.open(connect)
    elif typed=="tap":
        return  exection.open(connect)
    elif typed=="assert":
        return  exection.asserttext(connect)
    elif typed=="input":
        return  exection.input(connect)
    return False
