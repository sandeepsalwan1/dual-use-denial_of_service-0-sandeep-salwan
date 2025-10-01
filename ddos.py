import time
import asyncio
import aiohttp
import argparse
import json
import random
# Step 1: Make a single non-blocking HTTP request
async def request(url,method='GET',payload=None, headers=None):
    star = time.time()
    async with aiohttp.ClientSession() as session:
        try:
            kwargs = {'headers': headers} if headers else {}
            if method =='POST' and payload:
                kwargs['json'] = payload
            async with session.request(method, url, **kwargs) as resp:
                return {"stat":resp.status, 'success':resp.status < 400, 'time':time.time()-star}

        except Exception as e:
            return {}

async def concurrentReq(url,count,method='GET',payload=None, headers=None):
    coros = [request(url,method,payload,headers) for i in range(count)]
    return await asyncio.gather(*coros)

def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url",help="url")
    parser.add_argument("--payload",help="payload")
    parser.add_argument("--concurrencyCount",help="concurrencyCount")
    parser.add_argument("--mode",choices=["single","manual","continuous"],help="mode")

    # parser.parse_args()
    return parser
async def manual(url,count,header):
    while True:
        try:
            userInput = input(">").strip()
            if userInput == 'q':break
            elif userInput in ['go','g']:
                res = await concurrentReq(url,count,headers=header)
        except KeyboardInterrupt:
            break
            # print()





async def continuous(url,count,header,waitTime):
    # print('a')
    try:
        while True:
            res = await concurrentReq(url,count,headers=header)
            await asyncio.sleep(waitTime)
    except KeyboardInterrupt:
        # print('err')
        pass
            # userInput = input(">").strip()
            # if userInput == 'q':break
            # elif userInput in ['go','g']:


async def main():
    url = "https://xuandi.org"
    res = await request(url)
    res = await concurrentReq(url,6)
    # parser()
    # print( )
    args= parser().parse_args()
    if args.mode== 'manual':
        await manual(url,5,{})
    elif args.mode== 'continuous':
        await continuous(url,5,{},1.2)
    print(res)
    #a
# p

if __name__ == "__main__":
    asyncio.run(main())