https://cloud.tencent.com/document/product/436/35151#.E4.B8.8A.E4.BC.A0.E5.AF.B9.E8.B1.A1.EF.BC.88.E6.96.AD.E7.82.B9.E7.BB.AD.E4.BC.A0.EF.BC.89



| 参数名称           | 参数描述                                                     | 类型   | 是否必填 |
| :----------------- | :----------------------------------------------------------- | :----- | :------- |
| Bucket             | 存储桶名称，由 BucketName-APPID 构成                         | String | 是       |
| Key                | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名 `examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg` 中，对象键为 doc/pic.jpg | String | 是       |
| LocalFilePath      | 本地文件的路径名                                             | String | 是       |
| PartSize           | 分块上传的分块大小，默认为1MB                                | Int    | 否       |
| MAXThread          | 分块上传的并发数量，默认为5个线程上传分块                    | Int    | 否       |
| EnableMD5          | 是否需要 SDK 计算 Content-MD5，默认关闭，打开后会增加上传耗时 | Bool   | 否       |
| ACL                | 设置对象的 ACL，例如 'private'，'public-read'                | String | 否       |
| GrantFullControl   | 赋予被授权者所有的权限，格式为 `id="OwnerUin"`               | String | 否       |
| GrantRead          | 赋予被授权者读的权限，格式为 `id="OwnerUin"`                 | String | 否       |
| StorageClass       | 设置对象的存储类型，STANDARD，STANDARD_IA，ARCHIVE。默认值 STANDARD | String | 否       |
| Expires            | 设置 Expires                                                 | String | 否       |
| CacheControl       | 缓存策略，设置 Cache-Control                                 | String | 否       |
| ContentType        | 内容类型，设置 Content-Type                                  | String | 否       |
| ContentDisposition | 文件名称，设置 Content-Disposition                           | String | 否       |
| ContentEncoding    | 编码格式，设置 Content-Encoding                              | String | 否       |
| ContentLanguage    | 语言类型，设置 Content-Language                              | String | 否       |
| ContentLength      | 设置传输长度                                                 | String | 否       |
| ContentMD5         | 设置上传对象的 MD5 值用于校验                                | String | 否       |
| Metadata           | 用户自定义的对象元数据                                       | Dict   | 否       |
| TrafficLimit       | 单链接限速的值，单位为bit/s，限速值设置范围为819200 - 838860800，即100KB/s - 100MB/s，高级接口限制的是单线程的速度 | String | 否       |











| 参数名称                   | 参数描述                                                     | 类型   | 是否必填 |
| :------------------------- | :----------------------------------------------------------- | :----- | :------- |
| Bucket                     | 存储桶名称，由 BucketName-APPID 构成                         | String | 是       |
| Key                        | 对象键（Key）是对象在存储桶中的唯一标识。例如，在对象的访问域名`examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/doc/pic.jpg`中，对象键为 doc/pic.jpg | String | 是       |
| DestFilePath               | 文件下载的本地目的路径名                                     | String | 是       |
| PartSize                   | 分块下载的分块大小，默认为20MB                               | Int    | 否       |
| MAXThread                  | 分块下载的并发数量，默认为5个线程下载分块                    | Int    | 否       |
| EnableCRC                  | 是否开启本地文件与远程文件的 crc 校验，默认为 False          | Bool   | 否       |
| TrafficLimit               | 单链接限速的值，单位为bit/s，限速值设置范围为819200 - 838860800，即100KB/s - 100MB/s，高级接口限制的是单线程的速度 | String | 否       |
| IfMatch                    | ETag 与指定的内容一致时才返回                                | String | 否       |
| IfModifiedSince            | 在指定时间后被修改才返回，时间格式为 GMT                     | String | 否       |
| IfNoneMatch                | ETag 与指定的内容不一致才返回                                | String | 否       |
| IfUnmodifiedSince          | 对象修改时间早于或等于指定时间才返回，时间格式为 GMT         | String | 否       |
| ResponseCacheControl       | 设置响应头部 Cache-Control                                   | String | 否       |
| ResponseContentDisposition | 设置响应头部 Content-Disposition                             | String | 否       |
| ResponseContentEncoding    | 设置响应头部 Content-Encoding                                | String | 否       |
| ResponseContentLanguage    | 设置响应头部 Content-Language                                | String | 否       |
| ResponseContentType        | 设置响应头部 Content-Type                                    | String | 否       |
| ResponseExpires            | 设置响应头部 Expires                                         | String | 否       |
| VersionId                  | 指定下载对象的版本                                           | String | 否       |











