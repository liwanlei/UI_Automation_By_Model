import os
import subprocess


class HarmonyTools(object):
    def __init__(self, device):
        self.device = device

    def screen_pull(self, path):
        commandimg = "hdc -s {} shell screencap /sdcard/screen.png".format(self.device)
        os.system(commandimg)
        commandpull = "hdc -s {} pull /sdcard/screen.png {}".format(self.device, path)
        os.system(commandpull)

    def input(self, text):
        command = 'hdc -s  {}  shell input text  {}'.format(self.device, text)
        os.system(command)

    def tap(self, postion: tuple):
        command = 'hdc -s{} shell input tap {} {}'.format(self.device, postion[0], postion[1])
        os.system(command)

    def swap(self):
        position = self.__get_device_resolution()
        if position:
            y = int(position[1] / 2)
            x = int(position[0] / 4 * 3)
            x1 = int(position[0] / 4 * 1)
            command = 'hdc -s {}  shell input swipe {} {} {} {}'.format(self.device, x, y, x1, y)
            print(command)
            os.system(command)

    def __get_device_resolution(self, ):
        # 执行 hdc shell wm size 命令
        result = subprocess.run(['hdc', '-s', self.device, 'shell', 'wm', 'size'],
                                stdout=subprocess.PIPE,
                                text=True)

        # 获取命令输出
        output = result.stdout.strip()

        # 解析输出
        if 'Physical size:' in output:
            resolution_str = output.split('Physical size: ')[1]
            width, height = map(int, resolution_str.split('x'))
            return width, height
        else:
            print("无法识别的输出格式")
            return None

