var CryptoJS = require("crypto-js");
var WebSocketClient = require("websocket").client;
var fs = require("fs");

// AIUI websocket服务地址
const BASE_URL = "wss://aiui.xf-yun.com/v2/aiui/ws";

// 应用配置
const APPID = "";
const API_KEY = "";
const API_SECRET = "";

// 场景
var scene = "main_box";

// 请求类型用来设置文本请求还是音频请求，text/audio
// 音频请求需要先设置audio_path
// 当前音频格式默认pcm 16k 16bit，修改音频格式需要修改audioReq中的payload中音频相关参数
var reqType = "text";

// 请求文本
var payLoadText = "你是谁";

// 每帧音频数据大小，单位字节
var chunckSize = 1024;
// 音频文件位置
var filePath = "D:/temp/audio/date.pcm";

// 生成握手连接
function assembleAuthUrl(url) {
  var u = new URL(url);
  var host = u.host;
  var path = u.pathname;
  var date = new Date().toGMTString();

  var signatureOrigin = `host: ${host}\ndate: ${date}\nGET ${path} HTTP/1.1`;
  // console.log("signatureOrigin: " + signatureOrigin)
  var signatureSha = CryptoJS.HmacSHA256(signatureOrigin, API_SECRET);
  var signature = CryptoJS.enc.Base64.stringify(signatureSha);

  var authorizationOrigin = `api_key="${API_KEY}", algorithm="hmac-sha256", headers="host date request-line", signature="${signature}"`;
  // console.log("authorizationOrigin:" + authorizationOrigin)
  var authorization = btoa(authorizationOrigin);

  return `${url}?authorization=${authorization}&date=${date}&host=${host}`;
}

function base64Str(str) {
  return Buffer.from(str, "utf-8").toString("base64");
}

function deBase64Str(str) {
  return Buffer.from(str, "base64").toString("utf-8");
}

// 定义websocket client
var client = new WebSocketClient();

client.on("connectFailed", function (error) {
  // 建立连接失败
  console.log("Connect fail Error: " + error.toString());
});

client.on("connect", function (connection) {
  // 连接建立成功
  console.log("WebSocket client connected");

  connection.on("error", function (error) {
    console.log("Connection Error: " + error.toString());
  });
  connection.on("close", function () {
    console.log("echo-protocol Connection Closed");
  });
  connection.on("message", function (message) {
    // 结果解析
    if (message.type === "utf8") {
      var res = JSON.parse(message.utf8Data);
      var header = res["header"];
      var code = header["code"];
      if (code != 0) {
        console.log("request error: " + message.utf8Data);
        connection.close();
        return;
      }
      if ("payload" in res) {
        var payLoad = res["payload"];
        if ("nlp" in payLoad) {
          var nlp_json = payLoad["nlp"];
          var nlp_text_bs64 = nlp_json["text"];
          var nlp_text = deBase64Str(nlp_text_bs64);
          console.log("语义结果：" + nlp_text);
        }
        if ("iat" in payLoad) {
          var iat_json = payLoad["iat"];
          var iat_text_bs64 = iat_json["text"];
          var iat_text = deBase64Str(iat_text_bs64);
          console.log("识别结果：" + iat_text);
        }
      }
      if ("status" in header && header["status"] == 2) {
        console.log("结果接收完成");
        connection.close();
      }
    }
  });

  // 发送数据
  if (connection.connected) {
    sendMsg(connection);
  }
});

function sendMsg(conn) {
  if (reqType == "text") {
    var req = genTextReq();
    console.log("text req: " + req);
    conn.sendUTF(req);
  }
  if (reqType == "audio") {
    // 获取文件长度
    const fileLen = fs.statSync(filePath).size;
    var idx = 0;
    var idxMax = Math.ceil(fileLen / chunckSize);
    // 分片读取文件
    const stream = fs.createReadStream(filePath, {
      highWaterMark: chunckSize,
    });
    //  处理文件块回调
    function processChunk(data) {
      var status = 0;
      idx++;
      if (idxMax == 1) {
        // 一帧传完
        status = 3;
      } else if (idx == idxMax) {
        // 尾帧
        status = 2;
      } else if (idx != 1) {
        // 中间帧
        status = 1;
      }

      var req = genAudioReq(data, status);
      conn.sendUTF(req);
    }

    stream.on("data", processChunk);
    stream.on("error", (err) => {
      console.error("读取文件出错：", err);
    });
  }
}

function genTextReq() {
  // 构造文本请求参数
  var req = {
    header: {
      uid: "1234567891",
      app_id: APPID,
      stmid: "text-1",
      status: 3,
      scene: scene,
    },
    parameter: {
      nlp: {
        nlp: {
          compress: "raw",
          format: "json",
          encoding: "utf8",
        },
        sub_scene: "cbm_v45",
        new_session: true,
      },
    },
    payload: {
      text: {
        compress: "raw",
        format: "plain",
        text: base64Str(payLoadText),
        encoding: "utf8",
        status: 3,
      },
    },
  };
  return JSON.stringify(req);
}

function genAudioReq(data, status) {
  // 构造pcm音频请求参数
  var dataBase64 = Buffer.from(data).toString("base64");
  req = {
    header: {
      uid: "1234567891",
      app_id: APPID,
      stmid: "audio-1",
      status: status,
      scene: scene,
    },
    parameter: {
      nlp: {
        nlp: {
          compress: "raw",
          format: "json",
          encoding: "utf8",
        },
        sub_scene: "cbm_v45",
        new_session: true,
      },
    },
    payload: {
      audio: {
        encoding: "raw",
        sample_rate: 16000,
        channels: 1,
        bit_depth: 16,
        frame_size: data.length,
        status: status,
        audio: dataBase64,
      },
    },
  };
  return JSON.stringify(req);
}

// 建立连接
var handshakeUrl = assembleAuthUrl(BASE_URL);
var u = new URL(BASE_URL);
var host = u.host;
var path = u.pathname;
var origin = "http://" + host + path;

client.connect(handshakeUrl, "", origin);
