import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #인터넷 ip버전4(123.123.123.123형태), SOCK_STREAM= TCP통신
google_ip=socket.gethostbyname("google.com")  #구글 ip
sock.connect((google_ip, 80))  # connect() = 튜플형태의 한쌍의 host와 port넘겨 , http 포트 넘버=80

#데이터
sock.send("GET / HTTP/1.1\n".encode())  #socket통신은 바이너리 형태(byte로 형변환), http1.1프로토콜
sock.send("\n".encode()) #내용없음

buffer = sock.recv(4096)  #4096바이트 받아
buffer=buffer.decode().replace("\r\n","\n") #버퍼를 문자열 형태로 디코드 캐리지리턴을 파이썬 형태로 바꿔서 다시 버퍼에 저장
sock.close()

print(buffer)

'''
HTTP/1.1 200 OK
Date: Fri, 04 Sep 2020 11:24:25 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
P3P: CP="This is not a P3P policy! See g.co/p3phelp for more info."
Server: gws
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN
Set-Cookie: 1P_JAR=2020-09-04-11; expires=Sun, 04-Oct-2020 11:24:25 GMT; path=/; domain=.google.com; Secure
Set-Cookie: NID=204=dpmwIFDg14S40wODt9GhPJR__YUc6fsih_moMb7W_iFjNC2LFxd-pnfavX4j_KgmK4VGLlRwXTwv6kxPklPpQJZHd486vdoBZ3LImc9EyYcnWO7y6kwIMjqXk8slGvGF7CT2lau_Srf1__vZ8YxIcHzwho8sxf5_8nC19ofe1TI; expires=Sat, 06-Mar-2021 11:24:25 GMT; path=/; domain=.google.com; HttpOnly
Accept-Ranges: none
Vary: Accept-Encoding
Transfer-Encoding: chunked

500b
<!doctype html><html itemscope="" itemtype="http://schema.org/WebPage" lang="ko"><head><meta content="text/html; charset=UTF-8" http-equiv="Content-Type"><meta content="/images/branding/googleg/1x/googleg_standard_color_128dp.png" itemprop="image"><title>Google</title><script nonce="oaxy8paB8rwZplPMUS9gEQ==">(function(){window.google={kEI:'6SNSX_ONKdHywQPDsLnYCw',kEXPI:'0,202162,1151585,5662,730,224,5105,206,3204,10,1226,364,1499,612,205,383,246,5,1128,226,648,2982,469,128,5,182,3,374,129,157,173,218,90,41,130,22,735,130,116,215,69,168,408,211,138,515,252,10,1119048,1197761,329506,13677,4855,32691,15248,867,28684,9188,8384,4858,1362,284,9007,3024,4738,5,11033,1808,4020,978,7931,5297,2054,919,874,4192,6430,7432,1571,5525,4516,2778,919,2278,7,85,2711,1593,1279,2212,530,149,1103,840,517,1470,52,4258,312,1137,2,2669,2023,1777,520,1947,2229,93,328,1286,14,2927,2246,1813,1787,3227,2845,7,6068,6286,4455,641,2450,3684,1742,4929,108,3407,908,2,941,2614,2399,1384,6084,1704,473,1098,3,346,230,970,865,4625,148,189,3313,2488,2220,32,5733,4,1528,702,1602,1236,1145,327,79,41,1818,2393,89,1702,52,2377,463,460,1555,1232,1331,1504,1036,1315,3,2108,1172,1426,69,642,1,1390,382,200,2525,286,932,821,690,1968,491,914,1631,1019,508,38,2,158,25,887,564,464,225,430,31,1303,2286,180,108,115,1315,23,201,1556,875,115,52,535,87,1153,1255,1076,1,387,35,970,850,446,2,207,85,26,689,6,632,146,409,110,829,46,84,360,115,2,93,199,596,4,6,57,620,48,1746,8,119,6,867,80,4,72,454,7,30,1245,1082,22,127,286,63,299,279,244,232,187,1,253,289,57,458,11,283,491,901,74,37,49,162,51,679,26,286,262,80,5766110,3376,8797217,1323,549,333,444,1,2,80,1,900,896,1,9,2,2551,1,748,141,59,736,563,1,4265,1,1,2,1017,9,305,3299,248,283,527,32,1,5,7,3,1,7,10,4,9,1,2,2,8,12,6,10,8,2,35,12,2,1,23959867,53,2704777,2603,3',kBL:'QdLX'};google.sn='webhp';google.kHL='ko';})();(function(){google.lc=[];google.li=0;google.getEI=function(a){for(var c;a&&(!a.getAttribute||!(c=a.getAttribute("eid")));)a=a.parentNode;return c||google.kEI};google.getLEI=function(a){for(var c=null;a&&(!a.getAttribute||!(c=a.getAttribute("leid")));)a=a.parentNode;return c};google.ml=function(){return null};google.time=function(){return Date.now()};google.log=function(a,c,b,d,g){if(b=google.logUrl(a,c,b,d,g)){a=new Image;var e=google.lc,f=google.li;e[f]=a;a.onerror=a.onload=a.onabort=function(){delete e[f]};google.vel&&google.vel.lu&&google.vel.lu(b);a.src=b;google.li=f+1}};google.logUrl=function(a,c,b,d,g){var e="",f=google.ls||"";b||-1!=c.search("&ei=")||(e="&ei="+google.getEI(d),-1==c.search("&lei=")&&(d=google.getLEI(d))&&(e+="&lei="+d));d="";!b&&google.cshid&&-1==c.search("&cshid=")&&"slh"!=a&&(d="&cshid="+google.cshid);b=b||"/"+(g||"gen_204")+"?atyp=i&ct="+a+"&cad="+c+e+f+"&zx="+google.time()+d;/^http:/i.test(b)&&"https:"==window.location.protocol&&(google.ml(Error("a"),!1,{src:b,glmm:1}),b="");return b};}).call(this);(function(){google.y={};google.x=function(a,b){if(a)var c=a.id;else{do c=Math.random();while(google.y[c])}google.y[c]=[a,b];return!1};google.lm=[];google.plm=function(a){google.lm.push.apply(google.lm,a)};google.lq=[];google.load=function(a,b,c){google.lq.push([[a],b,c])};google.loadAll=function(a,b){google.lq.push([a,b])};}).call(this);google.f={};(function(){
document.documentElement.addEventListener("submit",function(b){var a;if(a=b.target){var c=a.getAttribute("data-subm
'''