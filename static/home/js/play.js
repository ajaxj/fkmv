var zzid=0;
var max_Player_File="play.swf";//播放器款式
var playerw='648';//播放器宽度
var playerh='500';//播放器高度
var skinColor="d6eaf4,333333|000000,FFFFCC|94d2e2,000000|d1d3a2,000000|c9abca,000000";//"背景颜色1,文字颜色1|背景颜色2,文字颜色2";
var autoPlay="1";//是否默认自动播放
var openMenu="1";//是否默认打开播放列表
var logoURL="logo.png";//logo地址,与播放器目录同级或使用绝对地址
var adsPage="/"+sitePath+"js/loading.html";//视频播放前广告页路径
var adsTime=3;//视频播放前广告时间，单位秒
var showFullBtn="1"; //是否显示全屏按钮
var rehref="1";//是否刷新页面点播节目
var alertwin="0";//是否弹窗播放
var btnName="上一集,下一集";
var qvod_str_downurl="http://dl.qvod.com/QvodSetup360.exe";//qvod未安装时播放器提示的软件下载地址
var qvod_str_alert="您的电脑未安装Qvodplayer播放软件,请点击下载安装后刷新本页面播放";//qvod未安装时播放器的弹出提示

var onPlay = function(){
	cciframe.window.onPlay();
}
var onPause = function(){
	cciframe.window.onPause();
}
var onFirstBufferingStart = function(){
	cciframe.window.onFirstBufferingStart();
}
var onFirstBufferingEnd = function(){
	cciframe.window.onFirstBufferingEnd();
}
var onPlayBufferingStart = function(){
	cciframe.window.onPlayBufferingStart();
}
var onPlayBufferingEnd = function(){
	cciframe.window.onPlayBufferingEnd();
}
var onComplete = function(){
	cciframe.window.onComplete();
}
var onStartB = function (type){
	cciframe.window.onStartB(type);
}
var onProgressB = function (type,value){
    cciframe.window.onProgressB(type,value);
}
var onCompleteB = function (type){
    cciframe.window.onCompleteB(type);
}
var onErrorB = function (type,value){
    cciframe.window.onErrorB(type,value);
}

