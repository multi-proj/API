#### first trial

```
import urllib3
import json
import base64
openApiURL = "http://aiopen.etri.re.kr:8000/WiseASR/Recognition"
accessKey = "401c8611-d813-426d-9df2-7e6923ec6d3a"
audioFilePath = "test6.m4a"
languageCode = "korean"
 
file = open(audioFilePath, "rb")
audioContents = base64.b64encode(file.read()).decode("utf8")
file.close()
 
requestJson = {
    "access_key": accessKey,
    "argument": {
        "language_code": languageCode,
        "audio": audioContents
    }
}
 
http = urllib3.PoolManager()
response = http.request(
    "POST",
    openApiURL,
    headers={"Content-Type": "application/json; charset=UTF-8"},
    body=json.dumps(requestJson)
)
 
print("[responseCode] " + str(response.status))
print("[responBody]")
print(response.data.decode('utf8'))
```


**사용가능 음성파일** according to [Etri Homepage](http://aiopen.etri.re.kr/guide_recognition.php)
 :  음성인식에 사용하기 위해 샘플링 주파수(sampling rate 또는 sampling frequency) 16kHz로 녹음된 음성 파일
 
 
