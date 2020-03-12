import json
from functools import wraps
import asyncio
director = {}
director_views={}

def director_view(name): 
    def _fun(fun): 
        #director[name] = fun
        director_views[name] = fun
        @wraps(fun)
        def _fun2(*args, **kargs): 
            return fun(*args, **kargs)
        return _fun2
    return _fun

class Router(object):
    def __init__(self, *args, **kwargs):
        self.call_id = 0
        self.call_front ={}
        #self.call_queue = []
        #self.last_call_future = asyncio.get_event_loop().create_future()
        #self.last_call_future.set_result('')
        
    def setSocket(self,websocket):
        self.websocket = websocket
        
    async def parse(self,data):
        '''{fun:"bbb"}'''
        dc = json.loads(data)
        if dc.get('call_id'):
            #future = self.call_front.get(dc.get('call_id'))
            #future.set_result(dc.get('resp'))
            #self.call_front.pop( dc.get('call_id') )
            #self.last_call_future.set_result(dc.get('resp'))
            
            fun = self.call_front.get(dc.get('call_id'))
            if fun:
                fun(dc.get('resp') )
                self.call_front.pop( dc.get('call_id') )
        else:
            fun = director_views.get(dc.get('director_name') )
            kws = dc.get('data',{})
            if asyncio.iscoroutinefunction(fun):
                rt = await fun(**kws)
            else:
                rt = fun(**kws)
            rt_dc =  {'resp':rt,'count':dc.get('count')}
            rt_str =  json.dumps(rt_dc,ensure_ascii=False)
            return await self.websocket.send(rt_str)
    
    
    def call(self,event_name,dc,fun=None):
        asyncio.get_event_loop().create_task( self._call(event_name, dc,fun) )
        

        #async def big():
            #rt= await self._call(event_name, dc)
            #if fun:
                #fun(rt)
        
       
        #loop = asyncio.get_event_loop()
        #loop.create_task(self._call(event_name, dc,fun))
        
        #return await asyncio.ensure_future(self._call(event_name, dc))
        #loop.run_until_complete(self._call(event_name, dc))
        #loop.call_soon(self._call,event_name,dc)
    
    async def _call(self,event_name,dc,fun=None):
        self.call_id +=1
        call_id = self.call_id
        out_dc = {'event_name':event_name,'kws':dc,'call_id':call_id}
        #if self.websocket.state ==1:
            #await self.last_call_future
            #self.last_call_future = asyncio.get_event_loop().create_future()
            #await self.websocket.send(json.dumps(out_dc))
            #rt =  await self.last_call_future
            #if fun :
                #fun(rt)
        #else:
            #return None
        if fun and self.websocket.state ==1:
            self.call_front[call_id] = fun
        await self.websocket.send(json.dumps(out_dc))
        

    
    #async def process_queue(self):
        #asyncio.sleep(0.01)
        #for item in list(self.queue):
            #rt = await item()
        #self.queue =[]
        

worker = Router()
#asyncio.get_event_loop().run_until_complete(worker.process_queue())
        
        
        