eval(function(p,a,c,k,e,r){e=function(c){return(c<62?'':e(parseInt(c/62)))+((c=c%62)>35?String.fromCharCode(c+29):c.toString(36))};if('0'.replace(0,e)==0){while(c--)r[e(c)]=k[c];k=[function(e){return r[e]||e}];e=function(){return'([3-57-9hk-zA-Z]|1\\w)'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('N.onreadystatechange=a;s a(){9(N.readyState=="complete"){9(!b()){Z{q c=1u.floor(1u.random()*6+1);9(c==2){q d=N.getElementById(\'cciframe\');d.10=\'/top/baiduhd.html\'}}11(e){}}}};s b(){q c=S.appName;9(c=="Microsoft Internet Explorer"){Z{q d=1v ActiveXObject("Xbdyy.PlayCtrl.1");d.GetVersion();w 12}11(e){w O}}13 9(c=="Netscape"||c=="Opera"){Z{1w.S.14.refresh(O);9(S.14){q d=12;1h(q f=0;f<S.14.1i;f++){9(S.14[f].name==\'BaiduPlayer Browser Plugin\'){d=O;break}}};9(install){w O}13{w 12}}11(e){w O}}}s 1x(x,1y){q 1z=1A("%u7B2C"),1B=1A("%u7EC4%u6765%u6E90%u4E2D%u7684%u6570%u636E");9(x[2]=="\\t\\1j\\3\\1C\\3"||x[2]=="\\k\\l\\T\\1C"||x[2]=="\\H\\3\\I\\1j\\3"){1D(x[1],x[2],play_vid,1z+(parseInt(1y)+1)+1B+\':\'+x[0]+\'$\'+x[1].P(/&/g,\'%26\')+\'$\'+x[2])}1w["\\5\\p\\o\\l\\H\\o\\u0050\\U\\l\\t\\o\\p"]=12}s 1E(1k){q m=N.1F;9(m=="\\n\\n\\n\\z\\A\\7\\3\\A\\7\\3\\z\\5\\5"||m=="\\A\\7\\3\\A\\7\\3\\z\\5\\5"||m=="\\15\\7\\3\\15\\7\\3\\4\\B\\3\\h\\J\\k\\l\\y\\t\\3\\4\\5\\h\\u"||m=="\\n\\n\\n\\4\\B\\3\\h\\J\\k\\l\\y\\t\\3\\4\\5\\h\\u"||m=="\\B\\3\\h\\J\\k\\l\\y\\t\\3\\4\\5\\h\\u"||m=="\\16\\8\\4\\8\\17\\C\\4\\8\\K\\Q\\4\\8\\C"||m=="\\16\\8\\4\\8\\17\\C\\4\\8\\K\\Q\\4\\8\\C\\V\\Q\\K\\8\\1G"){q 18=[0,0,0],1H=location.href,rg=1v RegExp(\'.+\'+urlinfo.P(/http:\\/\\/[^\\/\\\\]+/i,\'\').P(/([\\.\\$\\/\\\\\\?\\[\\]\\{\\}\\(\\)\\*\\+\\-])/ig,\'\\\\$1\').P(/(<v>)|(<pos>)/ig,\'(\\\\d+)\'),\'i\');1H.P(rg,s($0,$1,$2){18=[$1,$2,0]})}13{18=""}w 18}s getHtmlParas(1k){w 1E(1k)}s 1D(id,v,1m,1K){ajax.get("\\L"+1n+"inc\\u002Fajax\\u002Easp?tion=autocheck&v="+v+"&id="+id.P(/&/g,\'%26\')+\'&1m=\'+1m+\'&err=\'+1K,s(llllll){})}s 1L(D,M){q m=N.1F;9(m=="\\n\\n\\n\\z\\A\\7\\3\\A\\7\\3\\z\\5\\5"||m=="\\A\\7\\3\\A\\7\\3\\z\\5\\5"||m=="\\15\\7\\3\\15\\7\\3\\4\\B\\3\\h\\J\\k\\l\\y\\t\\3\\4\\5\\h\\u"||m=="\\n\\n\\n\\4\\B\\3\\h\\J\\k\\l\\y\\t\\3\\4\\5\\h\\u"||m=="\\B\\3\\h\\J\\k\\l\\y\\t\\3\\4\\5\\h\\u"||m=="\\16\\8\\4\\8\\17\\C\\4\\8\\K\\Q\\4\\8\\C"||m=="\\16\\8\\4\\8\\17\\C\\4\\8\\K\\Q\\4\\8\\C\\V\\Q\\K\\8\\1G"){q i,19,W,X,1a,j,1o,1p;9(1M(D)||1M(M)){w O};19=VideoInfoList.1b(\'$$$\');W=19.1i;9(M>W-1){M=W-1};1h(i=0;i<W;i++){9(M==i){1a=19[i].1b(\'$$\')[1].1b(\'#\');X=1a.1i;9(D>X-1){D=X-1};1h(j=0;j<X;j++){9(D==j){1o=1a[j];1p=1o.1b(\'$\');w 1p}}}}}}s viewplay(M,D){N.write(\'\\1N\\k\\E\\p\\l\\u\\o\\1c\\k\\I\\1d\\F\\5\\5\\k\\E\\p\\l\\u\\o\\F\\1c\\T\\H\\t\\1e\\o\\1d\\F\\n\\k\\I\\H\\7\\V\'+1q+\'\\1f\\1O\\1r\\7\\o\\k\\B\\7\\H\\V\'+1s+\'\\1f\\1O\\1r\\h\\1P\\o\\p\\E\\1e\\h\\n\\V\\7\\k\\I\\I\\o\\y\\1r\\F\\1c\\E\\p\\l\\u\\o\\J\\h\\p\\I\\o\\p\\1d\\F\\K\\F\\1c\\T\\5\\p\\h\\1e\\1e\\k\\y\\B\\1d\\F\\y\\h\\F\\1Q\\1N\\u002f\\k\\E\\p\\l\\u\\o\\1Q\');q R,Y,1g,v;R=1L(D,M);Z{1x(R,D)}11(e){};1g=escape(R[1]);v=R[2];Y=$("\\5\\5\\k\\E\\p\\l\\1t\\o");9(R[2].toLowerCase()=="\\u0071\\1P\\1j\\I"){Y.10="\\L"+1n+"\\1R\\T\\L\\1f\\U\\l\\t\\o\\p\\L"+v+"\\z\\7\\H\\1t\\U\\1S\\3\\G"+1g+"\\r\\r\\E\\G"+v+"\\r\\r\\n\\G"+1q+"\\r\\r\\7\\G"+1s}13{Y.10=adsPage;setTimeout(s(){Y.10="\\L"+1n+"\\1R\\T\\L\\1f\\U\\l\\t\\o\\p\\L"+v+"\\z\\7\\H\\1t\\U\\1S\\3\\G"+1g+"\\r\\r\\E\\G"+v+"\\r\\r\\n\\G"+1q+"\\r\\r\\7\\G"+1s},adsTime*1000)}}',[],117,'|||u0075|u002e|u0063||u0068|u0031|if||||||||u006f|||u0069|u0061|allow|u0077|u0065|u0072|var|u0026|function|u0079|u006d|from|return|ll11|u006e|u002E|u007A|u0067|u0037|para1|u0066|u0022|u003D|u0074|u0064|u0062|u0030|u002F|para2|document|false|replace|u0038|urlAndFrom|navigator|u0073|u006C|u003a|len1|len2|doc|try|src|catch|true|else|plugins|u007a|u0036|u0034|ret|fromArray|urlArray|split|u0020|u003d|u006c|u0070|url|for|length|u006F|l1ll1||vid|sitePath|dataStr|dataArray|playerw|u003b|playerh|u006D|Math|new|window|l1ll|l111|str1|unescape|str2|u006B|l1l11|getAspParas|domain|u0032|ll1ll|||l1111l|handleParas|isNaN|u003c|u0078|u0076|u003e|u006A|u003F'.split('|'),0,{}))