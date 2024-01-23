import requests, queue, threading, sys, time

host = sys.argv[1]
threads = int(sys.argv[2])
try:
    ext = sys.argv[3]
except:
    ext = False
    pass


try:
    requests.get(host)
except Exception as e:
    print(e)
    exit(0)

start = time.time()

print("[+] Scanning for directories..")

directory_list = open('/usr/share/dirbuster/wordlists/directory-list-lowercase-2.3-small.txt', 'r')

q = queue.Queue()

count = 0

def dirbuster(thread_no, q):
    global count
    while not q.empty():
        url = q.get()
        try:
            response = requests.get(url, allow_redirects=True, timeout=2)
            count += 1
            if response.status_code == 200:
                print("[+] Directory found: {}".format(str(response.url)))
        except:
             pass
        q.task_done()

for directory in directory_list.read().splitlines():
    if not ext:
        url = host + '/' + directory
    else:
        url = host + '/' + directory + ext
    q.put(url)

for i in range(threads):
    t = threading.Thread(target = dirbuster, args=(i, q))
    t.daemon = True
    t.start()

    q.join()  
    print("Time taken: {}".format(time.time() - start))
