from .router import director_view,worker
import asyncio

@director_view('add')
async def add(a,b):
    worker.call('sub',{'a':a,'b':b}  ,lambda x:print(x)  )
    worker.call('multi',{'a':a,'b':b},lambda x:print(x))
    worker.call('log',{'msg':'正在调用后端加函数'})
    worker.call('log',{'msg':'哈哈哈'})
    #print( await worker.call('multi',{'a':a,'b':b}) )
    #await worker.call('log',{'msg':'正在调用后端加函数'})
    #await worker.call('log',{'msg':'哈哈哈'})
    #await front_print()
    return int(a)+ int(b)

@director_view('front_print')
async def front_print():
    await worker.call('log',{'msg':'调用front print'})
    print('front_print')

#async def run():
    #while True:
        #await asyncio.sleep(2)
        #if getattr(worker,'websocket',None):
            #await worker.call('log',{'msg':'定时发送'})
        

#asyncio.get_event_loop().create_task(run())