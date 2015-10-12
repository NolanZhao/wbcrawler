# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Oct 4, 2015
@author:       Bo Zhao
@email:        bo_zhao@hks.harvard.edu
@website:      http://yenching.org
@organization: The Ohio State University
'''

# retweet type
# 1: reply
# 2: comment
# 3: reply to a comment
# 4: a reply and a comment


# status type
# 0: original
# 1: reply
# 2: comments

TOKEN = '2.00UjtoID_vpWMD6803c07a48xPUuYC'
# TOKEN = '2.00UjtoID_vpWMD1961e78a7fdHoBSB' # 旧梦

COUNT = 50
COUNT2 = 100

WAITING_TIME = 20
EMAIL_PASSWORD = 'nanjing1212'
BAIDU_AK = 'Y4wB8DznamkwhY8RxDiYNSHS'

# V10 hc563blnsg@163.com
# ck = 'SINAGLOBAL=71.233.245.138_1443916664.306643; UOR=,login.sina.com.cn,; ULV=1444533746724:6:6:6:128.103.193.220_1444533692.708269:1444533691849; U_TRS1=0000008a.31b230f.5611503b.60a80b4a; sso_info=v02m6alo5qztY2alrmpl7WIpZGTlKWQo4CljoSYpZGTnKWOk5ilkJSYpZGTlKWQlJCljpOAto6DmLiJp5WpmYO0tYyTkLKNg4yxjbOQtQ==; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWYTG863MkPLheimog5d7c_; Apache=128.103.193.220_1444533692.708269; SUB=_2A257HaZQDeTxGeNP71AV8y_LzzmIHXVYapCYrDV_PUNbuNBuLRXhkW95xZNoC3_KW-_S44QmUoB0s3tVOQ..; SUS=SID-5142431745-1444533760-GZ-1tq85-fa3ae86b47c6ec5ceaab4ca6dee65772; SUE=es%3Dee63ed2ef156ea0f69060e2e3d880f76%26ev%3Dv1%26es2%3Da3c8149d6982eecc3a8d08e71de4d052%26rs0%3DI%252Bnn3ddtLTnULoBjVJ0gd74Rs%252B6xEUdQbhw%252F4FVVv90lcXhE0xEYQyj%252F0KgGvwveuSLo5GM8jVdb2mNDp3ZNgzX0l6T0GdXAQl8HzxRSMCzqubkLGciyyKaO%252FO3uslMF9YmzN2pUMFyK%252BoSVjQbUjAA4y%252BsjstYQuLyIoUfdRtQ%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1444533760%26et%3D1444620160%26d%3D40c3%26i%3D5772%26us%3D1%26vf%3D1%26vt%3D4%26ac%3D59%26st%3D0%26lt%3D1%26uid%3D5142431745%26user%3Dhc563blnsg%2540163.com%26ag%3D4%26name%3Dhc563blnsg%2540163.com%26nick%3DMini_R%25E5%25B0%258F%25E7%2596%25AF%25E5%25AD%25906868%26sex%3D1%26ps%3D0%26email%3D%26dob%3D%26ln%3Dhc563blnsg%2540163.com%26os%3D%26fmp%3D%26lcp%3D2015-08-21%252014%253A21%253A57; ALF=1476069760; cREMloginname=hc563blnsg%40163.com; tgc=TGT-NTE0MjQzMTc0NQ==-1444533760-hk-D0E3413E59F324F00D4018D60EBD1BA3; ALC=ac%3D59%26bt%3D1444533760%26cv%3D5.0%26et%3D1476069760%26uid%3D5142431745%26vf%3D1%26vt%3D4%26es%3D43bf3c8f217a250b6bb21b7a731ecefd; LT=1444533760'
# 'v8 ' vcjmi41976504@126.com
#ck = 'SINAGLOBAL=23.127.5.35_1438381099.222158; UOR=www.google.com,blog.sina.com.cn,; U_TRS1=00000023.58191642.55bccd5d.3f434700; vjuids=-28335e30f.14ee982b46a.0.7a397cda; SGUID=1438436749265_34644990; lxlrtst=1443666296_o; ArtiFSize=14; lxlrttp=1443792570; Apache=71.233.245.138_1444060264.797192; U_TRS2=0000008a.417f4a43.5612acdf.a2f005e1; rotatecount=1; ULV=1444064489714:25:6:3:71.233.245.138_1444060264.797192:1443977692349; SessionID=17ma3rp8l85lcm38jdcht2sli2; vjlast=1443843509.1444064538.10; tgc=TGT-NTMyNzIyMjI0MQ==-1444064615-hk-4CBBCBCF9852ADCAEE36074A18BA5AE3; SUS=SID-5327222241-1444064615-GZ-06p1o-c8680828e7b5bf34ec19c5ff3c414b4a; SUE=es%3D3eb57f79b2478142c1c163f1f04dd320%26ev%3Dv1%26es2%3D58e03d54fcf56e4b26a0ec869846a600%26rs0%3DoUxbAw2fWw9dVeT0SP7yZSkyFBQ2xG%252B%252FYHIC1jMWqK5lcTTEAJW%252FpUwgDLCtYItNBXlbmlt%252FpbZ0ETvhndzqgvBduu8E7e5gyUOqieHyegZln0ixdC0GrL%252FR2PgG23i5YfVoGTJGmjYacAdqdpNZpe9i1Pu2CVp9UbU8CTm2zvw%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1444064615%26et%3D1444151015%26d%3D40c3%26i%3D4b4a%26us%3D1%26vf%3D1%26vt%3D2%26ac%3D59%26st%3D0%26lt%3D1%26uid%3D5327222241%26user%3Dvcjmi41976504%2540126.com%26ag%3D4%26name%3Dvcjmi41976504%2540126.com%26nick%3Dtwwetii793256%26sex%3D1%26ps%3D0%26email%3D%26dob%3D%26ln%3Dvcjmi41976504%2540126.com%26os%3D%26fmp%3D%26lcp%3D2015-09-21%252012%253A12%253A26; SUB=_2A257Ft03DeTxGeNN6VUT8izOzz2IHXVYYkn_rDV_PUNbuNBuLVnhkW8y8EtsqeTGpAdC1CuIzl_GkgZhFQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.49SfQ89T4PqZKkwsSCmT; ALC=ac%3D59%26bt%3D1444064615%26cv%3D5.0%26et%3D1475600615%26uid%3D5327222241%26vf%3D1%26vt%3D2%26es%3D5f8496c44c9f9c0b5c3af5fa3d563bdc; ALF=1475600615; LT=1444064615; sso_info=v02m6alo5qztbSdt52lnYalqY2zpLOMo5S2iaeVqZmDtLWMs4i3jKOIsoyjkLE=; cREMloginname=vcjmi41976504%40126.com'
# ck2= 'SINAGLOBAL=23.127.5.35_1438381099.222158; UOR=www.google.com,blog.sina.com.cn,; U_TRS1=00000023.58191642.55bccd5d.3f434700; vjuids=-28335e30f.14ee982b46a.0.7a397cda; SGUID=1438436749265_34644990; lxlrtst=1443666296_o; ArtiFSize=14; lxlrttp=1443792570; Apache=71.233.245.138_1444060264.797192; U_TRS2=0000008a.417f4a43.5612acdf.a2f005e1; rotatecount=1; ULV=1444064489714:25:6:3:71.233.245.138_1444060264.797192:1443977692349; SessionID=17ma3rp8l85lcm38jdcht2sli2; vjlast=1443843509.1444064538.10; tgc=TGT-NTMyNzIyMjI0MQ==-1444064615-hk-4CBBCBCF9852ADCAEE36074A18BA5AE3; SUS=SID-5327222241-1444064615-GZ-06p1o-c8680828e7b5bf34ec19c5ff3c414b4a; SUE=es%3D3eb57f79b2478142c1c163f1f04dd320%26ev%3Dv1%26es2%3D58e03d54fcf56e4b26a0ec869846a600%26rs0%3DoUxbAw2fWw9dVeT0SP7yZSkyFBQ2xG%252B%252FYHIC1jMWqK5lcTTEAJW%252FpUwgDLCtYItNBXlbmlt%252FpbZ0ETvhndzqgvBduu8E7e5gyUOqieHyegZln0ixdC0GrL%252FR2PgG23i5YfVoGTJGmjYacAdqdpNZpe9i1Pu2CVp9UbU8CTm2zvw%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1444064615%26et%3D1444151015%26d%3D40c3%26i%3D4b4a%26us%3D1%26vf%3D1%26vt%3D2%26ac%3D59%26st%3D0%26lt%3D1%26uid%3D5327222241%26user%3Dvcjmi41976504%2540126.com%26ag%3D4%26name%3Dvcjmi41976504%2540126.com%26nick%3Dtwwetii793256%26sex%3D1%26ps%3D0%26email%3D%26dob%3D%26ln%3Dvcjmi41976504%2540126.com%26os%3D%26fmp%3D%26lcp%3D2015-09-21%252012%253A12%253A26; SUB=_2A257Ft03DeTxGeNN6VUT8izOzz2IHXVYYkn_rDV_PUNbuNBuLVnhkW8y8EtsqeTGpAdC1CuIzl_GkgZhFQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW.49SfQ89T4PqZKkwsSCmT; ALC=ac%3D59%26bt%3D1444064615%26cv%3D5.0%26et%3D1475600615%26uid%3D5327222241%26vf%3D1%26vt%3D2%26es%3D5f8496c44c9f9c0b5c3af5fa3d563bdc; ALF=1475600615; LT=1444064615; sso_info=v02m6alo5qztbSdt52lnYalqY2zpLOMo5S2iaeVqZmDtLWMs4i3jKOIsoyjkLE=; cREMloginname=vcjmi41976504%40126.com'
# V6  bcebrierbb@sina.cn
# ck = 'SINAGLOBAL=23.127.5.35_1438381099.222158; UOR=www.google.com,blog.sina.com.cn,; U_TRS1=00000023.58191642.55bccd5d.3f434700; vjuids=-28335e30f.14ee982b46a.0.7a397cda; SGUID=1438436749265_34644990; ArtiFSize=14; lxlrtst=1444202415_o; lxlrttp=1444202415; ULV=1444366953628:27:8:5:71.233.245.138_1444363148.872468:1444145120706; vjlast=1444210485.1444366955.10; Apache=128.103.193.220_1444400547.219142; U_TRS2=000000dc.c8f44961.5617ed4a.e2402202; ULOGIN_IMG=hk-20262f018cfcd69a4bbaf39901bbb3d382fa; tgc=TGT-Mjk0MjI5NTIxNA==-1444410635-hk-9CD7FA1FD36CDADE404183CBF4F9AB4E; SUS=SID-2942295214-1444410635-GZ-qh1y9-9074c5dc349affbb1ea026f2ae9e5772; SUE=es%3D4efbbbc2a77b2afdb50220c5732230b4%26ev%3Dv1%26es2%3D8067b5b4392ec1fe4d9cb8316dd41a37%26rs0%3DyBsfh%252Brh%252FUDc8qpEShh4BSEvzvf9ZTEd5pvd4Yl34yYDaYiWBL%252BqhrpMmOChjrPaJsFKL%252FaDsplevUdCbtDxLTf%252BPdiClb3ip8WyYRIOcwrJ7q33vXrdTltyP%252FHCCRJ%252FbFaxqpA81bjyuXt%252BMJatytmbGSb%252FWOXviJJPECcz0e4%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1444410635%26et%3D1444497035%26d%3D40c3%26i%3D5772%26us%3D1%26vf%3D0%26vt%3D0%26ac%3D59%26st%3D0%26lt%3D1%26uid%3D2942295214%26user%3Dbcebrierbb.cn%26ag%3D8%26name%3Dbcebrierbb%2540sina.cn%26nick%3Dihcalta0vvjafge0%26sex%3D%26ps%3D0%26email%3Dbcebrierbb%2540sina.cn%26dob%3D%26ln%3Dbcebrierbb%2540sina.cn%26os%3D%26fmp%3D%26lcp%3D2015-10-04%252016%253A07%253A11; SUB=_2A257E4VbDeTxGeRH71AT-SvOyjiIHXVYaPGTrDV_PUNbuNBuLUXykW8PqFQQs7Jr34TmNjEn9d-UItedjw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhGc6hpzvDioaZ2zHoxHijy; ALC=ac%3D59%26bt%3D1444410635%26cv%3D5.0%26et%3D1475946635%26uid%3D2942295214%26vf%3D0%26vt%3D0%26es%3D6e6af51848d5d1d5b953470d4aec8442; ALF=1475946635; LT=1444410635; sso_info=v02m6alo5qztamaho2hm4eRoYyHmbaapoWmmbaUsImnlamZg7SyjpOQsoyjpLWMo4S0'

# V6 flk0gw4k0gwc@sina.cn
# ck = 'SINAGLOBAL=71.233.245.138_1443916664.306643; UOR=,login.sina.com.cn,; ULV=1444586586600:7:7:1:128.103.193.220_1444586553.916660:1444533746724; U_TRS1=0000008a.31b230f.5611503b.60a80b4a; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFFlPez3dFpyDKcX64dPgTB; SUB=_2A257HtQ-DeTxGeRH4lEX-CbPyj6IHXVYakL2rDV_PUNbuNBuLWX6kW8ZCE1AD3uFpRE1Hmv695mH2I6g9g..; Apache=128.103.193.220_1444586553.916660; SUS=SID-2993688312-1444586606-GZ-1eb9f-fba363d05d0843d96a25d930fddd5772; SUE=es%3De4fee4051fbf093a65e1cd6d5aa3acc5%26ev%3Dv1%26es2%3D0645da21f17fc16499a402d4379220cd%26rs0%3D3RLm5s2D99iCN4%252B3kav3jD4M2Ct04jkDr7O%252BpMOE9o22eFNG6gYEseVqSu5WmeXqiJnNOdF%252BhhHrkC1pt7xDVN4JPYCv5J%252B4UVwcHYlsq2OzzC39g8pEMvt%252Fw0RCZiWSarQU%252BKD8UtpFzhu8ht1RUlfUkDM0uGRB9nGfZIV8n%252Bg%253D%26rv%3D0; SUP=cv%3D1%26bt%3D1444586606%26et%3D1444673006%26d%3D40c3%26i%3D5772%26us%3D1%26vf%3D1%26vt%3D2%26ac%3D59%26st%3D0%26lt%3D1%26uid%3D2993688312%26user%3Dflk0gw4k0gwc.cn%26ag%3D8%26name%3Dflk0gw4k0gwc%2540sina.cn%26nick%3Dhgb1vbr7n3jzfn3j%26sex%3D%26ps%3D0%26email%3Dflk0gw4k0gwc%2540sina.cn%26dob%3D%26ln%3Dflk0gw4k0gwc%2540sina.cn%26os%3D%26fmp%3D%26lcp%3D2015-10-04%252016%253A07%253A57; ALF=1476122606; sso_info=v02m6alo5qztaiZtoixnaaJso22uLOap6mmm6ONqomnlamZg7SyjpOks42joLiMs4Sy; tgc=TGT-Mjk5MzY4ODMxMg==-1444586606-hk-6E6FD82615D61319FA6AAD9F51A7AAFA; ALC=ac%3D59%26bt%3D1444586606%26cv%3D5.0%26et%3D1476122606%26uid%3D2993688312%26vf%3D1%26vt%3D2%26es%3D3140ae6e2e05acbf9f7ef785a4f748c4; LT=1444586606; cREMloginname=flk0gw4k0gwc%40sina.cn'

username = "vcjmi41976504@126.com"
password = "zx1987"
