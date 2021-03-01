import concurrent.futures
import urllib.request
import time
import queue


class DynThreadPool(object):
    def __init__(self, workers=1,timeout=None):
        #self.q = queue.Queue()
        self.worker_number = workers
        #self.task_dc = {}
        self.timeout=timeout
        self.executor =  concurrent.futures.ThreadPoolExecutor(max_workers=self.worker_number) 
        self.runing_tasks =[]
        self.waiting_tasks = queue.Queue()
        self._quit = False

    def add_task(self,fun,*args,**kws):
        self.waiting_tasks.put(self.executor.submit(fun,*args,**kws))
        #self.q.put({'fun':fun,'kws':kws})
        #self.task_dc[self.executor.submit(fun,)]='FEEDER DONE'

    #def done(self,future):
        #pass
    def quit(self):
        self._quit = True

    def run(self):
        #with concurrent.futures.ThreadPoolExecutor(max_workers=self.worker_number) as executor:

            ## start a future for a thread which sends work in through the queue
            #future_to_url = {
                #executor.submit(feed_the_workers, 0.25): 'FEEDER DONE'}
        #self.runing_tasks = self.waiting_tasks
        while not self.waiting_tasks.empty():
            self.runing_tasks.append(self.waiting_tasks.get())        

        while self.runing_tasks or  not self.waiting_tasks.empty() :
            if self._quit:
                break
            # check for status of the futures which are currently working
            done, not_done = concurrent.futures.wait(
                self.runing_tasks, timeout=1,
                        return_when=concurrent.futures.FIRST_COMPLETED)

            #done, not_done = concurrent.futures.wait(
                #self.task_dc, timeout=0.25,
                #return_when=concurrent.futures.FIRST_COMPLETED)

            # if there is incoming work, start a new future
            while not self.waiting_tasks.empty():
                self.runing_tasks.append(self.waiting_tasks.get())

                # fetch a url from the queue
                #dc = self.q.get()

                ## Start the load operation and mark the future with its URL
                #self.task_dc[self.executor.submit(dc.get('fun'), **dc.get('kws'))] = url

            # process any completed futures
            for future in done:
                yield future
                #self.done(future)
                self.runing_tasks.remove(future)

                #url = future_to_url[future]
                #try:
                    #data = future.result()
                #except Exception as exc:
                    #print('%r generated an exception: %s' % (url, exc))
                #else:
                    #if url == 'FEEDER DONE':
                        #print(data)
                    #else:
                        #print('%r page is %d bytes' % (url, len(data)))

                ## remove the now completed future
                #del future_to_url[future]


#q = queue.Queue()

#URLS = ['http://www.foxnews.com/',
        #'http://www.cnn.com/',
        #'http://europe.wsj.com/',
        #'http://www.bbc.co.uk/',
        #'http://some-made-up-domain.com/']

#def feed_the_workers(spacing):
    #""" Simulate outside actors sending in work to do, request each url twice """
    #for url in URLS + URLS:
        #time.sleep(spacing)
        #q.put(url)
    #return "DONE FEEDING"

#def load_url(url, timeout):
    #""" Retrieve a single page and report the URL and contents """
    #with urllib.request.urlopen(url, timeout=timeout) as conn:
        #return conn.read()

## We can use a with statement to ensure threads are cleaned up promptly
## We can use a with statement to ensure threads are cleaned up promptly
#with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:

    ## start a future for a thread which sends work in through the queue
    #future_to_url = {
        #executor.submit(feed_the_workers, 0.25): 'FEEDER DONE'}

    #while future_to_url:
        ## check for status of the futures which are currently working
        #done, not_done = concurrent.futures.wait(
            #future_to_url, timeout=0.25,
            #return_when=concurrent.futures.FIRST_COMPLETED)

        ## if there is incoming work, start a new future
        #while not q.empty():

            ## fetch a url from the queue
            #url = q.get()

            ## Start the load operation and mark the future with its URL
            #future_to_url[executor.submit(load_url, url, 60)] = url

        ## process any completed futures
        #for future in done:
            #url = future_to_url[future]
            #try:
                #data = future.result()
            #except Exception as exc:
                #print('%r generated an exception: %s' % (url, exc))
            #else:
                #if url == 'FEEDER DONE':
                    #print(data)
                #else:
                    #print('%r page is %d bytes' % (url, len(data)))

            ## remove the now completed future
            #del future_to_url[future]


if __name__ =='__main__':
    import random
    import time
    def wori(msg):
        time.sleep(random.random())
        print(msg)    

    aa = DynThreadPool(workers=20)
    def big_wori():
        for i in range(20):
            aa.add_task(wori,'wori%s'%i)
    aa.add_task(big_wori)
    for future in aa.run():
        pass
    print('over')
