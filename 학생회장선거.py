from tkinter import *
from tkinter import messagebox
from functools import partial
from datetime import datetime
import csv
#import winsound

cand1_list = '유준우(2813) 공민준(2901) 김동연(2304) 도지호(2210)'.split()
cand2_list = '서찬우(1416) 박상현(1708) 이현진(1518) 조우현(1726)'.split()

df = ('Malgun Gothic', 25)
bf = ('Malgun Gothic', 25, 'bold')

wd = Tk()
w, h = wd.winfo_screenwidth(), wd.winfo_screenheight()
wd.geometry("+0+0")
wd.title('인하부중 학생회장 선거')

Label(wd, text='학생회장 및 3학년 부회장 후보', font=df, height=2).grid(row=0, column=0)
Label(wd, text='2학년 부회장 후보', font=df, height=2).grid(row=0, column=1)

bw = 30
bh = 2

v1 = ''
v2 = ''

def select(r, k):
    global v1, v2
    if k == 0:
        v1 = cand1_list[r-1]
        cand1_vote.configure(text=v1)
    elif k == 1:
        v2 = cand2_list[r-1]
        cand2_vote.configure(text=v2)

    if len(v1) and len(v2):
        submit.configure(state='normal')
def vote():
    global v1, v2
    t = datetime.now().strftime('%m.%d.%H:%M:%S')
    print(t, v1, v2)
    f = open('vote.csv', 'a', encoding='euckr')
    g = csv.writer(f, delimiter=',')
    g.writerow([t, v1, v2])
    f.close()
    messagebox.showinfo('투표 완료', t + ' ' + v1 + ' ' + v2 )

    v1 = ''
    v2 = ''
    cand1_vote.configure(text='미선택')
    cand2_vote.configure(text='미선택')
    submit.configure(state='disabled')

r = 1
for c in cand1_list:
    Button(wd, text=c, font=bf, width=bw, height=bh, command=partial(select, r, 0)).grid(row=r, column=0)
    r += 1

r = 1
for c in cand2_list:
    Button(wd, text=c, font=bf, width=bw, height=bh, command=partial(select, r, 1)).grid(row=r, column=1)
    r += 1

cand1_list.append('기권')
cand2_list.append('기권')
Button(wd, text='기권', font=df, command=partial(select, r, 0)).grid(row=r, column=0)
Button(wd, text='기권', font=df, command=partial(select, r, 1)).grid(row=r, column=1)
cand1_vote = Label(wd, text='미선택', font=bf, width=bw, height=bh)
cand1_vote.grid(row=r+1, column=0)
cand2_vote = Label(wd, text='미선택', font=bf, width=bw, height=bh)
cand2_vote.grid(row=r+1, column=1)
submit = Button(wd, text='투표 완료', font=bf, width=bw*2, height=bh, command=vote, state='disabled')
submit.grid(row=r+2, column=0, columnspan=2)

wd.mainloop()
