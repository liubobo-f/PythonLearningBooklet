# 功能：输入时间，在时间到的时候提醒喝水。反复循环
import winsound
import time as t
def reminder():
     print("时间到，请喝水！")
     winsound.Beep(500, 1000)
def wait(time):
    t.sleep(time)
    
def input_time():
    time = input("请输入时间：（分钟）")
    # 等待time分钟
    time = int(time) # * 60
    return time
  
while True:
    time = input_time()
    wait(time)
    reminder()
    


    
    