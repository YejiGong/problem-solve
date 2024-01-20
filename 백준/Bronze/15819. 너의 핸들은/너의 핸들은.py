N,I = map(int,input().split())
handles=[]

for i in range(N):
    handle = input()
    handles.append(handle)
handles.sort()
print(handles[I-1])