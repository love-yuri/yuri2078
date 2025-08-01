# Grpc从入门到入土

> 基于c#  .net8框架

## Hello

### 服务端

#### 1. 安装包

```xml
<PackageReference Include="Google.Protobuf" Version="3.31.1" />
<PackageReference Include="Grpc.Net.Client" Version="2.71.0" />
<PackageReference Include="Grpc.Tools" Version="2.72.0">
  <PrivateAssets>all</PrivateAssets>
  <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
</PackageReference>
```

- [Grpc.Net.Client](https://www.nuget.org/packages/Grpc.Net.Client)，其中包含 .NET Core 客户端。
- [Google.Protobuf](https://www.nuget.org/packages/Google.Protobuf/) 包含适用于 C# 的 Protobuf 消息。
- [Grpc.AspNetCore.Server]() 这个只有server端需要安装，用于启动grpc服务
- [Grpc.Tools](https://www.nuget.org/packages/Grpc.Tools/)，其中包含适用于 Protobuf 文件的 C# 工具支持。 运行时不需要工具包，因此依赖项标记为 `PrivateAssets="All"`。

#### 2. 新增proto通信文件

> 修改.csproj文件后，点击构建, 即可使用构建出来的cs类型
>
> ```xml
> <ItemGroup>
> 	<!-- 这里需server, 也可以用 -->
>     <Protobuf Include="Protos\greet.proto" GrpcServices="Server" />
> </ItemGroup>
> ```

```protobuf
syntax = "proto3";

option csharp_namespace = "GrpcSqlite";

// 最好搞上，做好区分。
package sqlite;

service Greeter {
  rpc SayHello (HelloRequest) returns (HelloReply);
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```

#### 3. 实现服务端

> 继承自`Greeter.GreeterBase`后实现SayHello 方法。

```csharp
public class GreetServer: Greeter.GreeterBase {
    public override Task<HelloReply> SayHello(HelloRequest request, ServerCallContext context)
    {
        return Task.FromResult(new HelloReply {
            Message = "Hello " + request.Name
        });
    }
}
```

#### 4. 启动服务

> 需要配置强制支持http2，不然和客户端通信会有问题

```csharp
var builder = WebApplication.CreateBuilder(args);

// 明确配置 Kestrel 支持 HTTP/2
builder.WebHost.ConfigureKestrel(options => {
    options.ListenLocalhost(5000, listenOptions => {
        listenOptions.Protocols = HttpProtocols.Http2; // 强制 HTTP/2
        // 如果是 HTTPS：
        // listenOptions.UseHttps("cert.pfx", "password");
    });
});

builder.Services.AddGrpc();
var app = builder.Build();
app.MapGrpcService<GreetServer>();
app.Run();
```

### 客户端

> 添加依赖-编写proto-修改csproj 这几个操作和上面几乎一致

```csharp
var httpHandler = new HttpClientHandler {
    UseProxy = false,
    Proxy = null
};

var channel = GrpcChannel.ForAddress("http://localhost:5000", new GrpcChannelOptions {
    HttpHandler = httpHandler
});

var client = new Greeter.GreeterClient(channel);
var reply = await client.SayHelloAsync(new HelloRequest { Name = "GreeterClient" });
```

