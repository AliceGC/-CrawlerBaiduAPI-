# -基于百度地图API爬取两地驾车时长-
利用百度地图提供的API接口，爬取武汉市至全国各个城市的公路历程以及驾车时长。

### 步骤
1. 从csv文档获取城市名，并通过地理编码服务获得各目标城市的经纬度
2. 基于经纬度，通过批量算路服务获取武汉市与目标城市之间的公路里程与驾车时长 【可选择不同策略】

### 官方网址：
[地理编码服务](http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-geocoding)
[百度API批量算路服务](http://lbsyun.baidu.com/index.php?title=webapi/route-matrix-api-v2)
